# -*- coding: utf-8 -*-
"""
hangulize
~~~~~~~~~

Korean Alphabet Transcription.
"""
import sys
import re
import unicodedata
from hangulize.hangul import *


SPACE = '_' # u'\U000f0000'
SPECIAL = chr(27) #u'\U000f0000'
BLANK = '(?:%s|%s)' % tuple(map(re.escape, (SPACE, SPECIAL)))
DONE = chr(0) #u'\U000fffff'
ENCODING = getattr(sys.stdout, 'encoding', 'utf-8')


class Phoneme(object):
    """This abstract class wraps a Hangul letter."""

    def __init__(self, letter):
        self.letter = letter

    def __repr__(self):
        name = type(self).__name__
        return "<%s '%s'>" % (name, self.letter.encode(ENCODING))


class Choseong(Phoneme):
    """A initial consonant in Hangul.

        >>> Choseong(G)
        <Choseung 'ㄱ'>
    """
    pass


class Jungseong(Phoneme):
    """A vowel in Hangul.

        >>> Jungseong(A)
        <Jungseong 'ㅏ'>
    """
    pass


class Jongseong(Phoneme):
    """A final consonant in Hangul.

        >>> Jongseong(G)
        <Jongseong 'ㄱ'>
    """
    pass


class Impurity(Phoneme):
    """An impurity letter will be kept."""
    pass


class Notation(object):
    """Describes loanword orthography.

    :param *rule: the ordered key-value list
    """

    VARIABLE_PATTERN = re.compile('<(?P<name>[a-zA-Z_][a-zA-Z0-9_]*)>')
    LEFTEDGE_PATTERN = re.compile(r'^\^\^')
    RIGHTEDGE_PATTERN = re.compile(r'\$\$$')
    LOOKBEHIND_PATTERN = re.compile('^(\^?){([^}]+?)}')
    LOOKAHEAD_PATTERN = re.compile('{([^}]+?)}(\$?)$')

    def __init__(self, rules):
        self.rules = rules

    def items(self, left_edge=False, right_edge=False, lang=None):
        """Yields each notation rules as regex."""
        for one in self.rules:
            pattern = one[0]
            # accept *args
            if len(one) == 2:
                val = one[1]
                if isinstance(val, Phoneme):
                    val = val,
            # accept args(a tuple instance)
            else:
                val = one[1:]
            yield pattern, val

    @property
    def chars(self):
        """The humane characters from the notation keys."""
        chest = []
        for one in self.rules:
            pattern = self.VARIABLE_PATTERN.sub('', one[0])
            pattern = re.sub(r'[\{\}\@\[\]\^\$]', '', pattern)
            for c in pattern:
                chest.append(c)
        return set(chest)


class Language(object):
    """Wraps a foreign language. The language should have a :class:`Notation`
    instance.

        >>> class Extraterrestrial(Language):
        ...     notation = Notation(
        ...         (u'ㅹ', (Choseong(BB), Jungseong(U), Jongseong(NG))),
        ...         (u'㉠', (Choseong(G),)),
        ...         (u'ㅣ', (Jungseong(I),)),
        ...         (u'ㅋ', (Choseong(K), Jungseong(I), Jongseong(G)))
        ...     )
        ...
        >>> ext = Extraterrestrial()
        >>> print ext.hangulize(u'ㅹ㉠ㅣㅋㅋㅋ')
        뿡기킥킥킥

    :param logger: the logger object in the logging module
    """

    vowels = ()
    notation = None
    special = '.,;?~"()[]{}'

    def __init__(self, logger=None):
        if not isinstance(self.notation, Notation):
            raise NotImplementedError("notation has to be defined")
        self.logger = logger

    @property
    def chars_pattern(self):
        """The regex pattern which is matched the valid characters."""
        return ''.join(re.escape(c) for c in self.notation.chars)

    def split(self, string):
        """Splits words from the string. Each words have only valid characters.
        """
        pattern = '[^%s]+' % self.chars_pattern
        return re.split(pattern, string)

    def transcribe(self, string):
        """Returns :class:`Phoneme` instance list from the word."""
        string = re.sub(r'\s+', SPACE, string)
        string = re.sub(r'^|$', SPECIAL, string)
        self._log(".. '%s'" % string)
        phonemes = []
        # escape special characters
        for esc in self.special:
            rewrite = Rewrite(re.escape(esc), (Impurity(esc),))
            string = rewrite(string, phonemes)
        string = Rewrite(DONE, SPECIAL)(string, phonemes)
        # apply the notation
        for item in self.notation.items():
            rewrite = Rewrite(*item)
            string = rewrite(string, phonemes, self)
        # insert spaces
        string = re.sub('^' + BLANK + '+', '', string)
        string = re.sub(BLANK + '+$', '', string)
        phonemes = phonemes[1:-1]
        Rewrite(SPACE, (Impurity(' '),))(string, phonemes)
        # flatten
        phonemes = reduce(list.__add__, map(list, filter(None, phonemes)), [])
        return phonemes

    def normalize(self, string):
        """Before transcribing, normalizes the string. You could specify the
        different normalization for the language with overriding this method.
        """
        return string

    def hangulize(self, string):
        """Hangulizes the string.

            >>> from hangulize.langs.ja import Japanese
            >>> ja = Japanese()
            >>> ja.hangulize(u'あかちゃん')
            아카찬
        """
        def stringify(syllable):
            if isinstance(syllable[0], Impurity):
                return syllable[0].letter
            else:
                return join(syllable)
        string = self.normalize(string)
        self._log(">> '%s'" % string)
        phonemes = self.transcribe(string)
        try:
            syllables = complete_syllables(phonemes)
            result = [stringify(syl) for syl in syllables]
            hangulized = ''.join(result)
        except TypeError:
            hangulized = u''
        self._log('=> %s' % hangulized)
        return hangulized

    def _log(self, msg, if_=True):
        if if_ and self.logger:
            self.logger.info(msg)
        return msg


class Rewrite(object):

    VOWELS_PATTERN = re.compile('@')
    VARIABLE_PATTERN = re.compile('<(?P<name>[a-zA-Z_][a-zA-Z0-9_]*)>')
    LEFT_EDGE_PATTERN = re.compile(r'^(\^?)\^')
    RIGHT_EDGE_PATTERN = re.compile(r'\$(\$?)$')
    LOOKBEHIND_PATTERN = re.compile('^(?P<edge>(?:\^(?:\^)?)?){([^}]+?)}')
    LOOKAHEAD_PATTERN = re.compile('{([^}]+?)}(?P<edge>(?:\$(?:\$)?)?)$')

    def __init__(self, pattern, val):
        """Makes a replace function with the given pattern and value."""
        self.pattern, self.val = pattern, val

    def __call__(self, string, phonemes=None, lang=None):
        repl = self.val

        # allocate needed offsets
        try:
            phonemes_len, string_len = len(phonemes), len(string)
            if phonemes_len < string_len:
                phonemes += [None] * (string_len - phonemes_len)
        except TypeError:
            pass

        if lang:
            if self.val and not isinstance(self.val, tuple):
                # variable replacement
                srcvars = list(self.find_actual_variables(self.pattern))
                dstvars = list(self.find_actual_variables(self.val))
                if len(srcvars) == len(dstvars) == 1:
                    src = getattr(lang, srcvars[0].group('name'))
                    dst = getattr(lang, dstvars[0].group('name'))
                    if len(src) != len(dst):
                        raise ValueError('the destination variable should '
                                         'have the same length with the '
                                         'source variable')
                    dictionary = dict(zip(src, dst))
                    def repl(match):
                        let = dictionary[match.group(0)]
                        return self.VARIABLE_PATTERN.sub(let, self.val)

        regex = re.compile(type(self).regexify(self.pattern, lang))

        if phonemes and isinstance(self.val, tuple):
            # toss phonemes, and check the matched string
            repl = DONE
            for match in regex.finditer(string):
                start, end = match.span()
                phonemes[start] = self.val
                repl = DONE * (end - start)
        elif not self.val:
            # when val is None, the matched string should remove
            repl = ''

        # replace the string
        prev = string
        string = regex.sub(repl, string)

        # report changes
        if prev != string:
            readable = string.replace(DONE, '.')
            readable = re.sub('^' + BLANK + '|' + BLANK + '$', '', readable)
            readable = re.sub(BLANK, ' ', readable)
            try:
                lang._log(".. '%s' ~ %s => %s ~ /%s/" % \
                          (readable, self.pattern, self.val, regex.pattern))
            except UnicodeError:
                lang._log(".. '%s' ! %s ~ /%s/" % \
                          (readable, self.pattern, regex.pattern))
            except AttributeError:
                pass

        return string

    @classmethod
    def regexify(cls, pattern, lang=None):
        regex = pattern
        if lang:
            regex = cls.regexify_variable(regex, lang)
        regex = cls.regexify_look_around(regex)
        regex = cls.regexify_edge_of_word(regex)
        return regex

    @classmethod
    def regexify_edge_of_word(cls, regex):
        left_edge = r'(?<=\1%s)' % BLANK
        right_edge = r'(?=%s\1)' % BLANK
        regex = cls.LEFT_EDGE_PATTERN.sub(left_edge, regex)
        regex = cls.RIGHT_EDGE_PATTERN.sub(right_edge, regex)
        return regex

    @classmethod
    def regexify_look_around(cls, regex):
        def lookbehind(match):
            edge = re.sub('\^$', BLANK, match.group('edge'))
            return r'(?<=' + edge + r'(?:' + match.group(2) + '))'
        def lookahead(match):
            edge = re.sub('^\$', BLANK, match.group('edge'))
            return r'(?=(?:' + match.group(1) + ')' + edge + ')'
        regex = cls.LOOKBEHIND_PATTERN.sub(lookbehind, regex)
        regex = cls.LOOKAHEAD_PATTERN.sub(lookahead, regex)
        return regex

    @classmethod
    def regexify_variable(cls, regex, lang):
        def to_variable(match):
            var = getattr(lang, match.group('name'))
            return '(%s)' % '|'.join(re.escape(x) for x in var)
        regex = cls.VOWELS_PATTERN.sub('<vowels>', regex)
        regex = cls.VARIABLE_PATTERN.sub(to_variable, regex)
        return regex

    def find_actual_variables(self, pattern):
        def dummy(match):
            return u'\uffff' * (match.end() - match.start())
        try:
            pattern = self.LOOKBEHIND_PATTERN.sub(dummy, pattern)
            pattern = self.LOOKAHEAD_PATTERN.sub(dummy, pattern)
            pattern = self.VOWELS_PATTERN.sub('<>', pattern)
            return self.VARIABLE_PATTERN.finditer(pattern)
        except TypeError:
            return ()


def normalize_roman(string):
    """Removes diacritics from the string and converts to lowercase.

        >>> normalize_roman(u'E\xe8\xe9') # Eèé
        u'eee'
    """
    return ''.join((c for c in unicodedata.normalize('NFD', string) \
                      if unicodedata.category(c) != 'Mn')).lower()


def complete_syllable(syllable):
    """Inserts the default jungseong or jongseong if it is not exists.

        >>> complete_syllable((Jungseong(YO),))
        (u'\u315b', u'\u3161', u'')
        >>> print join(_)
        요
    """
    syllable = list(syllable)
    components = [type(ph) for ph in syllable]
    if Choseong not in components:
        syllable.insert(0, Choseong(NG))
    if Jungseong not in components:
        syllable.insert(1, Jungseong(EU))
    if Jongseong not in components:
        syllable.insert(2, Jungseong(Null))
    return tuple((ph.letter for ph in syllable))


def complete_syllables(phonemes):
    """Separates each syllables and completes every syllable."""
    components, syllable = [Choseong, Jungseong, Jongseong], []
    if phonemes:
        for ph in phonemes:
            comp = type(ph)
            new_syllable = comp is Impurity or syllable and \
                           components.index(comp) <= \
                           components.index(type(syllable[-1]))
            if new_syllable:
                if syllable:
                    yield complete_syllable(syllable)
                    syllable = []
                if comp is Impurity:
                    yield (ph,)
                    continue
            syllable.append(ph)
        if syllable:
            yield complete_syllable(syllable)


def split_phonemes(word):
    """Returns the splitted phonemes from the word.

        >>> split_phonemes(u'안녕') #doctest: +NORMALIZE_WHITESPACE
        (<Choseong 'ㅇ'>, <Jungseong 'ㅏ'>, <Jongseong 'ㄴ'>,
         <Choseong 'ㄴ'>, <Jungseong 'ㅕ'>, <Jongseong 'ㅇ'>)
    """
    result = []
    for c in word:
        c = split(c)
        result.append(Choseong(c[0]))
        result.append(Jungseong(c[1]))
        if c[2] is not Null:
            result.append(Jongseong(c[2]))
    return tuple(result)


def join_phonemes(phonemes):
    """Returns the word from the splitted phonemes.

        >>> print join_phonemes((Jungseong(A), Jongseong(N),
        ...                      Choseong(N), Jungseong(YEO), Jongseong(NG)))
        안녕
    """
    syllables = complete_syllables(phonemes)
    chars = (join(syl) for syl in syllables)
    return reduce(unicode.__add__, chars)


def hangulize(string, locale='it', lang=None, logger=None):
    """Hangulizes the string with the given locale or lang.

        >>> print hangulize(u'gloria', 'it')
        글로리아

    :param string: the loanword
    :param locale: the locale code. if ``lang`` is not given, it is required
    :param lang: the :class:`Language` instance
    :param logger: if the logger instance is given, reports result by each
                   steps
    """
    if not lang:
        try:
            module = __import__('%s.langs.%s' % (__name__, locale))
            lang = getattr(getattr(module.langs, locale), locale)(logger)
        except ImportError:
            raise LanguageError('%s is not supported' % locale)
    return lang.hangulize(string)


class LanguageError(Exception):

    pass

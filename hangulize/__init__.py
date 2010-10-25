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


encoding = getattr(sys.stdout, 'encoding', 'utf-8')


class Phoneme(object):
    """This abstract class wraps a Hangul letter."""

    def __init__(self, letter):
        self.letter = letter

    def __repr__(self):
        return "<%s '%s'>" % (type(self).__name__,
                              self.letter.encode(encoding))


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

    def __init__(self, *rule):
        self.rule = list(rule)

    def items(self, left_edge=False, right_edge=False, lang=None):
        """Yields each notation rules as regex."""
        for one in self.rule:
            pattern = one[0]
            # accept *args
            if len(one) == 2:
                val = one[1]
                if isinstance(val, Phoneme):
                    val = val,
            # accept args(a tuple instance)
            else:
                val = one[1:]
            # when pattern and val has only one variable
            svars = list(self._find_actual_variables(pattern))
            dvars = list(self._find_actual_variables(val))
            if lang and len(svars) is len(dvars) is 1:
                src = getattr(lang, svars[0].group('name'))
                dst = getattr(lang, dvars[0].group('name'))
                if len(src) is not len(dst):
                    raise SyntaxError('destination variable should have the '
                                      'same length with source variable')
                for s, d in zip(src, dst):
                    srange, drange = svars[0].span(), dvars[0].span()
                    p = pattern[:srange[0]] + s + pattern[srange[1]:]
                    v = val[:drange[0]] + d + val[drange[1]:]
                    regex = self.regexify(p, left_edge, right_edge, lang)
                    if regex:
                        yield regex, v
            else:
                regex = self.regexify(pattern, left_edge, right_edge, lang)
                if regex:
                    yield regex, val

    @property
    def chars(self):
        """The humane characters from the notation keys."""
        chest = []
        for one in self.rule:
            pattern = self.VARIABLE_PATTERN.sub('', one[0])
            pattern = re.sub(r'[\{\}\@\[\]\^\$]', '', pattern)
            for c in pattern:
                chest.append(c)
        return set(chest)

    def regexify(self, pattern, left_edge=False, right_edge=False, lang=None):
        """Compiles a regular expression from the notation pattern."""
        regex = pattern
        # edge of string
        if self.LEFTEDGE_PATTERN.search(regex):
            if left_edge:
                regex = self.LEFTEDGE_PATTERN.sub(r'^', regex)
            else:
                return
        if self.RIGHTEDGE_PATTERN.search(regex):
            if right_edge:
                regex = self.RIGHTEDGE_PATTERN.sub(r'$', regex)
            else:
                return
        if left_edge:
            regex = self.LOOKBEHIND_PATTERN.sub(r'(?<=\1(?:\2))', regex)
        # look around
        regex = self.LOOKBEHIND_PATTERN.sub(r'(?<=\1(?:\2))', regex)
        regex = self.LOOKAHEAD_PATTERN.sub(r'(?=(?:\1)\2)', regex)
        if lang:
            def to_variable(match):
                var = getattr(lang, match.group('name'))
                return '|'.join(re.escape(l) for l in var)
            regex = re.sub('@', '<vowels>', regex)
            regex = self.VARIABLE_PATTERN.sub(to_variable, regex)
        return re.compile(regex)

    def _find_actual_variables(self, code):
        def dummy(match):
            return u'\uffff' * (match.end() - match.start())
        try:
            code = self.LOOKBEHIND_PATTERN.sub(dummy, code)
            code = self.LOOKAHEAD_PATTERN.sub(dummy, code)
            code = re.sub('@', '<vowels>', code)
            return self.VARIABLE_PATTERN.finditer(code)
        except TypeError:
            return ()


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
        words = self.split(string)
        last = len(words) - 1
        notation = self.notation
        result = []
        for i, word in enumerate(words):
            length = len(word)
            phonemes = [None] * length
            # check edge
            left_edge = not i
            right_edge = i == last
            for pattern, val in notation.items(left_edge, right_edge, self):
                if isinstance(val, tuple):
                    repl = ' '
                    for match in pattern.finditer(word):
                        start, end = match.span()
                        phonemes[start] = val
                        repl = ' ' * (end - start)
                    val = repl
                elif not val:
                    val = ''
                prev_word, prev_length = word, length
                word = pattern.sub(val, word)
                length = len(word)
                if length > prev_length:
                    phonemes += [None] * (length - prev_length)
                self._log(".. '%s' /%s/" % (word, pattern.pattern),
                          if_=word != prev_word)
            if phonemes:
                if result:
                    result.append((Impurity(' '),))
                result += phonemes
        return filter(None, result)

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
        phonemes = map(list, self.transcribe(string))
        syllables = complete_syllables(reduce(list.__add__, phonemes))
        result = [stringify(syl) for syl in syllables]
        hangulized = ''.join(result)
        self._log('=> %s' % hangulized)
        return hangulized

    def _log(self, msg, if_=True):
        if if_ and self.logger:
            self.logger.info(msg)
        return msg


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
            new_syllable = syllable and (comp is Impurity or \
                                         components.index(comp) <= \
                                         components.index(type(syllable[-1])))
            if new_syllable:
                yield complete_syllable(syllable)
                syllable = []
                # yield impurity
                if comp is Impurity:
                    yield (ph,)
                    continue
            syllable.append(ph)
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
        module = __import__('%s.langs.%s' % (__name__, locale))
        lang = getattr(getattr(module.langs, locale), locale)(logger=logger)
    return lang.hangulize(string)


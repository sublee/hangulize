# -*- coding: utf-8 -*-
import sys
import re
import functools
from hangulize.hangul import *


SPACE = '_' # u'\U000f0000'
EDGE = chr(3)
SPECIAL = chr(27) #u'\U000f0000'
BLANK = '(?:%s|%s|%s)' % tuple(map(re.escape, (SPACE, EDGE, SPECIAL)))
DONE = chr(0) #u'\U000fffff'
ENCODING = getattr(sys.stdout, 'encoding', 'utf-8')


def cached_property(func, name=None):
    if name is None:
        name = func.__name__
    def get(self):
        try:
            return self.__dict__[name]
        except KeyError:
            val = func(self)
            self.__dict__[name] = val
            return val
    functools.update_wrapper(get, func)
    def del_(self):
        self.__dict__.pop(name, None)
    return property(get, None, del_)


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

    def __init__(self, rules):
        self.rules = rules

    def __iter__(self):
        if not getattr(self, '_rewrites', None):
            self._rewrites = [Rewrite(*item) for item in self.items()]
        return iter(self._rewrites)

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
            pattern = Rewrite.VARIABLE_PATTERN.sub('', one[0])
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

    def __new__(cls):
        if not getattr(cls, '_instances', None):
            cls._instances = {}
        if cls not in cls._instances:
            cls._instances[cls] = object.__new__(cls)
        return cls._instances[cls]

    def __init__(self):
        if not isinstance(self.notation, Notation):
            raise NotImplementedError("notation has to be defined")

    @cached_property
    def _steal_specials(self):
        # keep special characters
        def keep(match, rewrite):
            self._specials.append(match.group(0))
            return SPECIAL
        esc = '(%s)' % '|'.join(re.escape(x) for x in self.special)
        return Rewrite(esc, keep)

    @cached_property
    def _recover_specials(self):
        # escape special characters
        def escape(match, rewrite):
            return (Impurity(self._specials.pop(0)),)
        return Rewrite(SPECIAL, escape)

    @property
    def chars_pattern(self):
        """The regex pattern which is matched the valid characters."""
        return ''.join(re.escape(c) for c in self.notation.chars)

    def split(self, string):
        """Splits words from the string. Each words have only valid characters.
        """
        pattern = '[^%s]+' % self.chars_pattern
        return re.split(pattern, string)

    def transcribe(self, string, logger=None):
        """Returns :class:`Phoneme` instance list from the word."""
        string = re.sub(r'\s+', SPACE, string)
        string = re.sub(r'^|$', EDGE, string)
        self._specials = []
        phonemes = []

        # steal special characters
        string = self._steal_specials(string, phonemes)
        # apply the notation
        for rewrite in self.notation:
            string = rewrite(string, phonemes, lang=self, logger=logger)
        # recover special characters
        string = self._recover_specials(string, phonemes)

        # insert spaces
        string = re.sub('^' + BLANK + '+', '', string)
        string = re.sub(BLANK + '+$', '', string)
        phonemes = phonemes[1:-1]
        _hold_spaces(string, phonemes)

        # flatten
        phonemes = reduce(list.__add__, map(list, filter(None, phonemes)), [])
        return phonemes

    def normalize(self, string):
        """Before transcribing, normalizes the string. You could specify the
        different normalization for the language with overriding this method.
        """
        return string

    def hangulize(self, string, logger=None):
        """Hangulizes the string.

            >>> from hangulize.langs.ja import Japanese
            >>> ja = Japanese()
            >>> ja.hangulize(u'あかちゃん')
            아카찬
        """
        from hangulize.processing import complete_syllables
        def stringify(syllable):
            if isinstance(syllable[0], Impurity):
                return syllable[0].letter
            else:
                return join(syllable)
        string = self.normalize(string)
        logger and logger.info(">> '%s'" % string)
        phonemes = self.transcribe(string, logger=logger)
        try:
            syllables = complete_syllables(phonemes)
            result = [stringify(syl) for syl in syllables]
            hangulized = ''.join(result)
        except TypeError:
            hangulized = u''
        logger and logger.info('=> %s' % hangulized)
        return hangulized

    @property
    def iso639_1(self):
        return self.__iso639__.get(1)

    @property
    def iso639_2(self):
        return self.__iso639__.get(2)

    @property
    def iso639_3(self):
        return self.__iso639__.get(3)

    @property
    def code(self):
        return re.sub('^hangulize\.langs\.', '', type(self).__module__)


class Rewrite(object):

    VOWELS_PATTERN = re.compile('@')
    VARIABLE_PATTERN = re.compile('<(?P<name>[a-zA-Z_][a-zA-Z0-9_]*)>')
    LEFT_EDGE_PATTERN = re.compile(r'^(\^?)\^')
    RIGHT_EDGE_PATTERN = re.compile(r'\$(\$?)$')
    LOOKBEHIND_PATTERN = re.compile('^(?P<edge>(?:\^(?:\^)?)?){([^}]+?)}')
    LOOKAHEAD_PATTERN = re.compile('{([^}]+?)}(?P<edge>(?:\$(?:\$)?)?)$')
    def NEGATIVE(regex):
        pattern = regex.pattern.replace('{', '\[').replace('}', '\]')
        return re.compile(pattern)
    NEGATIVE_LOOKBEHIND_PATTERN = NEGATIVE(LOOKBEHIND_PATTERN)
    NEGATIVE_LOOKAHEAD_PATTERN = NEGATIVE(LOOKAHEAD_PATTERN)
    del NEGATIVE

    def __init__(self, pattern, val):
        """Makes a replace function with the given pattern and value."""
        self.pattern, self.val = pattern, val
        self.__regexes__ = {}

    def __call__(self, string, phonemes=None, lang=None, logger=None):
        # allocate needed offsets
        try:
            phonemes_len, string_len = len(phonemes), len(string)
            if phonemes_len < string_len:
                phonemes += [None] * (string_len - phonemes_len)
        except TypeError:
            pass

        regex = self.compile_pattern(lang)

        # replacement function
        def repl(match):
            val = self.val(match, self) if callable(self.val) else self.val
            repls.append(val)

            if val:
                is_tuple = isinstance(val, tuple)
                if not is_tuple:
                    if lang:
                        # variable replacement
                        srcvars = self.find_actual_variables(self.pattern)
                        dstvars = self.find_actual_variables(self.val)
                        srcvars, dstvars = list(srcvars), list(dstvars)
                        if len(srcvars) == len(dstvars) == 1:
                            src = getattr(lang, srcvars[0].group('name'))
                            dst = getattr(lang, dstvars[0].group('name'))
                            if len(src) != len(dst):
                                msg = 'the destination variable should ' \
                                      'have the same length with the ' \
                                      'source variable'
                                raise ValueError(msg)
                            dictionary = dict(zip(src, dst))
                            let = dictionary[match.group(0)]
                            val = self.VARIABLE_PATTERN.sub(let, val)
                    return val
                elif phonemes and is_tuple:
                    # toss phonemes, and check the matched string
                    start, end = match.span()
                    phonemes[start] = val
                    return DONE * (end - start)
            elif not val:
                # when val is None, the matched string should remove
                return ''

        repls = []
        prev = string
        # replace the string
        string = regex.sub(repl, string)

        if logger:
            # report changes
            def readably(string):
                string = string.replace(DONE, '.')
                string = string.replace(SPECIAL, '#')
                string = re.sub('^' + BLANK + '|' + BLANK + '$', '', string)
                string = re.sub(BLANK, ' ', string)
                return string
            if prev != string:
                readable = readably(string)
                val = repls.pop()
                args = (readable, self.pattern)
                if not val:
                    msg = ".. '%s'\tremove %s" % args
                elif isinstance(val, tuple):
                    val = ''.join(x.letter for x in val)
                    msg = ".. '%s'\thangulize %s -> %s" % (args + (val,))
                else:
                    msg = ".. '%s'\trewrite %s -> %s" % (args + (val,))
                logger.info(msg)

        return string

    def compile_pattern(self, lang=None):
        if lang not in self.__regexes__:
            regex = re.compile(type(self).regexify(self.pattern, lang))
            self.__regexes__[lang] = regex
        return self.__regexes__[lang]

    @classmethod
    def regexify(cls, pattern, lang=None):
        regex = pattern
        if lang:
            regex = cls.regexify_variable(regex, lang)
        regex = cls.regexify_lookaround(regex)
        regex = cls.regexify_negative_lookaround(regex)
        regex = cls.regexify_edge_of_word(regex)
        return regex

    @classmethod
    def regexify_edge_of_word(cls, regex):
        left_edge = r'(?<=\1%s)' % BLANK
        right_edge = r'(?=%s\1)' % BLANK
        regex = cls.LEFT_EDGE_PATTERN.sub(left_edge, regex)
        regex = cls.RIGHT_EDGE_PATTERN.sub(right_edge, regex)
        return regex

    def make_lookaround(behind_pattern, ahead_pattern,
                        behind_prefix, ahead_prefix):
        @classmethod
        def meth(cls, regex):
            def lookbehind(match):
                edge = re.sub('\^$', BLANK, match.group('edge'))
                return '(?' + behind_prefix + edge + \
                       '(?:' + match.group(2) + '))'
            def lookahead(match):
                edge = re.sub('^\$', BLANK, match.group('edge'))
                return '(?' + ahead_prefix + \
                       '(?:' + match.group(1) + ')' + edge + ')'
            regex = behind_pattern.sub(lookbehind, regex)
            regex = ahead_pattern.sub(lookahead, regex)
            return regex
        return meth
    regexify_lookaround = make_lookaround(LOOKBEHIND_PATTERN,
                                          LOOKAHEAD_PATTERN,
                                          '<=', '=')
    regexify_negative_lookaround = make_lookaround(NEGATIVE_LOOKBEHIND_PATTERN,
                                                   NEGATIVE_LOOKAHEAD_PATTERN,
                                                   '<!', '!')
    del make_lookaround

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


_hold_spaces = Rewrite(SPACE, (Impurity(' '),))


class HangulizeError(Exception):

    pass


class LanguageError(HangulizeError):

    pass


class InvalidCodeError(HangulizeError):

    pass

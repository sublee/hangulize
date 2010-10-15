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


encoding = sys.stdout.encoding


class Phoneme(object):

    def __init__(self, letter):
        self.letter = letter

    def __repr__(self):
        return "<%s '%s'>" % (type(self).__name__,
                              self.letter.encode(encoding))


class Choseong(Phoneme):
    pass

class Jungseong(Phoneme):
    pass

class Jongseong(Phoneme):
    pass

class Impurity(Phoneme):
    pass


class Notation(object):

    def __init__(self, *rule):
        self.rule = list(rule)

    def items(self, lang=None):
        """Yields each notation rules as regex."""
        for pattern, val in self.rule:
            yield self.regexify(pattern, lang), val

    @property
    def chars(self):
        chest = []
        for pattern, _ in self.rule:
            pattern = re.sub(r'[\{\}\@\[\]\^\$]', '', pattern)
            for c in pattern:
                chest.append(c)
        return set(chest)

    def regexify(self, pattern, lang=None):
        """Compiles a regular expression from the notation pattern."""
        regex = pattern
        if lang:
            vowels = ''.join([re.escape(v) for v in lang.vowels])
            regex = re.sub('@', vowels, regex)
        regex = re.sub('^{([^}]+?)}', r'(?<=[\1])', regex)
        regex = re.sub('{([^}]+?)}$', r'(?=[\1])', regex)
        return re.compile(regex)


class Language(object):

    vowels = ()
    notation = None

    def __init__(self, logger=None):
        if not isinstance(self.notation, Notation):
            raise NotImplementedError("notation has to be defined")
        self.logger = logger

    def get_phonemes(self, word):
        length = len(word)
        phonemes = [None] * length
        for pattern, val in self.notation.items(self):
            if isinstance(val, tuple):
                for match in pattern.finditer(word):
                    start, end = match.span()
                    phonemes[start] = val
                    del phonemes[start + 1:end]
                val = ' '
            elif not val:
                val = ''
            prev_word, prev_length = word, length
            word = pattern.sub(val, word)
            length = len(word)
            if length > prev_length:
                phonemes += [None] * (length - prev_length)
            if self.logger and word != prev_word:
                self.logger.info("-> '%s'" % word)
        return filter(bool, phonemes)

    @property
    def chars_pattern(self):
        return ''.join(re.escape(c) for c in self.notation.chars)

    def split(self, string):
        pattern = '[^%s]+' % self.chars_pattern
        return re.split(pattern, string)

    def syllables(self, word):
        components, syllable = [Choseong, Jungseong, Jongseong, Impurity], []
        phonemes = list(self.get_phonemes(word))
        if phonemes:
            phonemes = reduce(list.__add__, map(list, phonemes))
            for ph in phonemes:
                comp = type(ph)
                new_syllable = syllable and components.index(comp) <= \
                               components.index(type(syllable[-1]))
                if new_syllable:
                    yield complete_syllable(syllable)
                    syllable = []
                if comp is not Choseong and not syllable:
                    syllable.append(Choseong(NG))
                if comp is not Jungseong and len(syllable) is 1:
                    syllable.append(Jungseong(EU))
                syllable.append(ph)
            yield complete_syllable(syllable)

    def normalize(self, string):
        return string

    def hangulize(self, string):
        def stringify(syllable):
            if isinstance(syllable[0], Impurity):
                return syllable[0].letter
            else:
                return join(syllable)
        string = self.normalize(string)
        if self.logger:
            self.logger.info("-> '%s'" % string)
        hangulized = []
        for word in self.split(string):
            syllables = [stringify(syl) for syl in self.syllables(word)]
            if not syllables:
                continue
            hangulized.append(reduce(unicode.__add__, syllables))
        return ' '.join(hangulized)


def phonemes(word):
    result = []
    for c in word:
        c = split(c)
        result.append(Choseong(c[0]))
        result.append(Jungseong(c[1]))
        if c[2] is not Null:
            result.append(Jongseong(c[2]))
    return tuple(result)


def normalize_roman(string):
    """Removes diacritics from the string and converts to lowercase.

        >>> normalize_roman(u'E\xe8\xe9') # Eèé
        u'eee'
    """
    return ''.join((c for c in unicodedata.normalize('NFD', string) \
                      if unicodedata.category(c) != 'Mn')).lower()


def complete_syllable(syllable):
    if len(syllable) is not 3:
        if len(syllable) is 1:
            syllable.append(Jungseong(EU))
        syllable.append(Jongseong(Null))
    return tuple((ph.letter for ph in syllable))


def hangulize(string, locale='it', lang=None, logger=None):
    if not lang:
        module = __import__('%s.langs.%s' % (__name__, locale))
        lang = getattr(getattr(module.langs, locale), locale)(logger=logger)
    return lang.hangulize(string)


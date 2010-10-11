# -*- coding: utf-8 -*-
"""
hangulize
~~~~~~~~~

Korean Alphabet Transcription.
"""
import unicodedata
from .hangul import join, EU, NG, Null
from .phoneme import Choseong, Jungseong, Jongseong


class Loanword(object):

    def __init__(self, word, notation):
        self.word = normalize_roman(word)
        self.notation = notation

    def get_phonemes(self, word):
        length = len(word)
        phonemes = [None] * length
        for pattern, val in self.notation.items():
            if isinstance(val, tuple):
                for match in pattern.finditer(word):
                    start, end = match.span()
                    phonemes[start] = val
                    del phonemes[start + 1:end]
                val = ' '
            elif not val:
                val = ''
            prev_length = length
            _ = word
            word = pattern.sub(val, word)
            length = len(word)
            if length > prev_length:
                phonemes += [None] * (length - prev_length)
            # verbose
            # if word != _:
            #    print word
        return filter(bool, phonemes)

    def syllables(self, word):
        components, syllable = (Choseong, Jungseong, Jongseong), []
        phonemes = list(self.get_phonemes(word))
        if phonemes:
            phonemes = reduce(list.__add__, map(list, phonemes))
            for ph in phonemes:
                comp = type(ph)
                new_syllable = bool(syllable and \
                                    components.index(comp) <= \
                                    components.index(type(syllable[-1])))
                if new_syllable:
                    yield complete_syllable(syllable)
                    syllable = []
                if comp is not Choseong and not syllable:
                    syllable.append(Choseong(NG))
                if comp is not Jungseong and len(syllable) is 1:
                    syllable.append(Jungseong(EU))
                syllable.append(ph)
            yield complete_syllable(syllable)

    def hangulize(self):
        syllables = [join(syllable) for syllable in self.syllables(self.word)]
        if not syllables:
            raise ValueError('cannot hangulize')
        return reduce(unicode.__add__, syllables)


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


def hangulize(word, locale='en_us', notation=None):
    """Transcribe.

        >>> print hangulize(u'gloria').encode('utf-8')
        글로리아
        >>> print hangulize(u'Innocenti', locale='it').encode('utf-8')
        인노첸티
        >>> print hangulize(u'Cerigotto', locale='it').encode('utf-8')
        체리고토
        >>> print hangulize(u'Juventus', locale='it').encode('utf-8')
        유벤투스
        >>> print hangulize(u'Schiavonia', locale='it').encode('utf-8')
        스키아보니아
        >>> print hangulize(u'Fogli', locale='it').encode('utf-8')
        폴리
    """
    if not notation:
        module = __import__('%s.notations.%s' % (__name__, locale))
        notation = getattr(getattr(module.notations, locale), locale)()
    return Loanword(word, notation).hangulize()



# -*- coding: utf-8 -*-
import unicodedata
from .phoneme import Choseong, Jungseong, Jongseong, EU, Null


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


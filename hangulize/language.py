import re
from .utils import complete_syllable
from .notation import Notation
from .phoneme import *


class Language(object):

    vowels = ()
    notation = None

    def __init__(self):
        if not isinstance(self.notation, Notation):
            raise NotImplementedError("notation has to be defined")

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
            # _ = word
            prev_length = length
            word = pattern.sub(val, word)
            length = len(word)
            if length > prev_length:
                phonemes += [None] * (length - prev_length)
            # verbose
            # if word != _:
            #    print word
        return filter(bool, phonemes)

    def syllables(self, word):
        components, syllable = (Choseong, Jungseong, Jongseong, Impurity), []
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
        hangulized = []
        for word in re.split(r'\s+', string):
            syllables = [stringify(syl) for syl in self.syllables(word)]
            if not syllables:
                raise ValueError('cannot hangulize')
            hangulized.append(reduce(unicode.__add__, syllables))
        # print ' '.join(hangulized)
        return ' '.join(hangulized)


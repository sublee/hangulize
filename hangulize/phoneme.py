from .hangul import *


class Phoneme(object):

    def __init__(self, letter):
        self.letter = letter

    def __repr__(self):
        return "<%s '%s'>" % (type(self).__name__, self.letter.encode('utf-8'))


class Choseong(Phoneme):
    pass

class Jungseong(Phoneme):
    pass

class Jongseong(Phoneme):
    pass

class Impurity(Phoneme):
    pass


def phonemes(word):
    result = []
    for c in word:
        c = split(c)
        result.append(Choseong(c[0]))
        result.append(Jungseong(c[1]))
        if c[2] is not Null:
            result.append(Jongseong(c[2]))
    return tuple(result)


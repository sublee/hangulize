# -*- coding: utf-8 -*-
import unicodedata


def normalize_roman(string, additional=None):
    """Removes diacritics from the string and converts to lowercase.

        >>> normalize_roman(u'E\xe8\xe9') # Eèé
        u'eee'
    """
    if additional:
        safe = additional.keys() + additional.values()
        def gen():
            for c in string:
                if c not in safe:
                    yield normalize_roman(c)
                elif c in additional:
                    yield additional[c]
                else:
                    yield c
        return ''.join(gen())
    else:
        chars = []
        for c in string:
            if unicodedata.category(c) == 'Lo':
                chars.append(c)
            else:
                nor = unicodedata.normalize('NFD', c)
                chars.extend(x for x in nor if unicodedata.category(x) != 'Mn')
        return ''.join(chars).lower()

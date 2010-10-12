# -*- coding: utf-8 -*-
"""
hangulize
~~~~~~~~~

Korean Alphabet Transcription.
"""
from .hangul import join, EU, NG, Null
from .phoneme import Choseong, Jungseong, Jongseong


def hangulize(word, locale='it', lang=None):
    if not lang:
        module = __import__('%s.langs.%s' % (__name__, locale))
        lang = getattr(getattr(module.langs, locale), locale)()
    return lang.hangulize(word)


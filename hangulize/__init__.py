# -*- coding: utf-8 -*-
"""
hangulize
~~~~~~~~~

Korean Alphabet Transcription.
"""
import sys
import re
from hangulize.processing import *
from hangulize.normalization import *


def import_module(code):
    """Imports a module from the given code."""
    submods = code.split('.')
    module = __import__('%s.langs.%s' % (__name__, code)).langs
    for submod in submods:
        module = getattr(module, submod)
    return module


def get_lang(code, logger=None):
    """Returns a language instance from the given code."""
    return import_module(code).__lang__(logger)


def supported(code):
    """Checks if hangulize supports the given language.

        >>> supported('ita')
        True
        >>> supported('kat.narrow')
        True
        >>> supported('kor')
        False
    """
    try:
        import_module(code)
        return True
    except ImportError:
        return False


def hangulize(string, code=None, lang=None, logger=None):
    """Hangulizes the string with the given language code or lang.

        >>> print hangulize(u'gloria', 'ita')
        글로리아

    :param string: the loanword
    :param code: the language code as ISO 639-3. if ``lang`` is not given,
                 it is required
    :param lang: the :class:`Language` instance
    :param logger: if the logger instance is given, reports result by each
                   steps
    """
    if not lang:
        try:
            lang = get_lang(code, logger=logger)
        except ImportError:
            raise LanguageError('%s is not supported' % code)
    return lang.hangulize(string)

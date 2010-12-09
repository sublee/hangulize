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


def hangulize(string, code=None, iso639=None, lang=None, logger=None):
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
        lang = get_lang(code, iso639=iso639, logger=logger)
    return lang.hangulize(string)


def import_module(code):
    """Imports a module from the given code."""
    submods = code.split('.')
    module = __import__('%s.langs.%s' % (__name__, code)).langs
    for submod in submods:
        module = getattr(module, submod)
    return module


def get_lang(code, iso639=None, logger=None):
    """Returns a language instance from the given code."""
    def make_lang(code, submods, logger):
        try:
            code = '.'.join([code] + list(submods))
            return import_module(code).__lang__(logger)
        except ImportError:
            raise LanguageError('%s is not supported' % code)
    # split module path
    if '.' in code:
        code = code.split('.')
        submods = code[1:]
        code = code[0]
    else:
        submods = ()
    # guess if ISO 639-1 or 639-3
    if not iso639:
        if len(code) == 2:
            iso639 = 1
        elif len(code) == 3:
            iso639 = 3
    try:
        # fix the warning when importing pycountry
        import logging
        if not getattr(logging, 'NullHandler', None):
            class NullHandler(logging.Handler):
                def emit(self, record):
                    pass
        logging.getLogger('pycountry.db').addHandler(NullHandler())
        from pycountry import languages
        attr = ['alpha2', 'bibliographic', 'terminology'][iso639 - 1]
        code = languages.get(**{attr: code}).terminology
    except TypeError:
        # out of 2~3 characters
        raise InvalidCodeError('%s is invalid language code' % code)
    except KeyError:
        try:
            return make_lang(code, submods, logger)
        except LanguageError:
            raise InvalidCodeError('%s is invalid ISO 639-%d code' % \
                                   (code, iso639))
    except ImportError:
        if iso639 != 3:
            raise ImportError('pycountry is required '
                              'to use ISO 639-%d' % iso639)
    return make_lang(code, submods, logger)


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

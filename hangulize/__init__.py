# -*- coding: utf-8 -*-
"""
    hangulize
    ~~~~~~~~~

    Korean Alphabet Transcription.

    :copyright: (c) 2010-2016 by Heungsub Lee
    :license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import, unicode_literals
import importlib


__version__ = '0.0.8'
__all__ = [b'hangulize', b'get_lang', b'supports']


def hangulize(string, code=None, iso639=None, lang=None, logger=None):
    """Transcribes a loanword to Hangul.

        >>> print hangulize(u'gloria', 'ita')
        글로리아

    :param string: an loan word
    :param code: a language code as ISO 639-3. if ``lang`` is not given,
                 it is required
    :param lang: a :class:`Language` instance
    :param logger: if the logger instance is given, reports result by each
                   steps
    """
    if not lang:
        lang = get_lang(code, iso639=iso639)
    return lang.hangulize(string, logger=logger)


def get_lang(code, iso639=None):
    """Returns a language instance from the given code."""
    code_head = code.split('.', 1)[0]
    if len(code_head) < 2 or len(code_head) > 3:
        raise ValueError('%r is an invalid language code' % code)
    def make_lang(code, submods):
        try:
            code = '.'.join([code] + list(submods))
            return import_lang_module(code).__lang__()
        except ImportError:
            raise ValueError('Hangulize does not support %s' % code)
    # split module path
    if '.' in code:
        code = code.split('.')
        submods = code[1:]
        code = code[0]
    else:
        submods = ()
    # guess if ISO 639-1 or 639-3
    if iso639 is None:
        if len(code) == 2:
            iso639 = 1
        elif len(code) == 3:
            iso639 = 3
    try:
        # fix the warning when importing pycountry
        import logging
        from pycountry import languages
        if not getattr(logging, 'NullHandler', None):
            class NullHandler(logging.Handler):
                def emit(self, record):
                    pass
            logging.NullHandler = NullHandler
        logging.getLogger('pycountry.db').addHandler(logging.NullHandler())
        attr = ['alpha2', 'bibliographic', 'terminology'][iso639 - 1]
        code = languages.get(**{attr: code}).terminology
    except TypeError:
        # out of 2~3 characters
        raise ValueError('%r is an invalid language code' % code)
    except KeyError:
        try:
            return make_lang(code, submods)
        except ValueError:
            raise ValueError('{0!r} is an invalid ISO 639-{1} code'
                             ''.format(code, iso639))
    except ImportError:
        if iso639 != 3:
            raise ImportError('ISO 639-%d requires pycountry' % iso639)
    return make_lang(code, submods)


def import_lang_module(code):
    """Imports a module from the given code."""
    submods = code.split('.')
    module = __import__('%s.langs.%s' % (__name__, code)).langs
    for submod in submods:
        module = getattr(module, submod)
    return module


def supports(code):
    """Checks if hangulize supports the given language.

        >>> supports('ita')
        True
        >>> supports('kat.narrow')
        True
        >>> supports('kor')
        False
    """
    try:
        import_lang_module(code)
        return True
    except ImportError:
        return False


def supported(code):
    """Deprecated with 0.0.6. Use :func:`hangulize.supports` instead."""
    import warnings
    warnings.warn('supported() has been deprecated, use supports() instead',
                  DeprecationWarning)
    return supports(code)


# include all submodules.
for name in ['.models', '.normalization', '.processing']:
    module = importlib.import_module(name, __name__)
    __all__.extend(module.__all__)
    for attr in module.__all__:
        locals()[attr] = getattr(module, attr)

# -*- coding: utf-8 -*-
import os
import sys
import unittest

import hangulize

from cmds.helper import color


class LazyTestSuite(unittest.TestSuite):

    def __init__(self, tests=()):
        self._tests = tests


class HangulizeTestCase(unittest.TestCase):

    def runTest(self):
        pass

    def assert_examples(self, examples, lang=None, logger=None):
        cls = type(self)
        # store examples
        if getattr(cls, '_store_examples', False):
            cls._stored_examples.update(examples)
            return
        errors = []
        lang = lang or self.lang
        if isinstance(lang, basestring):
            lang = hangulize.get_lang(lang)
        try:
            lang_name = type(lang).__name__
        except AttributeError:
            lang_name = 'AnonymouseLanguage'
        for word, want in examples.items():
            try:
                got = lang.hangulize(word, logger=logger)
                assert want == got
            except self.failureException:
                errors.append((word, want, got))
        if errors:
            def form(error):
                return " * '%s' should be '%s', but '%s' was given" % (
                    color(error[0], 'cyan'),
                    color(error[1], 'green'),
                    color(error[2], 'red')
                )
            errors = map(form, errors)
            msg = color(lang_name, 'yellow') + '\n' + '\n'.join(errors)
            raise HangulizeAssertionError(msg.encode('utf-8'))

    @classmethod
    def get_examples(cls, method_name=None):
        cls._store_examples = True
        cls._stored_examples = {}
        self = cls()
        if method_name:
            method_names = [method_name]
        else:
            method_names = [x for x in dir(cls) if x.startswith('test')]
        for method_name in method_names:
            getattr(cls, method_name)(self)
        examples = cls._stored_examples
        del cls._store_examples, cls._stored_examples
        return examples

    def _exc_info(self):
        info = sys.exc_info()
        return info[:2] + (None,)


class HangulizeAssertionError(HangulizeTestCase.failureException):

    pass


def filename(path):
    return os.path.sep.join(os.path.basename(path).split(os.path.extsep)[:-1])


def suite(lang=None):
    loader = unittest.TestLoader()
    if lang:
        mods = [lang.replace('.', '_')]
    else:
        mods = (filename(x) for x in os.listdir(os.path.dirname(__file__)) \
                            if x.endswith(os.path.extsep + 'py') and \
                               '__init__' not in x)
    def tests():
        for mod in mods:
            mod = getattr(__import__('%s.%s' % (__name__, mod)), mod)
            yield loader.loadTestsFromModule(mod)
            del mod
    suite = LazyTestSuite(tests())
    return suite


suite_for_setup = suite(os.environ.get('HANGULIZE_TEST_LANG'))

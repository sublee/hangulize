# -*- coding: utf-8 -*-
import sys
import os.path
import time
import unittest
from cmds.repl import color


class LazyTestSuite(unittest.TestSuite):

    def __init__(self, tests=()):
        self._tests = tests


class HangulizeTestCase(unittest.TestCase):

    def tearDown(self):
        time.sleep(0.1)

    def runTest(self):
        pass

    def assert_examples(self, examples):
        cls = type(self)
        if getattr(cls, '_capture_examples', False):
            cls._captured_examples = examples
            del cls._capture_examples
            return
        for word, want in examples.items():
            try:
                got = self.lang.hangulize(word)
                assert want == got
            except self.failureException as e:
                msg = 'in %s notation, %s should be transcribed to %s, ' \
                      'but %s was given' % (color(self.lang_name, 'yellow'),
                                            color(word, 'cyan'),
                                            color(want, 'green'),
                                            color(got, 'red'))
                raise HangulizeAssertionError(msg.encode('utf-8'))

    @classmethod
    def get_examples(cls, method_name):
        cls._capture_examples = True
        getattr(cls, method_name)(cls())
        examples = cls._captured_examples
        del cls._captured_examples
        return examples

    def __init__(self, *args, **kwargs):
        super(HangulizeTestCase, self).__init__(*args, **kwargs)
        try:
            self.lang_name = type(self.lang).__name__
        except AttributeError:
            pass

    def _exc_info(self):
        info = sys.exc_info()
        return info[:2] + (None,)


class HangulizeAssertionError(HangulizeTestCase.failureException):

    pass


def filename(path):
    return os.path.sep.join(os.path.basename(path).split(os.path.extsep)[:-1])


def suite(code=None):
    loader = unittest.TestLoader()
    if code:
        mods = [code.replace('.', '_')]
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

import sys
import os.path
import unittest
import time


class LazyTestSuite(unittest.TestSuite):

    def __init__(self, tests=()):
        self._tests = tests


class HangulizeTestCase(unittest.TestCase):

    def hangulize(self, word):
        return self.lang.hangulize(word)

    def tearDown(self):
        time.sleep(0.1)


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
    def add_tests():
        for mod in mods:
            mod = getattr(__import__('%s.%s' % (__name__, mod)), mod)
            yield loader.loadTestsFromModule(mod)
            del mod
    suite = LazyTestSuite(add_tests())
    return suite

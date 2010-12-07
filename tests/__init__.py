import sys
import os.path
import unittest


class HangulizeTestCase(unittest.TestCase):

    def hangulize(self, word):
        return self.lang.hangulize(word)


def filename(path):
    return os.path.sep.join(os.path.basename(path).split(os.path.extsep)[:-1])


def suite(code=None):
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    if code:
        mods = [code.replace('.', '_')]
    else:
        mods = (filename(x) for x in os.listdir(os.path.dirname(__file__)) \
                            if x.endswith('.py') and '__init__' not in x)
    for mod in mods:
        mod = getattr(__import__('%s.%s' % (__name__, mod)), mod)
        suite.addTest(loader.loadTestsFromModule(mod))
    return suite

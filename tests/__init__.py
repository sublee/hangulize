import os.path
import unittest


class HangulizeTestCase(unittest.TestCase):

    def hangulize(self, word):
        return self.lang.hangulize(word)


def filename(path):
    return os.path.sep.join(os.path.basename(path).split(os.path.extsep)[:-1])


def suite():
    #from internal import *
    suite = unittest.TestSuite()
    curdir = os.path.dirname(__file__)
    mods = (filename(x) for x in os.listdir(curdir) \
                        if x.endswith('.py') and '__init__' not in x)
    for mod in mods:
        mod = getattr(__import__('%s.%s' % (__name__, mod)), mod)
        for test_case in (x for x in dir(mod) if x.endswith('TestCase')):
            test_case = getattr(mod, test_case)
            suite.addTest(unittest.makeSuite(test_case))
    #suite.addTest(unittest.makeSuite(PatternTestCase))
    #suite.addTest(unittest.makeSuite(AlgorithmTestCase))
    return suite

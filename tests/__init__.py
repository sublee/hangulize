import os.path
import unittest


class HangulizeTestCase(unittest.TestCase):

    def hangulize(self, word):
        return self.lang.hangulize(word)


def suite():
    from internal import *
    suite = unittest.TestSuite()
    curdir = os.path.dirname(__file__)
    codes = (x for x in os.listdir(curdir) \
             if os.path.isdir(os.path.join(cursir, x)))
    suite.addTest(unittest.makeSuite(PatternTestCase))
    suite.addTest(unittest.makeSuite(AlgorithmTestCase))
    return suite

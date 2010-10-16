import unittest


class HangulizeTestCase(unittest.TestCase):

    def hangulize(self, word):
        return self.lang.hangulize(word)


def suite():
    from internal import *
    from it import ItalianTestCase
    from ja import JapaneseTestCase
    from es import SpanishTestCase
    from pl import PolishTestCase
    from cs import CzechTestCase
    from sh import SerboCroatianTestCase
    from ro import RomanianTestCase
    from hu import HungarianTestCase
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(APITestCase))
    suite.addTest(unittest.makeSuite(AlgorithmTestCase))
    suite.addTest(unittest.makeSuite(ItalianTestCase))
    suite.addTest(unittest.makeSuite(JapaneseTestCase))
    suite.addTest(unittest.makeSuite(SpanishTestCase))
    suite.addTest(unittest.makeSuite(PolishTestCase))
    suite.addTest(unittest.makeSuite(CzechTestCase))
    suite.addTest(unittest.makeSuite(SerboCroatianTestCase))
    suite.addTest(unittest.makeSuite(RomanianTestCase))
    suite.addTest(unittest.makeSuite(HungarianTestCase))
    return suite


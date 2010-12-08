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
    from vi import VietnameseTestCase
    from sv import SwedishTestCase
    from nl import DutchTestCase
    from de import GermanTestCase
    from pt import PortugueseTestCase
    from ptbr import BrazilianPortugueseTestCase
    from ru import RussianTestCase
    from cy import WelshTestCase
    from wlm import MiddleWelshTestCase
    from bg import BulgarianTestCase
    from ell import ModernGreekTestCase
    from grc import AncientGreekTestCase
    from ka1 import Georgian1TestCase
    from ka2 import Georgian2TestCase
    from la import LatinTestCase
    from isl import IcelandicTestCase
    from fi import FinnishTestCase
    from et import EstonianTestCase
    from lv import LatvianTestCase
    from lt import LithuanianTestCase
    from ca import CatalanTestCase
    from sk import SlovakTestCase
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(APITestCase))
    suite.addTest(unittest.makeSuite(PatternTestCase))
    suite.addTest(unittest.makeSuite(AlgorithmTestCase))
    suite.addTest(unittest.makeSuite(ItalianTestCase))
    suite.addTest(unittest.makeSuite(JapaneseTestCase))
    suite.addTest(unittest.makeSuite(SpanishTestCase))
    suite.addTest(unittest.makeSuite(PolishTestCase))
    suite.addTest(unittest.makeSuite(CzechTestCase))
    suite.addTest(unittest.makeSuite(SerboCroatianTestCase))
    suite.addTest(unittest.makeSuite(RomanianTestCase))
    suite.addTest(unittest.makeSuite(HungarianTestCase))
    suite.addTest(unittest.makeSuite(VietnameseTestCase))
    suite.addTest(unittest.makeSuite(SwedishTestCase))
    suite.addTest(unittest.makeSuite(DutchTestCase))
    suite.addTest(unittest.makeSuite(GermanTestCase))
    suite.addTest(unittest.makeSuite(PortugueseTestCase))
    suite.addTest(unittest.makeSuite(BrazilianPortugueseTestCase))
    suite.addTest(unittest.makeSuite(RussianTestCase))
    suite.addTest(unittest.makeSuite(WelshTestCase))
    suite.addTest(unittest.makeSuite(MiddleWelshTestCase))
    suite.addTest(unittest.makeSuite(BulgarianTestCase))
    suite.addTest(unittest.makeSuite(ModernGreekTestCase))
    suite.addTest(unittest.makeSuite(AncientGreekTestCase))
    suite.addTest(unittest.makeSuite(Georgian1TestCase))
    suite.addTest(unittest.makeSuite(Georgian2TestCase))
    suite.addTest(unittest.makeSuite(LatinTestCase))
    suite.addTest(unittest.makeSuite(IcelandicTestCase))
    suite.addTest(unittest.makeSuite(FinnishTestCase))
    suite.addTest(unittest.makeSuite(EstonianTestCase))
    suite.addTest(unittest.makeSuite(LatvianTestCase))
    suite.addTest(unittest.makeSuite(LithuanianTestCase))
    suite.addTest(unittest.makeSuite(CatalanTestCase))
    suite.addTest(unittest.makeSuite(SlovakTestCase))
    return suite

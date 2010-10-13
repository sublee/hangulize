import unittest


class HangulizeTestCase(unittest.TestCase):

    def hangulize(self, word):
        return self.lang.hangulize(word)


def suite():
    from api import *
    from it import ItalianTestCase
    from ja import JapaneseTestCase
    from es import SpanishTestCase
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LanguagesTestCase))
    suite.addTest(unittest.makeSuite(ItalianTestCase))
    suite.addTest(unittest.makeSuite(JapaneseTestCase))
    suite.addTest(unittest.makeSuite(SpanishTestCase))
    return suite


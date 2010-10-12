# -*- coding: utf-8 -*-
import unittest
from hangulize.langs.it import Italian


class HangulizeTestCase(unittest.TestCase):

    def hangulize(self, word):
        return self.lang.hangulize(word)


class ItalianTestCase(HangulizeTestCase):

    def setUp(self):
        self.lang = Italian()

    def test_hangulize(self):
        assert u'이탈리아' == self.hangulize(u'italia')
        assert u'인노첸티' == self.hangulize(u'Innocenti')
        assert u'체리고토' == self.hangulize(u'Cerigotto')
        assert u'유벤투스' == self.hangulize(u'Juventus')
        assert u'스키아보니아' == self.hangulize(u'Schiavonia')
        assert u'폴리' == self.hangulize(u'Fogli')
        assert u'카라바조' == self.hangulize(u'Caravaggio')
        assert u'네포스' == self.hangulize(u'nephos')
        assert u'스보차키셰' == self.hangulize(u'sbozzacchisce')
        assert u'스칼렌게' == self.hangulize(u'Scalenghe')
        assert u'파브리치오' == self.hangulize(u'Fabrizio')
        assert u'안기아리' == self.hangulize(u'Anghiari')
        assert u'소콰드로' == self.hangulize(u'soqquadro')
        assert u'볼로냐' == self.hangulize(u'Bologna')
        assert u'포니니' == self.hangulize(u'Fognini')
        assert u'이냐치오' == self.hangulize(u'Ignazio')
        assert u'지로 디탈리아' == self.hangulize(u"Giro d'Italia")


if __name__ == "__main__":
    unittest.main()


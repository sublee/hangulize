# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.epo import Esperanto


class EsperantoTestCase(HangulizeTestCase):

    lang = Esperanto()

    def test_examples_in_wikipedia(self):
        """ http://ko.wikipedia.org/wiki/에스페란토 """
        assert u'수페르시그노' == self.hangulize(u'Supersigno')
        assert u'차펠로' == self.hangulize(u'Ĉapelo')
        assert u'살루톤' == self.hangulize(u'Saluton')
        assert u'지스 레비도' == self.hangulize(u'Ĝis revido')
        assert u'아디아우' == self.hangulize(u'Adiaŭ')
        assert u'예스' == self.hangulize(u'Jes')
        assert u'네' == self.hangulize(u'Ne')
        assert u'단콘' == self.hangulize(u'Dankon')
        assert u'미 트레 조야스 렌콘티 빈' == \
               self.hangulize(u'Mi tre ĝojas renkonti vin')
        assert u'추 비 파르타스 보네' == self.hangulize(u'Ĉu vi fartas bone')
        assert u'미 에스타스 코레오' == self.hangulize(u'Mi estas koreo')
        assert u'이치스모' == self.hangulize(u'iĉismo')
        assert u'리이스모' == self.hangulize(u'riismo')
        assert u'링그베 우니베르살라' == self.hangulize(u'lingve universala')
        assert u'라 에스페란티스토' == self.hangulize(u'La Esperantisto')

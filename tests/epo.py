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
        assert u'린그베 우니베르살라' == self.hangulize(u'lingve universala')
        assert u'라 에스페란티스토' == self.hangulize(u'La Esperantisto')

    def test_examples_of_iceager(self):
        assert u'파스포르타 세르보' == self.hangulize(u'Pasporta Servo')
        assert u'폰토' == self.hangulize(u'Fonto')
        assert u'에스페란투요' == self.hangulize(u'Esperantujo')
        assert u'리테라투라 포이로' == self.hangulize(u'Literatura Foiro')
        assert u'라 에스페로' == self.hangulize(u'La Espero')
        assert u'핀벤키스모' == self.hangulize(u'Finvenkismo')
        assert u'라우미스모' == self.hangulize(u'Raŭmismo')
        assert u'치비타니스모' == self.hangulize(u'Civitanismo')
        assert u'우누아 리브로' == self.hangulize(u'Unua Libro')
        assert u'두아 리브로' == self.hangulize(u'Dua Libro')
        assert u'린그보 인테르나치아' == self.hangulize(u'Lingvo Internacia')
        assert u'푼다멘토 데 에스페란토' == \
               self.hangulize(u'Fundamento de Esperanto')
        assert u'라 온도 데 에스페란토' == \
               self.hangulize(u'La Ondo de Esperanto')
        assert u'라 테아트라 모바도 둠 라 밀리토' == \
               self.hangulize(u'La Teatra Movado dum la Milito')
        assert u'고고 카이 리아이 아미코이' == \
               self.hangulize(u'Gogo kaj liaj amikoj')
        assert u'세리오 오리엔토옥치덴토' == \
               self.hangulize(u'Serio Oriento-Okcidento')
        assert u'추 비 프레타스?' == self.hangulize(u'Ĉu vi pretas?')

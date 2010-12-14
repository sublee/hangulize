# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.epo import Esperanto


class EsperantoTestCase(HangulizeTestCase):

    lang = Esperanto()

    def test_examples_in_wikipedia(self):
        """ http://ko.wikipedia.org/wiki/에스페란토 """
        self.assert_examples({
            u'Supersigno': u'수페르시그노',
            u'Ĉapelo': u'차펠로',
            u'Saluton': u'살루톤',
            u'Ĝis revido': u'지스 레비도',
            u'Adiaŭ': u'아디아우',
            u'Jes': u'예스',
            u'Ne': u'네',
            u'Dankon': u'단콘',
            u'Mi tre ĝojas renkonti vin': u'미 트레 조야스 렌콘티 빈',
            u'Ĉu vi fartas bone': u'추 비 파르타스 보네',
            u'Mi estas koreo': u'미 에스타스 코레오',
            u'iĉismo': u'이치스모',
            u'riismo': u'리이스모',
            u'lingve universala': u'린그베 우니베르살라',
            u'La Esperantisto': u'라 에스페란티스토',
        })

    def test_examples_of_iceager(self):
        self.assert_examples({
            u'Pasporta Servo': u'파스포르타 세르보',
            u'Fonto': u'폰토',
            u'Esperantujo': u'에스페란투요',
            u'Literatura Foiro': u'리테라투라 포이로',
            u'La Espero': u'라 에스페로',
            u'Finvenkismo': u'핀벤키스모',
            u'Raŭmismo': u'라우미스모',
            u'Civitanismo': u'치비타니스모',
            u'Unua Libro': u'우누아 리브로',
            u'Dua Libro': u'두아 리브로',
            u'Lingvo Internacia': u'린그보 인테르나치아',
            u'Fundamento de Esperanto': u'푼다멘토 데 에스페란토',
            u'La Ondo de Esperanto': u'라 온도 데 에스페란토',
            u'La Teatra Movado dum la Milito': u'라 테아트라 모바도 둠 라 밀리토',
            u'Gogo kaj liaj amikoj': u'고고 카이 리아이 아미코이',
            u'Serio Oriento-Okcidento': u'세리오 오리엔토옥치덴토',
            u'Ĉu vi pretas?': u'추 비 프레타스?',
        })
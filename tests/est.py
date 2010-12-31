# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.est import Estonian


class EstonianTestCase(HangulizeTestCase):

    lang = Estonian()

    def test_people(self):
        self.assert_examples({
            u'Andrus Ansip': u'안드루스 안시프',
            u'Jakob Hurt': u'야코브 후르트',
            u'Maarja-Liis Ilus': u'마리아리스 일루스',
            u'Ernst Jaakson': u'에른스트 약손',
            u'Carl Robert Jakobson': u'카를 로베르트 야콥손',
            u'Siim Kallas': u'심 칼라스',
            u'Kaia Kanepi': u'카이아 카네피',
            u'Gerd Kanter': u'게르드 칸테르',
            u'Jaan Kaplinski': u'얀 카플린스키',
            u'Paul Keres': u'파울 케레스',
            u'Jaan Kirsipuu': u'얀 키르시푸',
            u'Lydia Koidula': u'뤼디아 코이둘라',
            u'Jaan Kross': u'얀 크로스',
            u'Kerli Kõiv': u'케를리 커이브',
            u'Mart Laar': u'마르트 라르',
            u'Lennart Meri': u'렌나르트 메리',
            u'Markko Märtin': u'마르코 매르틴',
            u'Georg Ots': u'게오르그 오츠',
            u'Juhan Parts': u'유한 파르츠',
            u'Indrek Pertelson': u'인드레크 페르텔손',
            u'Arvo Pärt': u'아르보 패르트',
            u'Konstantin Päts': u'콘스탄틴 패츠',
            u'Johannes Pääsuke': u'요한네스 패수케',
            u'Kristjan Raud': u'크리스티안 라우드',
            u'Arnold Rüütel': u'아르놀드 뤼텔',
            u'Gustav Suits': u'구스타브 수이츠',
            u'Kristina Šmigun': u'크리스티나 슈미군',
            u'Anton Hansen Tammsaare': u'안톤 한센 탐사레',
            u'Rudolf Tobias': u'루돌프 토비아스',
            u'Villu Toots': u'빌루 토츠',
            u'Veljo Tormis': u'벨리오 토르미스',
            u'Jüri Uluots': u'위리 울루오츠',
            u'Andrus Veerpalu': u'안드루스 베르팔루',
            u'Veiko Õunpuu': u'베이코 어운푸',
        })

    def test_places(self):
        self.assert_examples({
            u'Haapsalu': u'합살루',
            u'Kohtla-Järve': u'코흐틀라얘르베',
            u'Koiva': u'코이바',
            u'Kuressaare': u'쿠레사레',
            u'Narva': u'나르바',
            u'Paide': u'파이데',
            u'Pärnu': u'패르누',
            u'Rakvere': u'라크베레',
            u'Tallinn': u'탈린',
            u'Tartu': u'타르투',
            u'Toompea': u'톰페아',
            u'Valga': u'발가',
            u'Viljandi': u'빌리안디',
            u'Võru': u'버루',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            u'Kalevipoeg': u'칼레비포에그',
            u'kannel': u'칸넬',
        })

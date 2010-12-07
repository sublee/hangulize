# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.et import Estonian


class EstonianTestCase(HangulizeTestCase):

    lang = Estonian()

    def test_people(self):
        assert u'안드루스 안시프' == self.hangulize(u'Andrus Ansip')
        assert u'야코브 후르트' == self.hangulize(u'Jakob Hurt')
        assert u'마리아리스 일루스' == self.hangulize(u'Maarja-Liis Ilus ')
        assert u'에른스트 약손' == self.hangulize(u'Ernst Jaakson')
        assert u'카를 로베르트 야콥손' == \
               self.hangulize(u'Carl Robert Jakobson')
        assert u'심 칼라스' == self.hangulize(u'Siim Kallas')
        assert u'카이아 카네피' == self.hangulize(u'Kaia Kanepi')
        assert u'게르드 칸테르' == self.hangulize(u'Gerd Kanter')
        assert u'얀 카플린스키' == self.hangulize(u'Jaan Kaplinski')
        assert u'파울 케레스' == self.hangulize(u'Paul Keres')
        assert u'얀 키르시푸' == self.hangulize(u'Jaan Kirsipuu')
        assert u'뤼디아 코이둘라' == self.hangulize(u'Lydia Koidula')
        assert u'얀 크로스' == self.hangulize(u'Jaan Kross')
        assert u'케를리 커이브' == self.hangulize(u'Kerli Kõiv')
        assert u'마르트 라르' == self.hangulize(u'Mart Laar')
        assert u'렌나르트 메리' == self.hangulize(u'Lennart Meri')
        assert u'마르코 매르틴' == self.hangulize(u'Markko Märtin')
        assert u'게오르그 오츠' == self.hangulize(u'Georg Ots')
        assert u'유한 파르츠' == self.hangulize(u'Juhan Parts')
        assert u'인드레크 페르텔손' == self.hangulize(u'Indrek Pertelson')
        assert u'아르보 패르트' == self.hangulize(u'Arvo Pärt')
        assert u'콘스탄틴 패츠' == self.hangulize(u'Konstantin Päts')
        assert u'요한네스 패수케' == self.hangulize(u'Johannes Pääsuke')
        assert u'크리스티안 라우드' == self.hangulize(u'Kristjan Raud')
        assert u'아르놀드 뤼텔' == self.hangulize(u'Arnold Rüütel')
        assert u'구스타브 수이츠' == self.hangulize(u'Gustav Suits')
        assert u'크리스티나 슈미군' == self.hangulize(u'Kristina Šmigun')
        assert u'안톤 한센 탐사레' == self.hangulize(u'Anton Hansen Tammsaare')
        assert u'루돌프 토비아스' == self.hangulize(u'Rudolf Tobias')
        assert u'빌루 토츠' == self.hangulize(u'Villu Toots')
        assert u'벨리오 토르미스' == self.hangulize(u'Veljo Tormis')
        assert u'위리 울루오츠' == self.hangulize(u'Jüri Uluots')
        assert u'안드루스 베르팔루' == self.hangulize(u'Andrus Veerpalu')
        assert u'베이코 어운푸' == self.hangulize(u'Veiko Õunpuu')

    def test_places(self):
        assert u'합살루' == self.hangulize(u'Haapsalu')
        assert u'코흐틀라얘르베' == self.hangulize(u'Kohtla-Järve')
        assert u'코이바' == self.hangulize(u'Koiva')
        assert u'쿠레사레' == self.hangulize(u'Kuressaare')
        assert u'나르바' == self.hangulize(u'Narva')
        assert u'파이데' == self.hangulize(u'Paide')
        assert u'패르누' == self.hangulize(u'Pärnu')
        assert u'라크베레' == self.hangulize(u'Rakvere')
        assert u'탈린' == self.hangulize(u'Tallinn')
        assert u'타르투' == self.hangulize(u'Tartu')
        assert u'톰페아' == self.hangulize(u'Toompea')
        assert u'발가' == self.hangulize(u'Valga')
        assert u'빌리안디' == self.hangulize(u'Viljandi')
        assert u'버루' == self.hangulize(u'Võru')

    def test_miscellaneous(self):
        assert u'칼레비포에그' == self.hangulize(u'Kalevipoeg')
        assert u'칸넬' == self.hangulize(u'kannel')

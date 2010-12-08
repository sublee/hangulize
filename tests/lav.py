# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.lav import Latvian


class LatvianTestCase(HangulizeTestCase):

    lang = Latvian()

    def test_people(self):
        assert u'알베르츠' == self.hangulize(u'Alberts')
        assert u'구나르스 아스트라' == self.hangulize(u'Gunārs Astra')
        assert u'헬무츠 발데리스' == self.hangulize(u'Helmuts Balderis')
        assert u'야니스 발로디스' == self.hangulize(u'Jānis Balodis')
        assert u'크리샤니스 바론스' == self.hangulize(u'Krišjānis Barons')
        assert u'미하일스 바리슈니코우스' == \
               self.hangulize(u'Mihails Barišņikovs')
        assert u'비즈마 벨셰비차' == self.hangulize(u'Vizma Belševica')
        assert u'에두아르츠 베르클라우스' == self.hangulize(u'Eduards Berklavs')
        assert u'에르네스츠 블랑크스' == self.hangulize(u'Ernests Blanks')
        assert u'루돌프스 블라우마니스' == self.hangulize(u'Rūdolfs Blaumanis')
        assert u'알렉산드르스 착스' == self.hangulize(u'Aleksandrs Čaks')
        assert u'야니스 착스테' == self.hangulize(u'Jānis Čakste')
        assert u'에밀스 다르진슈' == self.hangulize(u'Emīls Dārziņš')
        assert u'엘리아스 엘리에제르스 데슬레르스' == \
               self.hangulize(u'Eliass Eliezers Desslers')
        assert u'세르게이스 에이젠슈테인스' == \
               self.hangulize(u'Sergejs Eizenšteins')
        assert u'모우샤 페이긴스' == self.hangulize(u'Movša Feigins')
        assert u'엘리나 가란차' == self.hangulize(u'Elīna Garanča')
        assert u'에르네스츠 굴비스' == self.hangulize(u'Ernests Gulbis')
        assert u'우비스 헬마니스' == self.hangulize(u'Uvis Helmanis')
        assert u'아르투르스 이르베' == self.hangulize(u'Artūrs Irbe')
        assert u'카를리스 이르비티스' == self.hangulize(u'Kārlis Irbītis')
        assert u'가티스 야호비치' == self.hangulize(u'Gatis Jahovičs')
        assert u'카스파르스 캄발라' == self.hangulize(u'Kaspars Kambala')
        assert u'알렉산드르스 코블렌츠' == \
               self.hangulize(u'Aleksandrs Koblencs')
        assert u'구스타우스 클루치스' == self.hangulize(u'Gustavs Klucis')
        assert u'아브람스 이작스 쿡스' == self.hangulize(u'Ābrams Izāks Kūks')
        assert u'알렉산드르스 코발레우스키스' == \
               self.hangulize(u'Aleksandrs Kovaļevskis')
        assert u'미첼리스 크로그젬스' == self.hangulize(u'Miķelis Krogzems')
        assert u'유리스 크론베르크스' == self.hangulize(u'Juris Kronbergs')
        assert u'아티스 크론발츠' == self.hangulize(u'Atis Kronvalds')
        assert u'알베르츠 크비에시스' == self.hangulize(u'Alberts Kviesis')
        assert u'알렉산드르스 라이메' == self.hangulize(u'Aleksandrs Laime')
        assert u'니콜라이스 로스키스' == self.hangulize(u'Nikolajs Loskis')
        assert u'예우게니야 리시치나' == self.hangulize(u'Jevgēnija Ļisicina')
        assert u'직프리츠 안나 메이에로비츠' == \
               self.hangulize(u'Zigfrīds Anna Meierovics')
        assert u'에우게니스 밀레르스' == self.hangulize(u'Evgenijs Millers')
        assert u'카를리스 밀렌바흐스' == self.hangulize(u'Kārlis Mīlenbahs')
        assert u'스타니슬라우스 올리야르스' == \
               self.hangulize(u'Stanislavs Olijars')
        assert u'엘비라 오졸리냐' == self.hangulize(u'Elvīra Ozoliņa')
        assert u'빌헬름스 오스트발츠' == self.hangulize(u'Vilhelms Ostvalds')
        assert u'산디스 오졸린슈' == self.hangulize(u'Sandis Ozoliņš')
        assert u'발데마르스 오졸린슈' == self.hangulize(u'Valdemārs Ozoliņš')
        assert u'아르티스 파브릭스' == self.hangulize(u'Artis Pabriks')
        assert u'카를리스 파덱스' == self.hangulize(u'Karlis Padegs')
        assert u'마리안 파하르스' == self.hangulize(u'Marian Pahars')
        assert u'블라디미르스 페트로우스' == \
               self.hangulize(u'Vladimirs Petrovs')
        assert u'안드레이스 품푸르스' == self.hangulize(u'Andrejs Pumpurs')
        assert u'마르틴슈 루베니스' == self.hangulize(u'Mārtiņš Rubenis')
        assert u'유리스 루베니스' == self.hangulize(u'Juris Rubenis')
        assert u'엘자 로젠베르가' == self.hangulize(u'Elza Rozenberga')
        assert u'울랴나 세묘노바' == self.hangulize(u'Uļjana Semjonova')
        assert u'마리스 슈트롬베르크스' == self.hangulize(u'Māris Štrombergs')
        assert u'페테리스 스투치카' == self.hangulize(u'Pēteris Stučka')
        assert u'빅토르스 슈체르바티흐스' == \
               self.hangulize(u'Viktors Ščerbatihs')
        assert u'하랄츠 실로우스' == self.hangulize(u'Haralds Silovs')
        assert u'안드리스 슈첼레' == self.hangulize(u'Andris Šķēle')
        assert u'에르네스츠 슈탈베르크스' == \
               self.hangulize(u'Ernests Štālbergs')
        assert u'군티스 울마니스' == self.hangulize(u'Guntis Ulmanis')
        assert u'카를리스 울마니스' == self.hangulize(u'Kārlis Ulmanis')
        assert u'로만스 바인슈테인스' == self.hangulize(u'Romāns Vainšteins')
        assert u'크리샤니스 발데마르스' == \
               self.hangulize(u'Krišjānis Valdemārs')
        assert u'미첼리스 발테르스' == self.hangulize(u'Miķelis Valters')
        assert u'발디스 발테르스' == self.hangulize(u'Valdis Valters')
        assert u'알렉산드르스 바낙스' == self.hangulize(u'Aleksandrs Vanags')
        assert u'오야르스 바치에티스' == self.hangulize(u'Ojārs Vācietis')
        assert u'에두아르츠 베이덴바움스' == \
               self.hangulize(u'Eduards Veidenbaums')
        assert u'막스 베인레이흐스' == self.hangulize(u'Makss Veinreihs')
        assert u'비스발디스' == self.hangulize(u'Visvaldis')
        assert u'야젭스 비톨스' == self.hangulize(u'Jāzeps Vītols')
        assert u'마리스 베르파코우스키스' == \
               self.hangulize(u'Māris Verpakovskis')
        assert u'알렉산드르스 보이트케비치' == \
               self.hangulize(u'Aleksandrs Voitkevičs')
        assert u'카를리스 자린슈' == self.hangulize(u'Kārlis Zariņš')
        assert u'구스타우스 젬갈스' == self.hangulize(u'Gustavs Zemgals')
        assert u'발디스 자틀레르스' == self.hangulize(u'Valdis Zatlers')
        assert u'이만츠 지에도니스' == self.hangulize(u'Imants Ziedonis')
        assert u'세르게이스 졸톡스' == self.hangulize(u'Sergejs Žoltoks')

    def test_places(self):
        assert u'다우가바' == self.hangulize(u'Daugava')
        assert u'다우가우필스' == self.hangulize(u'Daugavpils')
        assert u'그로비냐' == self.hangulize(u'Grobiņa')
        assert u'예캅필스' == self.hangulize(u'Jēkabpils')
        assert u'옐가바' == self.hangulize(u'Jelgava')
        assert u'예르시카' == self.hangulize(u'Jersika')
        assert u'유르말라' == self.hangulize(u'Jūrmala')
        assert u'코크네세' == self.hangulize(u'Koknese')
        assert u'쿠르제메' == self.hangulize(u'Kurzeme')
        assert u'라트갈레' == self.hangulize(u'Latgale')
        assert u'라트비야' == self.hangulize(u'Latvija')
        assert u'리에파야' == self.hangulize(u'Liepāja')
        assert u'레제크네' == self.hangulize(u'Rēzekne')
        assert u'리가' == self.hangulize(u'Rīga')
        assert u'발미에라' == self.hangulize(u'Valmiera')
        assert u'벤츠필스' == self.hangulize(u'Ventspils')
        assert u'비제메' == self.hangulize(u'Vidzeme')
        assert u'젬갈레' == self.hangulize(u'Zemgale')

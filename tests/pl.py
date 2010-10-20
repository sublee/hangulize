# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class PolishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0208.jsp """

    def setUp(self):
        from hangulize.langs.pl import Polish
        self.lang = Polish()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0106.jsp """
        assert u'부라크' == self.hangulize(u'burak')
        assert u'십코' == self.hangulize(u'szybko')
        assert u'도브제' == self.hangulize(u'dobrze')
        assert u'흘레프' == self.hangulize(u'chleb')
        assert u'첼' == self.hangulize(u'cel')
        assert u'발리츠키' == self.hangulize(u'Balicki')
        assert u'노츠' == self.hangulize(u'noc')
        assert u'다치' == self.hangulize(u'dać')
        assert u'다흐' == self.hangulize(u'dach')
        assert u'즈드로비' == self.hangulize(u'zdrowy')
        assert u'스워트키' == self.hangulize(u'słodki')
        assert u'포트' == self.hangulize(u'pod')
        assert u'파솔라' == self.hangulize(u'fasola')
        assert u'베프슈티크' == self.hangulize(u'befsztyk')
        assert u'구라' == self.hangulize(u'góra')
        assert u'그라트' == self.hangulize(u'grad')
        assert u'타르크' == self.hangulize(u'targ')
        assert u'헤르바타' == self.hangulize(u'herbata')
        assert u'흐루비에슈프' == self.hangulize(u'Hrubieszów')
        assert u'키노' == self.hangulize(u'kino')
        assert u'닥틸' == self.hangulize(u'daktyl')
        assert u'크룰' == self.hangulize(u'król')
        assert u'반크' == self.hangulize(u'bank')
        assert u'리스' == self.hangulize(u'lis')
        assert u'콜라노' == self.hangulize(u'kolano')
        assert u'모틸' == self.hangulize(u'motyl')
        assert u'모스트' == self.hangulize(u'most')
        assert u'짐노' == self.hangulize(u'zimno')
        assert u'삼' == self.hangulize(u'sam')
        assert u'네르카' == self.hangulize(u'nerka')
        assert u'도쿠멘트' == self.hangulize(u'dokument')
        assert u'디반' == self.hangulize(u'dywan')
        assert u'그단스크' == self.hangulize(u'Gdańsk')
        assert u'포즈난' == self.hangulize(u'Poznań')
        assert u'파라' == self.hangulize(u'para')
        assert u'스웁스크' == self.hangulize(u'Słupsk')
        assert u'흐워프' == self.hangulize(u'chłop')
        assert u'로베르' == self.hangulize(u'rower')
        assert u'가르네크' == self.hangulize(u'garnek')
        assert u'슈누르' == self.hangulize(u'sznur')
        assert u'세르체' == self.hangulize(u'serce')
        assert u'스레브로' == self.hangulize(u'srebro')
        assert u'파스' == self.hangulize(u'pas')
        assert u'실레피' == self.hangulize(u'ślepy')
        assert u'지시' == self.hangulize(u'dziś')
        assert u'탐' == self.hangulize(u'tam')
        assert u'마트카' == self.hangulize(u'matka')
        assert u'부트' == self.hangulize(u'but')
        assert u'바르샤바' == self.hangulize(u'Warszawa')
        assert u'피브니차' == self.hangulize(u'piwnica')
        assert u'크레프' == self.hangulize(u'krew')
        assert u'자메크' == self.hangulize(u'zamek')
        assert u'즈브로드니아' == self.hangulize(u'zbrodnia')
        assert u'비부스' == self.hangulize(u'wywóz')
        assert u'그보지지크' == self.hangulize(u'gwoździk')
        assert u'비엥시' == self.hangulize(u'więź')
        assert u'지토' == self.hangulize(u'żyto')
        assert u'루주니' == self.hangulize(u'różny')
        assert u'위슈카' == self.hangulize(u'łyżka')
        assert u'스트라시' == self.hangulize(u'straż')
        assert u'호리' == self.hangulize(u'chory')
        assert u'쿠흐니아' == self.hangulize(u'kuchnia')
        assert u'다흐' == self.hangulize(u'dach')
        assert u'지우라' == self.hangulize(u'dziura')
        assert u'즈본' == self.hangulize(u'dzwon')
        assert u'모시옹츠' == self.hangulize(u'mosiądz')
        assert u'니에치비에치' == self.hangulize(u'niedźwiedź')
        assert u'제보' == self.hangulize(u'drzewo')
        assert u'워치' == self.hangulize(u'łodż')
        assert u'치스티' == self.hangulize(u'czysty')
        assert u'베치카' == self.hangulize(u'beczka')
        assert u'클루치' == self.hangulize(u'klucz')
        assert u'샤리' == self.hangulize(u'szary')
        assert u'무슈타르다' == self.hangulize(u'musztarda')
        assert u'카펠루시' == self.hangulize(u'kapelusz')
        assert u'제카' == self.hangulize(u'rzeka')
        assert u'프셰미실' == self.hangulize(u'Przemyśl')
        assert u'코우니에시' == self.hangulize(u'kołnierz')
        assert u'야스니' == self.hangulize(u'jasny')
        assert u'크라이' == self.hangulize(u'kraj')
        assert u'워노' == self.hangulize(u'łono')
        assert u'그워바' == self.hangulize(u'głowa')
        assert u'부우카' == self.hangulize(u'bułka')
        assert u'카나우' == self.hangulize(u'kanał')
        assert u'트라바' == self.hangulize(u'trawa')
        assert u'트롱바' == self.hangulize(u'trąba')
        assert u'몽카' == self.hangulize(u'mąka')
        assert u'콩트' == self.hangulize(u'kąt')
        assert u'통' == self.hangulize(u'tą')
        assert u'제로' == self.hangulize(u'zero')
        assert u'켕파' == self.hangulize(u'kępa')
        assert u'벵고시' == self.hangulize(u'węgorz')
        assert u'쳉스토호바' == self.hangulize(u'Częstochowa')
        assert u'프로셰' == self.hangulize(u'proszę')
        assert u'지마' == self.hangulize(u'zima')
        assert u'우도' == self.hangulize(u'udo')
        assert u'프루바' == self.hangulize(u'próba')
        assert u'쿨라' == self.hangulize(u'kula')
        assert u'닥틸' == self.hangulize(u'daktyl')

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'자메크' == self.hangulize(u'zamek')
        assert u'모크리' == self.hangulize(u'mokry')
        assert u'스웁스크' == self.hangulize(u'Słupsk')

    def test_2nd(self):
        """제2항: b, d, g
        1. 어말에 올 때에는 '프', '트', '크'로 적는다.
        2. 유성 자음 앞에서는 '브', '드', '그'로 적는다.
        3. 무성 자음 앞에서 b, g는 받침으로 적고, d는 '트'로 적는다.
        """
        assert u'오트' == self.hangulize(u'od')
        assert u'즈브로드니아' == self.hangulize(u'zbrodnia')
        assert u'그랍스키' == self.hangulize(u'Grabski')
        assert u'오트피스' == self.hangulize(u'odpis')

    def test_3rd(self):
        """제3항: w, z, ź, dz, ż, rz, sz
        1. w, z, ź, dz가 무성 자음 앞이나 어말에 올 때에는 '프, 스, 시, 츠'로
           적는다.
        2. ż와 rz는 모음 앞에 올 때에는 'ㅈ'으로 적되, 앞의 자음이 무성
           자음일 때에는 '시'로 적는다. 유성 자음 앞에 올 때에는 '주', 무성
           자음 앞에 올 때에는 '슈', 어말에 올 때에는 '시'로 적는다.
        3. sz는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        assert u'자바프카' == self.hangulize(u'zabawka')
        assert u'오브라스' == self.hangulize(u'obraz')
        assert u'제슈프' == self.hangulize(u'Rzeszów')
        assert u'프셰미실' == self.hangulize(u'Przemyśl')
        assert u'그주모트' == self.hangulize(u'grzmot')
        assert u'우슈코' == self.hangulize(u'łóżko')
        assert u'펭헤시' == self.hangulize(u'pęcherz')
        assert u'코슈트' == self.hangulize(u'koszt')
        assert u'코시' == self.hangulize(u'kosz')

    def test_4th(self):
        """제4항: ł
        1. ł는 뒤따르는 모음과 결합할 때 합쳐서 적는다. (ło는 '워'로 적는다.)
           다만, 자음 뒤에 올 때에는 두 음절로 갈라 적는다.
        2. oł는 '우'로 적는다.
        """
        assert u'워노' == self.hangulize(u'łono')
        assert u'그워바' == self.hangulize(u'głowa')
        assert u'프시야치우' == self.hangulize(u'przyjaciół')

    def test_5th(self):
        """제5항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        assert u'올레이' == self.hangulize(u'olej')

    def test_6th(self):
        """제6항: m
        어두의 m이 l, r 앞에 올 때에는 '으'를 붙여 적는다.
        """
        assert u'믈레코' == self.hangulize(u'mleko')
        assert u'므루프카' == self.hangulize(u'mrówka')

    def test_7th(self):
        """제7항: ę
        ę은 '엥'으로 적는다. 다만, 어말의 ę는 '에'로 적는다.
        """
        assert u'렝카' == self.hangulize(u'ręka')
        assert u'프로셰' == self.hangulize(u'proszę')

    def test_8th(self):
        """제8항
        'ㅈ', 'ㅊ'으로 표기되는 자음(c, z) 뒤의 이중 모음은 단모음으로 적는다.
        """
        assert u'스타차' == self.hangulize(u'stacja')
        assert u'프리제르' == self.hangulize(u'fryzjer')

    def test_etc(self):
        assert u'프시아치우' == self.hangulize(u'przjyaciół')


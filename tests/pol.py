# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.pol import Polish


class PolishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0208.jsp """

    lang = Polish()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0106.jsp """
        self.assert_examples({
            u'burak': u'부라크',
            u'szybko': u'십코',
            u'dobrze': u'도브제',
            u'chleb': u'흘레프',
            u'cel': u'첼',
            u'Balicki': u'발리츠키',
            u'noc': u'노츠',
            u'dać': u'다치',
            u'dach': u'다흐',
            u'zdrowy': u'즈드로비',
            u'słodki': u'스워트키',
            u'pod': u'포트',
            u'fasola': u'파솔라',
            u'befsztyk': u'베프슈티크',
            u'góra': u'구라',
            u'grad': u'그라트',
            u'targ': u'타르크',
            u'herbata': u'헤르바타',
            u'Hrubieszów': u'흐루비에슈프',
            u'kino': u'키노',
            u'daktyl': u'닥틸',
            u'król': u'크룰',
            u'bank': u'반크',
            u'lis': u'리스',
            u'kolano': u'콜라노',
            u'motyl': u'모틸',
            u'most': u'모스트',
            u'zimno': u'짐노',
            u'sam': u'삼',
            u'nerka': u'네르카',
            u'dokument': u'도쿠멘트',
            u'dywan': u'디반',
            u'Gdańsk': u'그단스크',
            u'Poznań': u'포즈난',
            u'para': u'파라',
            u'Słupsk': u'스웁스크',
            u'chłop': u'흐워프',
            u'rower': u'로베르',
            u'garnek': u'가르네크',
            u'sznur': u'슈누르',
            u'serce': u'세르체',
            u'srebro': u'스레브로',
            u'pas': u'파스',
            u'ślepy': u'실레피',
            u'dziś': u'지시',
            u'tam': u'탐',
            u'matka': u'마트카',
            u'but': u'부트',
            u'Warszawa': u'바르샤바',
            u'piwnica': u'피브니차',
            u'krew': u'크레프',
            u'zamek': u'자메크',
            u'zbrodnia': u'즈브로드니아',
            u'wywóz': u'비부스',
            u'gwoździk': u'그보지지크',
            u'więź': u'비엥시',
            u'żyto': u'지토',
            u'różny': u'루주니',
            u'łyżka': u'위슈카',
            u'straż': u'스트라시',
            u'chory': u'호리',
            u'kuchnia': u'쿠흐니아',
            u'dach': u'다흐',
            u'dziura': u'지우라',
            u'dzwon': u'즈본',
            u'mosiądz': u'모시옹츠',
            u'niedźwiedź': u'니에치비에치',
            u'drzewo': u'제보',
            u'łodż': u'워치',
            u'czysty': u'치스티',
            u'beczka': u'베치카',
            u'klucz': u'클루치',
            u'szary': u'샤리',
            u'musztarda': u'무슈타르다',
            u'kapelusz': u'카펠루시',
            u'rzeka': u'제카',
            u'Przemyśl': u'프셰미실',
            u'kołnierz': u'코우니에시',
            u'jasny': u'야스니',
            u'kraj': u'크라이',
            u'łono': u'워노',
            u'głowa': u'그워바',
            u'bułka': u'부우카',
            u'kanał': u'카나우',
            u'trawa': u'트라바',
            u'trąba': u'트롱바',
            u'mąka': u'몽카',
            u'kąt': u'콩트',
            u'tą': u'통',
            u'zero': u'제로',
            u'kępa': u'켕파',
            u'węgorz': u'벵고시',
            u'Częstochowa': u'쳉스토호바',
            u'proszę': u'프로셰',
            u'zima': u'지마',
            u'udo': u'우도',
            u'próba': u'프루바',
            u'kula': u'쿨라',
            u'daktyl': u'닥틸',
        })

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            u'zamek': u'자메크',
            u'mokry': u'모크리',
            u'Słupsk': u'스웁스크',
        })

    def test_2nd(self):
        """제2항: b, d, g
        1. 어말에 올 때에는 '프', '트', '크'로 적는다.
        2. 유성 자음 앞에서는 '브', '드', '그'로 적는다.
        3. 무성 자음 앞에서 b, g는 받침으로 적고, d는 '트'로 적는다.
        """
        self.assert_examples({
            u'od': u'오트',
            u'zbrodnia': u'즈브로드니아',
            u'Grabski': u'그랍스키',
            u'odpis': u'오트피스',
        })

    def test_3rd(self):
        """제3항: w, z, ź, dz, ż, rz, sz
        1. w, z, ź, dz가 무성 자음 앞이나 어말에 올 때에는 '프, 스, 시, 츠'로
           적는다.
        2. ż와 rz는 모음 앞에 올 때에는 'ㅈ'으로 적되, 앞의 자음이 무성
           자음일 때에는 '시'로 적는다. 유성 자음 앞에 올 때에는 '주', 무성
           자음 앞에 올 때에는 '슈', 어말에 올 때에는 '시'로 적는다.
        3. sz는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        self.assert_examples({
            u'zabawka': u'자바프카',
            u'obraz': u'오브라스',
            u'Rzeszów': u'제슈프',
            u'Przemyśl': u'프셰미실',
            u'grzmot': u'그주모트',
            u'łóżko': u'우슈코',
            u'pęcherz': u'펭헤시',
            u'koszt': u'코슈트',
            u'kosz': u'코시',
        })

    def test_4th(self):
        """제4항: ł
        1. ł는 뒤따르는 모음과 결합할 때 합쳐서 적는다. (ło는 '워'로 적는다.)
           다만, 자음 뒤에 올 때에는 두 음절로 갈라 적는다.
        2. oł는 '우'로 적는다.
        """
        self.assert_examples({
            u'łono': u'워노',
            u'głowa': u'그워바',
            u'przyjaciół': u'프시야치우',
        })

    def test_5th(self):
        """제5항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            u'olej': u'올레이',
        })

    def test_6th(self):
        """제6항: m
        어두의 m이 l, r 앞에 올 때에는 '으'를 붙여 적는다.
        """
        self.assert_examples({
            u'mleko': u'믈레코',
            u'mrówka': u'므루프카',
        })

    def test_7th(self):
        """제7항: ę
        ę은 '엥'으로 적는다. 다만, 어말의 ę는 '에'로 적는다.
        """
        self.assert_examples({
            u'ręka': u'렝카',
            u'proszę': u'프로셰',
        })

    def test_8th(self):
        """제8항
        'ㅈ', 'ㅊ'으로 표기되는 자음(c, z) 뒤의 이중 모음은 단모음으로 적는다.
        """
        self.assert_examples({
            u'stacja': u'스타차',
            u'fryzjer': u'프리제르',
        })

    def test_etc(self):
        self.assert_examples({
            u'przjyaciół': u'프시아치우',
        })
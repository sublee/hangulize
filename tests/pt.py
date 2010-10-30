# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class PortugueseTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0219.jsp """

    def setUp(self):
        from hangulize.langs.pt import Portuguese
        self.lang = Portuguese()
    
    def test_1st(self):
        """제1항
        c, g는 a, o, u 앞에서는 각각 ‘ㅋ, ㄱ'으로 적고, e, i 앞에서는
        ‘ㅅ, ㅈ'으로 적는다.
        """
        assert u'카브랄' == self.hangulize(u'Cabral')
        assert u'카모싱' == self.hangulize(u'Camocim')
        assert u'에가스' == self.hangulize(u'Egas')
        assert u'질' == self.hangulize(u'Gil')

    def test_2nd(self):
        """제2항
        gu, qu는 a, o, u 앞에서는 각각 ‘구, 쿠'로 적고, e, i 앞에서는
        ‘ㄱ, ㅋ'으로 적는다.
        """
        assert u'이구아수' == self.hangulize(u'Iguaçú')
        assert u'아라쿠아리' == self.hangulize(u'Araquari')
        assert u'게하' == self.hangulize(u'Guerra')
        assert u'아킬리누' == self.hangulize(u'Aquilino')

    def test_3rd(self):
        """제3항
        d, t는 ㄷ, ㅌ으로 적는다.
        """
        assert u'아마두' == self.hangulize(u'Amado')
        assert u'코스타' == self.hangulize(u'Costa')
        assert u'디아만티나' == self.hangulize(u'Diamantina')
        assert u'알레그레트' == self.hangulize(u'Alegrete')
        assert u'몬트스' == self.hangulize(u'Montes')

    def test_4th(self):
        """제4항
        어말의 -che는 ‘시'로 적는다.
        """
        assert u'앙고시' == self.hangulize(u'Angoche')
        assert u'페니시' == self.hangulize(u'Peniche')

    def test_5th(self):
        """제5항: l
        1. 어중의 l이 모음 앞에 오거나 모음이 따르지 않는 비음 앞에 오는
           경우에는 ‘?'로 적는다. 다만, 비음 뒤의 l은 모음 앞에 오더라도 ‘ㄹ'로
           적는다.
        2. 어말 또는 자음 앞의 l은 받침 ‘ㄹ'로 적는다.
        """
        assert u'카를루스' == self.hangulize(u'Carlos')
        assert u'아말리아' == self.hangulize(u'Amalia')
        assert u'술' == self.hangulize(u'Sul')
        assert u'아줄' == self.hangulize(u'Azul')
        assert u'질베르투' == self.hangulize(u'Gilberto')
        assert u'카라콜' == self.hangulize(u'Caracol')

    def test_6th(self):
        """제6항
        m, n은 각각 ㅁ, ㄴ으로 적고, 어말에서는 모두 받침 ‘ㅇ'으로 적는다.
        어말 -ns의 n도 받침 ‘ㅇ'으로 적는다.
        """
        assert u'마누엘' == self.hangulize(u'Manuel')
        assert u'모니스' == self.hangulize(u'Moniz')
        assert u'캄푸스' == self.hangulize(u'Campos')
        assert u'빈센트' == self.hangulize(u'Vincente')
        assert u'산타렝' == self.hangulize(u'Santarem')
        assert u'혼동' == self.hangulize(u'Rondon')
        assert u'링스' == self.hangulize(u'Lins')
        assert u'후벵스' == self.hangulize(u'Rubens')

    def test_7th(self):
        """제7항
        ng, nc, nq 연쇄에서 ‘g, c, q'가 ‘ㄱ'이나 ‘ㅋ'으로 표기되면 ‘n'은
        받침 ‘ㅇ'으로 적는다.
        """
        assert u'앙골라' == self.hangulize(u'Angola')
        assert u'안젤루' == self.hangulize(u'Angelo')
        assert u'브랑쿠' == self.hangulize(u'Branco')
        assert u'프란시스쿠' == self.hangulize(u'Francisco')
        assert u'콩키스타' == self.hangulize(u'Conquista')
        assert u'중케이루' == self.hangulize(u'Junqueiro')

    def test_8th(self):
        """제8항
        r는 어두나 n, l, s 뒤에 오는 경우에는 ‘ㅎ'으로 적고, 그 밖의 경우에는
        ‘ㄹ, 르'로 적는다.
        """
        assert u'히베이루' == self.hangulize(u'Ribeiro')
        assert u'엔히크' == self.hangulize(u'Henrique')
        assert u'반데이라' == self.hangulize(u'Bandeira')
        assert u'살라자르' == self.hangulize(u'Salazar')

    def test_9th(self):
        """제9항: s
        1. 어두나 모음 앞에서는 ‘ㅅ'으로 적고, 모음 사이에서는 ‘ㅈ'으로 적는다.
        2. 무성 자음 앞이나 어말에서는 ‘스'로 적고, 유성 자음 앞에서는 ‘즈'로
           적는다.
        """
        assert u'살라자르' == self.hangulize(u'Salazar')
        assert u'아폰수' == self.hangulize(u'Afonso')
        assert u'바호주' == self.hangulize(u'Barroso')
        assert u'제르바지우' == self.hangulize(u'Gervasio')

    def test_10th(self):
        """제10항: sc, sç, xc
        sc와 xc는 e, i 앞에서 ‘ㅅ'으로 적는다. sç는 항상 ‘ㅅ'으로 적는다.
        """
        assert u'나시멘투' == self.hangulize(u'Nascimento')
        assert u'피시나' == self.hangulize(u'piscina')
        assert u'이셀렌트' == self.hangulize(u'excelente')
        assert u'크레사' == self.hangulize(u'cresça')

    def test_11st(self):
        """제11항
        x는 ‘시'로 적되, 어두 e와 모음 사이에 오는 경우에는 ‘ㅈ'으로 적는다.
        """
        assert u'테이셰이라' == self.hangulize(u'Teixeira')
        assert u'리슈' == self.hangulize(u'lixo')
        assert u'이자므' == self.hangulize(u'exame')
        assert u'이젬플루' == self.hangulize(u'exemplo')

    def test_12nd(self):
        """제12항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만, rr는
        ‘ㅎ, 흐'로, ss는 ‘ㅅ, 스'로 적는다.
        """
        assert u'가헤트' == self.hangulize(u'Garrett')
        assert u'바호주' == self.hangulize(u'Barroso')
        assert u'마토주' == self.hangulize(u'Mattoso')
        assert u'토레스' == self.hangulize(u'Toress')

    def test_13rd(self):
        """제13항
        o는 ‘오'로 적되, 어말이나 -os의 o는 ‘우'로 적는다.
        """
        assert u'노브르' == self.hangulize(u'Nobre')
        assert u'안토니우' == self.hangulize(u'Antonio')
        assert u'멜루' == self.hangulize(u'Melo')
        assert u'사라마구' == self.hangulize(u'Saramago')
        assert u'파수스' == self.hangulize(u'Passos')
        assert u'라구스' == self.hangulize(u'Lagos')

    def test_14th(self):
        """제14항
        e는 ‘에'로 적되, 어두 무강세 음절에서는 ‘이'로 적는다. 어말에서는
        ‘으'로 적는다.
        """
        assert u'몬테마요르' == self.hangulize(u'Montemayor')
        assert u'이스트레모스' == self.hangulize(u'Estremoz')
        assert u'시프르' == self.hangulize(u'Chifre')
        assert u'드' == self.hangulize(u'de')

    def test_15th(self):
        """제15항: -es
        1. p, b, m, f, v 다음에 오는 어말 -es는 ‘-에스'로 적는다.
        2. 그 밖의 어말 -es는 ‘-으스'로 적는다.
        """
        assert u'로페스' == self.hangulize(u'Lopes')
        assert u'고메스' == self.hangulize(u'Gomes')
        assert u'네베스' == self.hangulize(u'Neves')
        assert u'샤베스' == self.hangulize(u'Chaves')
        assert u'소아르스' == self.hangulize(u'Soares')
        assert u'피르스' == self.hangulize(u'Pires')

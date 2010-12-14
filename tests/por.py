# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.por import Portuguese


class PortugueseTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0219.jsp """

    lang = Portuguese()

    def test_1st(self):
        """제1항
        c, g는 a, o, u 앞에서는 각각 ‘ㅋ, ㄱ'으로 적고, e, i 앞에서는
        ‘ㅅ, ㅈ'으로 적는다.
        """
        self.assert_examples({
            u'Cabral': u'카브랄',
            u'Camocim': u'카모싱',
            u'Egas': u'에가스',
            u'Gil': u'질',
        })

    def test_2nd(self):
        """제2항
        gu, qu는 a, o, u 앞에서는 각각 ‘구, 쿠'로 적고, e, i 앞에서는
        ‘ㄱ, ㅋ'으로 적는다.
        """
        self.assert_examples({
            u'Iguaçú': u'이구아수',
            u'Araquari': u'아라쿠아리',
            u'Guerra': u'게하',
            u'Aquilino': u'아킬리누',
        })

    def test_3rd(self):
        """제3항
        d, t는 ㄷ, ㅌ으로 적는다.
        """
        self.assert_examples({
            u'Amado': u'아마두',
            u'Costa': u'코스타',
            u'Diamantina': u'디아만티나',
            u'Alegrete': u'알레그레트',
            u'Montes': u'몬트스',
        })

    def test_4th(self):
        """제4항
        어말의 -che는 ‘시'로 적는다.
        """
        self.assert_examples({
            u'Angoche': u'앙고시',
            u'Peniche': u'페니시',
        })

    def test_5th(self):
        """제5항: l
        1. 어중의 l이 모음 앞에 오거나 모음이 따르지 않는 비음 앞에 오는
           경우에는 ‘?'로 적는다. 다만, 비음 뒤의 l은 모음 앞에 오더라도 ‘ㄹ'로
           적는다.
        2. 어말 또는 자음 앞의 l은 받침 ‘ㄹ'로 적는다.
        """
        self.assert_examples({
            u'Carlos': u'카를루스',
            u'Amalia': u'아말리아',
            u'Sul': u'술',
            u'Azul': u'아줄',
            u'Gilberto': u'질베르투',
            u'Caracol': u'카라콜',
        })

    def test_6th(self):
        """제6항
        m, n은 각각 ㅁ, ㄴ으로 적고, 어말에서는 모두 받침 ‘ㅇ'으로 적는다.
        어말 -ns의 n도 받침 ‘ㅇ'으로 적는다.
        """
        self.assert_examples({
            u'Manuel': u'마누엘',
            u'Moniz': u'모니스',
            u'Campos': u'캄푸스',
            u'Vincente': u'빈센트',
            u'Santarem': u'산타렝',
            u'Rondon': u'혼동',
            u'Lins': u'링스',
            u'Rubens': u'후벵스',
        })

    def test_7th(self):
        """제7항
        ng, nc, nq 연쇄에서 ‘g, c, q'가 ‘ㄱ'이나 ‘ㅋ'으로 표기되면 ‘n'은
        받침 ‘ㅇ'으로 적는다.
        """
        self.assert_examples({
            u'Angola': u'앙골라',
            u'Angelo': u'안젤루',
            u'Branco': u'브랑쿠',
            u'Francisco': u'프란시스쿠',
            u'Conquista': u'콩키스타',
            u'Junqueiro': u'중케이루',
        })

    def test_8th(self):
        """제8항
        r는 어두나 n, l, s 뒤에 오는 경우에는 ‘ㅎ'으로 적고, 그 밖의 경우에는
        ‘ㄹ, 르'로 적는다.
        """
        self.assert_examples({
            u'Ribeiro': u'히베이루',
            u'Henrique': u'엔히크',
            u'Bandeira': u'반데이라',
            u'Salazar': u'살라자르',
        })

    def test_9th(self):
        """제9항: s
        1. 어두나 모음 앞에서는 ‘ㅅ'으로 적고, 모음 사이에서는 ‘ㅈ'으로 적는다.
        2. 무성 자음 앞이나 어말에서는 ‘스'로 적고, 유성 자음 앞에서는 ‘즈'로
           적는다.
        """
        self.assert_examples({
            u'Salazar': u'살라자르',
            u'Afonso': u'아폰수',
            u'Barroso': u'바호주',
            u'Gervasio': u'제르바지우',
        })

    def test_10th(self):
        """제10항: sc, sç, xc
        sc와 xc는 e, i 앞에서 ‘ㅅ'으로 적는다. sç는 항상 ‘ㅅ'으로 적는다.
        """
        self.assert_examples({
            u'Nascimento': u'나시멘투',
            u'piscina': u'피시나',
            u'excelente': u'이셀렌트',
            u'cresça': u'크레사',
        })

    def test_11st(self):
        """제11항
        x는 ‘시'로 적되, 어두 e와 모음 사이에 오는 경우에는 ‘ㅈ'으로 적는다.
        """
        self.assert_examples({
            u'Teixeira': u'테이셰이라',
            u'lixo': u'리슈',
            u'exame': u'이자므',
            u'exemplo': u'이젬플루',
        })

    def test_12nd(self):
        """제12항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만, rr는
        ‘ㅎ, 흐'로, ss는 ‘ㅅ, 스'로 적는다.
        """
        self.assert_examples({
            u'Garrett': u'가헤트',
            u'Barroso': u'바호주',
            u'Mattoso': u'마토주',
            u'Toress': u'토레스',
        })

    def test_13rd(self):
        """제13항
        o는 ‘오'로 적되, 어말이나 -os의 o는 ‘우'로 적는다.
        """
        self.assert_examples({
            u'Nobre': u'노브르',
            u'Antonio': u'안토니우',
            u'Melo': u'멜루',
            u'Saramago': u'사라마구',
            u'Passos': u'파수스',
            u'Lagos': u'라구스',
        })

    def test_14th(self):
        """제14항
        e는 ‘에'로 적되, 어두 무강세 음절에서는 ‘이'로 적는다. 어말에서는
        ‘으'로 적는다.
        """
        self.assert_examples({
            u'Montemayor': u'몬테마요르',
            u'Estremoz': u'이스트레모스',
            u'Chifre': u'시프르',
            u'de': u'드',
        })

    def test_15th(self):
        """제15항: -es
        1. p, b, m, f, v 다음에 오는 어말 -es는 ‘-에스'로 적는다.
        2. 그 밖의 어말 -es는 ‘-으스'로 적는다.
        """
        self.assert_examples({
            u'Lopes': u'로페스',
            u'Gomes': u'고메스',
            u'Neves': u'네베스',
            u'Chaves': u'샤베스',
            u'Soares': u'소아르스',
            u'Pires': u'피르스',
        })
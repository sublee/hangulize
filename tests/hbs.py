# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.hbs import SerboCroatian


class SerboCroatianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0210.jsp """

    lang = SerboCroatian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0108.jsp """
        self.assert_examples({
            u'bog': u'보그',
            u'drobnjak': u'드로브냐크',
            u'pogreb': u'포그레브',
            u'cigara': u'치가라',
            u'novac': u'노바츠',
            u'čelik': u'첼리크',
            u'točka': u'토치카',
            u'kolač': u'콜라치',
            u'naći': u'나치',
            u'sestrić': u'세스트리치',
            u'desno': u'데스노',
            u'drvo': u'드르보',
            u'medved': u'메드베드',
            u'džep': u'제프',
            u'narudžba': u'나루지바',
        #    u'Ðurađ': u'주라지',
            u'fasada': u'파사다',
            u'kifla': u'키플라',
            u'šaraf': u'샤라프',
            u'gost': u'고스트',
            u'dugme': u'두그메',
            u'krug': u'크루그',
            u'hitan': u'히탄',
            u'šah': u'샤흐',
            u'korist': u'코리스트',
            u'krug': u'크루그',
            u'jastuk': u'야스투크',
            u'levo': u'레보',
            u'balkon': u'발콘',
            u'šal': u'샬',
            u'ljeto': u'레토',
            u'pasulj': u'파술',
            u'malo': u'말로',
            u'mnogo': u'므노고',
            u'osam': u'오삼',
            u'nos': u'노스',
            u'banka': u'반카',
            u'loman': u'로만',
            u'Njegoš': u'네고시',
            u'svibanj': u'스비반',
            u'peta': u'페타',
            u'opština': u'옵슈티나',
            u'lep': u'레프',
            u'riba': u'리바',
            u'torba': u'토르바',
            u'mir': u'미르',
            u'sedam': u'세담',
            u'posle': u'포슬레',
            u'glas': u'글라스',
            u'šal': u'샬',
            u'vlasništvo': u'블라스니슈트보',
            u'broš': u'브로시',
            u'telo': u'텔로',
            u'ostrvo': u'오스트르보',
            u'put': u'푸트',
            u'vatra': u'바트라',
            u'olovka': u'올로브카',
            u'proliv': u'프롤리브',
            u'zavoj': u'자보이',
            u'pozno': u'포즈노',
            u'obraz': u'오브라즈',
            u'žena': u'제나',
            u'izložba': u'이즐로주바',
            u'muž': u'무주',
            u'pojas': u'포야스',
            u'zavoj': u'자보이',
            u'odjelo': u'오델로',
            u'bakar': u'바카르',
            u'cev': u'체브',
            u'dim': u'딤',
            u'molim': u'몰림',
            u'zubar': u'주바르',
        })

    def test_1st(self):
        """제1항: k, p
        k, p는 어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            u'jastuk': u'야스투크',
            u'јастук': u'야스투크',
            u'opština': u'옵슈티나',
            u'општина': u'옵슈티나',
        })

    def test_2nd(self):
        """제2항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            u'kula': u'쿨라',
            u'кула': u'쿨라',
        })

    def test_3rd(self):
        """제3항: m
        어두의 m이 l, r, n 앞에 오거나 어중의 m이 r 앞에 올 때에는 '으'를
        붙여 적는다.
        """
        self.assert_examples({
            u'mlad': u'믈라드',
            u'млад': u'믈라드',
            u'mnogo': u'므노고',
            u'много': u'므노고',
            u'smrt': u'스므르트',
            u'смрт': u'스므르트',
        })

    def test_4th(self):
        """제4항: š
        š는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        self.assert_examples({
            u'šljivovica': u'슐리보비차',
            u'шљивовица': u'슐리보비차',
            u'Niš': u'니시',
            u'Ниш': u'니시',
        })

    def test_5th(self):
        """제5항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        self.assert_examples({
            u'bjedro': u'베드로',
            u'бједро': u'베드로',
            u'sjedlo': u'셰들로',
            u'сједло': u'셰들로',
        })

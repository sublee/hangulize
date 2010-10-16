# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class SerboCroatianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0210.jsp """

    def setUp(self):
        from hangulize.langs.sh import SerboCroatian
        self.lang = SerboCroatian()
    
    def test_1st(self):
        """제1항: k, p
        k, p는 어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'야스투크' == self.hangulize(u'jastuk')
        assert u'야스투크' == self.hangulize(u'јастук')
        assert u'옵슈티나' == self.hangulize(u'opština')
        assert u'옵슈티나' == self.hangulize(u'општина')

    def test_2nd(self):
        """제2항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        assert u'쿨라' == self.hangulize(u'kula')
        assert u'쿨라' == self.hangulize(u'кула')

    def test_3rd(self):
        """제3항: m
        어두의 m이 l, r, n 앞에 오거나 어중의 m이 r 앞에 올 때에는 '으'를
        붙여 적는다.
        """
        assert u'믈라드' == self.hangulize(u'mlad')
        assert u'믈라드' == self.hangulize(u'млад')
        assert u'므노고' == self.hangulize(u'mnogo')
        assert u'므노고' == self.hangulize(u'много')
        assert u'스므르트' == self.hangulize(u'smrt')
        assert u'스므르트' == self.hangulize(u'смрт')

    def test_4th(self):
        """제4항: š
        š는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        assert u'슐리보비차' == self.hangulize(u'šljivovica')
        assert u'슐리보비차' == self.hangulize(u'шљивовица')
        assert u'니시' == self.hangulize(u'Niš')
        assert u'니시' == self.hangulize(u'Ниш')

    def test_5th(self):
        """제5항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        assert u'베드로' == self.hangulize(u'bjedro')
        assert u'베드로' == self.hangulize(u'бједро')
        assert u'셰들로' == self.hangulize(u'sjedlo')
        assert u'셰들로' == self.hangulize(u'сједло')


# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class SerboCroatianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0210.jsp """

    def setUp(self):
        from hangulize.langs.sh import SerboCroatian
        self.lang = SerboCroatian()
    
    def test_1st(self):
        """제1항: k, p"""
        assert u'야스투크' == self.hangulize(u'jastuk')
        assert u'옵슈티나' == self.hangulize(u'opština')

    def test_2nd(self):
        """제2항: l"""
        assert u'쿨라' == self.hangulize(u'kula')

    def test_3rd(self):
        """제3항: m"""
        assert u'믈라드' == self.hangulize(u'mlad')
        assert u'므노고' == self.hangulize(u'mnogo')
        assert u'스므르트' == self.hangulize(u'smrt')

    def test_4th(self):
        """제4항: š"""
        assert u'슐리보비차' == self.hangulize(u'šljivovica')
        assert u'니시' == self.hangulize(u'Niš')

    def test_5th(self):
        """제5항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        assert u'베드로' == self.hangulize(u'bjedro')
        #assert u'셰들로' == self.hangulize(u'sjedlo')


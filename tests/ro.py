# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class RomanianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0211.jsp """

    def setUp(self):
        from hangulize.langs.ro import Romanian
        self.lang = Romanian()
    
    def test_1st(self):
        """제1항: c, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'카프' == self.hangulize(u'cap')
        assert u'큰테크' == self.hangulize(u'Cîntec')
        assert u'팍투러' == self.hangulize(u'factură')
        assert u'셉템브리에' == self.hangulize(u'septembrie')

    def test_2nd(self):
        """제2항: c, g
        c, g는 e, i 앞에서는 각각 'ㅊ', 'ㅈ'으로, 그 밖의 모음 앞에서는 'ㅋ',
        'ㄱ'으로 적는다.
        """
        assert u'카프' == self.hangulize(u'cap')
        assert u'첸트루' == self.hangulize(u'centru')
        assert u'갈라치' == self.hangulize(u'Galaţi')
        assert u'지젤' == self.hangulize(u'Gigel')

    def test_3rd(self):
        """제3항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        assert u'클레이' == self.hangulize(u'clei')

    def test_4th(self):
        """제4항: n
        n이 어말에서 m 뒤에 올 때는 '으'를 붙여 적는다.
        """
        assert u'렘느' == self.hangulize(u'lemn')
        assert u'품느' == self.hangulize(u'pumn')

    def test_5th(self):
        """제5항: e
        e는 '에'로 적되, 인칭 대명사 및 동사 este, era 등의 어두 모음 e는
        '예'로 적는다.
        """
        assert u'에밀' == self.hangulize(u'Emil')
        assert u'예우' == self.hangulize(u'eu')
        assert u'옐' == self.hangulize(u'el')
        assert u'예스테' == self.hangulize(u'este')
        assert u'예라' == self.hangulize(u'era')


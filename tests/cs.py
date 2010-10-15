# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class CzechTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0205.jsp """

    def setUp(self):
        from hangulize.langs.cs import Czech
        self.lang = Czech()

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'모제크' == self.hangulize(u'mozek')
        assert u'코롭테프' == self.hangulize(u'koroptev')

    def test_2nd(self):
        """제2항: b, d, d', g
        1. 어말에 올 때에는 '프', '트', '티', '크'로 적는다.
        2. 유성 자음 앞에서는 '브', '드', '디', '그'로 적는다.
        3. 무성 자음 앞에서 b, g는 받침으로 적고, d, d'는 '트', '티'로 적는다.
        """
        assert u'레트' == self.hangulize(u'led')
        assert u'레드비나' == self.hangulize(u'ledvina')
        assert u'옵호트' == self.hangulize(u'obchod')
        assert u'오트파트키' == self.hangulize(u'odpadky')

    def test_3nd(self):
        """제3항: v, w, z, ř, ž, š
        1. v, w, z가 무성 자음 앞이나 어말에 올 때에는 '프, 프, 스'로 적는다.
        2. ř, ž가 유성 자음 앞에 올 때에는 '르주', '주', 무성 자음 앞에 올
           때에는 '르슈', '슈', 어말에 올 때에는 '르시', '시'로 적는다.
        3. š는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        assert u'흐미스' == self.hangulize(u'hmyz')
        assert u'나모르주니크' == self.hangulize(u'námořník')
        assert u'호르슈키' == self.hangulize(u'hořký')
        assert u'코우르시' == self.hangulize(u'kouř')
        assert u'푸슈카' == self.hangulize(u'puška')
        assert u'미시' == self.hangulize(u'myš')

    def test_4th(self):
        """제4항: l, lj
        어중의 l, lj가 모음 앞에 올 때에는 'ㄹㄹ', 'ㄹ리'로 적는다.
        """
        assert u'콜로' == self.hangulize(u'kolo')

    def test_5th(self):
        """제5항: m
        m이 r 앞에 올 때에는 '으'를 붙여 적는다.
        """
        assert u'후므르' == self.hangulize(u'humr')

    def test_6th(self):
        """제6항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        assert u'베크' == self.hangulize(u'věk')
        assert u'셰스트' == self.hangulize(u'šest')


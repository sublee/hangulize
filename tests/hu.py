# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class HungarianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0212.jsp """

    def setUp(self):
        from hangulize.langs.hu import Hungarian
        self.lang = Hungarian()
    
    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'어블러크' == self.hangulize(u'ablak')
        assert u'칩케' == self.hangulize(u'csipke')

    def test_2nd(self):
        """제2항
        bb, cc, dd, ff, gg, ggy, kk, ll, lly, nn, nny, pp, rr, ss, ssz, tt,
        tty는 b, c, d, f, g, gy, k, l, ly, n, ny, p, r, s, sz, t, ty와 같이
        적는다. 다만, 어중의 nn, nny와 모음 앞의 ll은 'ㄴㄴ', 'ㄴ니',
        'ㄹㄹ'로 적는다.
        """
        assert u'쾨죄트' == self.hangulize(u'között')
        assert u'딘네' == self.hangulize(u'dinnye')
        assert u'눌러' == self.hangulize(u'nulla')

    def test_3rd(self):
        """제3항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        assert u'올러이' == self.hangulize(u'olaj')

    def test_4th(self):
        """제4항: s
        s는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        assert u'페슈트' == self.hangulize(u'Pest')
        assert u'러포시' == self.hangulize(u'lapos')

    def test_5th(self):
        """제5항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        assert u'네르' == self.hangulize(u'nyer')
        #assert u'셰옘' == self.hangulize(u'selyem')


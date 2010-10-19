# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class VietnameseTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0218.jsp """

    def setUp(self):
        from hangulize.langs.vi import Vietnamese
        self.lang = Vietnamese()
    
    def test_1st(self):
        """제1항
        nh는 이어지는 모음과 합쳐서 한 음절로 적는다. 어말이나 자음 앞에서는
        받침 ‘ㄴ' 으로 적되, 그 앞의 모음이 a인 경우에는 a와 합쳐 ‘아인'으로
        적는다.
        """
        #assert u'냐짱' == self.hangulize(u'Nha Trang')
        #assert u'호찌민' == self.hangulize(u'Hô Chi Minh')
        #assert u'타인호아' == self.hangulize(u'Thanh Hoa')
        #assert u'동카인' == self.hangulize(u'Đông Khanh')

    def test_2nd(self):
        """제2항
        qu는 이어지는 모음이 a일 경우에는 합쳐서 ‘꽈'로 적는다.
        """
        assert u'꽝' == self.hangulize(u'Quang')
        #assert u'핫꽌호' == self.hangulize(u'hat quan ho')
        assert u'꾸옥' == self.hangulize(u'Quôc')
        assert u'꾸옌' == self.hangulize(u'Quyên')

    def test_3rd(self):
        """제3항
        y는 뒤따르는 모음과 합쳐서 한 음절로 적는다.
        """
        assert u'옌' == self.hangulize(u'yên')
        assert u'응우옌' == self.hangulize(u'Nguyên')

    def test_4th(self):
        """제4항
        어중의 l이 모음 앞에 올 때에는 ‘ㄹㄹ'로 적는다.
        다만, 인명의 성과 이름은 별개의 단어로 보아 이 규칙을 적용하지 않는다.
        """
        #assert u'끌롱쁫' == self.hangulize(u'klông put')
        assert u'쁠래이꾸' == self.hangulize(u'Pleiku')
        #assert u'할롱' == self.hangulize(u'Ha Long')
        #assert u'밀라이' == self.hangulize(u'My Lay')


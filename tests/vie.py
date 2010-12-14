# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.vie import Vietnamese


class VietnameseTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0218.jsp """

    lang = Vietnamese()

    def test_1st(self):
        """제1항
        nh는 이어지는 모음과 합쳐서 한 음절로 적는다. 어말이나 자음 앞에서는
        받침 ‘ㄴ' 으로 적되, 그 앞의 모음이 a인 경우에는 a와 합쳐 ‘아인'으로
        적는다.
        """
        self.assert_examples({
        #    u'Nha Trang': u'냐짱',
        #    u'Hô Chi Minh': u'호찌민',
        #    u'Thanh Hoa': u'타인호아',
        #    u'Đông Khanh': u'동카인',
        })

    def test_2nd(self):
        """제2항
        qu는 이어지는 모음이 a일 경우에는 합쳐서 ‘꽈'로 적는다.
        """
        self.assert_examples({
            u'Quang': u'꽝',
        #    u'hat quan ho': u'핫꽌호',
            u'Quôc': u'꾸옥',
            u'Quyên': u'꾸옌',
        })

    def test_3rd(self):
        """제3항
        y는 뒤따르는 모음과 합쳐서 한 음절로 적는다.
        """
        self.assert_examples({
            u'yên': u'옌',
            u'Nguyên': u'응우옌',
        })

    def test_4th(self):
        """제4항
        어중의 l이 모음 앞에 올 때에는 ‘ㄹㄹ'로 적는다.
        다만, 인명의 성과 이름은 별개의 단어로 보아 이 규칙을 적용하지 않는다.
        """
        self.assert_examples({
        #    u'klông put': u'끌롱쁫',
            u'Pleiku': u'쁠래이꾸',
        #    u'Ha Long': u'할롱',
        #    u'My Lay': u'밀라이',
        })
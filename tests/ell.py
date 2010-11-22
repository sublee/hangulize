# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ell import ModernGreek


class ModernGreekTestCase(HangulizeTestCase):

    lang = ModernGreek()

    def test_examples_of_iceager(self):
        assert u'피이' == self.hangulize(u'πηγή')
        assert u'요르이아' == self.hangulize(u'Γιωργία')
        assert u'헤리' == self.hangulize(u'χέρι')
        assert u'헤레테' == self.hangulize(u'χαίρετε')

    '''
    def test_1st(self):
        """y는 ‘이'로 적는다."""
        assert u'폴리비오스' == self.hangulize(u'Polybios')

    def test_2nd(self):
        """ae, oe, ou는 각각 ‘아이', ‘오이', ‘우'로 적는다."""
        assert u'아카이아' == self.hangulize(u'Achaea')
        assert u'델포이' == self.hangulize(u'Delphoe')
        assert u'에피쿠로스' == self.hangulize(u'Epicouros')

    def test_3rd(self):
        """c와 ch는 [k]의 표기 방법에 따라 적는다."""
        assert u'케르키라' == self.hangulize(u'Cercyra')
        assert u'아이스킬로스' == self.hangulize(u'Aeschylos')

    def test_4th(self):
        """g, c, ch, h 앞의 n은 받침 ‘ㅇ'으로 적는다."""
        assert u'앙키라' == self.hangulize(u'ancyra')
    '''

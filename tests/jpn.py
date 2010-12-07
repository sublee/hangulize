# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.jpn import Japanese


class JapaneseTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0206.jsp """

    lang = Japanese()

    def test_1st(self):
        """제1항: 촉음
        촉음(促音) [ッ(っ)]는 'ㅅ'으로 통일해서 적는다.
        """
        assert u'삿포로' == self.hangulize(u'サッポロ')
        assert u'돗토리' == self.hangulize(u'トットリ')
        assert u'욧카이치' == self.hangulize(u'ヨッカイチ')

    def test_2nd(self):
        """제2항: 장모음
        장모음은 따로 표기하지 않는다.
        """
        assert u'규슈' == self.hangulize(u'キュウシュウ')
        assert u'니가타' == self.hangulize(u'ニイガタ')
        assert u'도쿄' == self.hangulize(u'トウキョウ')
        assert u'오사카' == self.hangulize(u'オオサカ')

    def test_hangulize(self):
        assert u'니혼' == self.hangulize(u'にほん')
        assert u'니혼바시' == self.hangulize(u'にほんばし')
        assert u'아카찬' == self.hangulize(u'あかちゃん')

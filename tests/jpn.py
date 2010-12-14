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
        self.assert_examples({
            u'サッポロ': u'삿포로',
            u'トットリ': u'돗토리',
            u'ヨッカイチ': u'욧카이치',
        })

    def test_2nd(self):
        """제2항: 장모음
        장모음은 따로 표기하지 않는다.
        """
        self.assert_examples({
            u'キュウシュウ': u'규슈',
            u'ニイガタ': u'니가타',
            u'トウキョウ': u'도쿄',
            u'オオサカ': u'오사카',
        })

    def test_hangulize(self):
        self.assert_examples({
            u'にほん': u'니혼',
            u'にほんばし': u'니혼바시',
            u'あかちゃん': u'아카찬',
        })
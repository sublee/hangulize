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

    def test_examples_a_column(self):
        self.assert_examples({
            u'あゆみ': u'아유미',
            u'あつぎ': u'아쓰기',
            u'あいづわかまつ': u'아이즈와카마쓰',
            u'あらかわ': u'아라카와',
            u'へいあん': u'헤이안',
            u'あきた': u'아키타',
            u'あきはばら': u'아키하바라',
            u'あおもり': u'아오모리',
            u'あまくさ': u'아마쿠사',
            u'あさま': u'아사마',
            u'あしお': u'아시오',
            u'あしかが': u'아시카가',
            u'あかぎ': u'아카기',
            u'あかいし': u'아카이시',
            u'おあかん': u'오아칸',
            u'あさひかわ': u'아사히카와',
            u'あご': u'아고',
            u'あたみ': u'아타미',
            u'あまみおお': u'아마미오',
            u'あいち': u'아이치',
            u'あんじょう': u'안조',
            u'あつみ': u'아쓰미',
            u'あかん': u'아칸',
            u'あそ': u'아소',
            u'あぶくま': u'아부쿠마',
            u'あげお': u'아게오',
            u'おわりあさひ': u'오와리아사히',
            u'あすか': u'아스카',
            u'あかし': u'아카시',
            u'あばしり': u'아바시리',
            u'あやべ': u'아야베',
            u'あしのこ': u'아시노코',
            u'あわじ': u'아와지',
            u'あまがさき': u'아마가사키',
            u'くろさわ あきら': u'구로사와 아키라',
            u'ごとう あつし': u'고토 아쓰시',
        })

# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.deu import German


class GermanTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0202.jsp """

    lang = German()

    def test_1st(self):
        """제1항: 
        1. 자음 앞의 는 '으'를 붙여 적는다.
        2. 어말의 '는 '어'로 적는다.
        3. 복합어 및 파생어의 선행 요소가 로 끝나는 경우는 2의 규정을 준용한다.
        """
        self.assert_examples({
            u'Hormon': u'호르몬',
            u'Hermes': u'헤르메스',
            u'Herr': u'헤어',
            u'Rasur': u'라주어',
            u'Tür': u'튀어',
            u'Ohr': u'오어',
            u'Vater': u'파터',
            u'Schiller': u'실러',
        # 합성어
        #    u'verarbeiten': u'페어아르바이텐',
        #    u'zerknirschen': u'체어크니르셴',
        #    u'Fürsorge': u'퓌어조르게',
        #    u'Vorbild': u'포어빌트',
        #    u'auβerhalb': u'아우서할프',
        #    u'Urkunde': u'우어쿤데',
        #    u'Vaterland': u'파터란트',
        })

    def test_2nd(self):
        """제2항: 어말의 파열음은 '으'를 붙여 적는 것을 원칙으로 한다."""
        self.assert_examples({
        #    u'Rostock': u'로스토크', # 규칙?
            u'Stadt': u'슈타트',
        })

    def test_3rd(self):
        """제3항: 철자 'berg', 'burg'는 '베르크', '부르크'로 통일해서 적는다."""
        self.assert_examples({
            u'Heidelberg': u'하이델베르크',
            u'Hamburg': u'함부르크',
        })

    def test_4th(self):
        """제4항: 
        1. 어말 또는 자음 앞에서는 '슈'로 적는다.
        2.  앞에서는 'ㅅ'으로 적는다.
        3. 그 밖의 모음 앞에서는 뒤따르는 모음에 따라 '샤, 쇼, 슈' 등으로 적는다.
        """
        self.assert_examples({
            u'Mensch': u'멘슈',
            u'Mischling': u'미슐링',
            u'Schüler': u'쉴러',
            u'schön': u'쇤',
            u'Schatz': u'샤츠',
            u'schon': u'숀',
            u'Schule': u'슐레',
            u'Schelle': u'셸레',
        })

    def test_5th(self):
        """제5항: 로 발음되는 äu, eu는 '오이'로 적는다."""
        self.assert_examples({
            u'läuten': u'로이텐',
            u'Fräulein': u'프로일라인',
            u'Europa': u'오이로파',
            u'Freundin': u'프로인딘',
        })

    def test_6th(self):
        """연음, -st, ich/achlaut, 움라우트, 강세음절의 r"""
        self.assert_examples({
            u'ein': u'아인',
            u'einer': u'아이너',
            u'einen': u'아이넨',
            u'ist': u'이스트',
            u'bist': u'비스트',
            u'Buch': u'부흐',
            u'ich': u'이히',
            u'Königen': u'쾨니겐',
            u'für': u'퓌어',
            u'der': u'데어',
        })

    def test_7th(self):
        """준칙: 모음 또는 l 앞의 ng에는 'ㄱ'을 첨가하여 표기한다."""
        self.assert_examples({
            u'Tübingen': u'튀빙겐',
            u'Spengler': u'슈펭글러',
        })

    def test_8th(self):
        """기타 용례"""
        self.assert_examples({
            u'Fischer': u'피셔',
            u'Richard': u'리하르트',
            u'Niclas': u'니클라스',
            u'Kupfer': u'쿠퍼',
            u'Beelitz': u'벨리츠',
        })
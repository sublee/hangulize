# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class GermanTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0202.jsp """

    def setUp(self):
        from hangulize.langs.de import German
        self.lang = German()
    
    def test_1st(self):
        """제1항: 
        1. 자음 앞의 는 '으'를 붙여 적는다.
        2. 어말의 '는 '어'로 적는다.
        3. 복합어 및 파생어의 선행 요소가 로 끝나는 경우는 2의 규정을 준용한다.
        """
        assert u'호르몬' == self.hangulize(u'Hormon')
        assert u'헤르메스' == self.hangulize(u'Hermes')
        assert u'헤어' == self.hangulize(u'Herr')
        #assert u'라주어' == self.hangulize(u'Razur') # z가 ㅈ ?
        assert u'튀어' == self.hangulize(u'Tür')
        assert u'오어' == self.hangulize(u'Ohr')
        assert u'파터' == self.hangulize(u'Vater')
        assert u'실러' == self.hangulize(u'Schiller')
        # 합성어
        #assert u'페어아르바이텐' == self.hangulize(u'verarbeiten')
        #assert u'체어크니르셴' == self.hangulize(u'zerknirschen')
        #assert u'퓌어조르게' == self.hangulize(u'Fürsorge')
        #assert u'포어빌트' == self.hangulize(u'Vorbild')
        #assert u'아우서할프' == self.hangulize(u'auβerhalb')
        #assert u'우어쿤데' == self.hangulize(u'Urkunde')
        #assert u'파터란트' == self.hangulize(u'Vaterland')

    def test_2nd(self):
        """제2항: 어말의 파열음은 '으'를 붙여 적는 것을 원칙으로 한다."""
        #assert u'로스토크' == self.hangulize(u'Rostock') # 규칙?
        assert u'슈타트' == self.hangulize(u'Stadt')

    def test_3rd(self):
        """제3항: 철자 'berg', 'burg'는 '베르크', '부르크'로 통일해서 적는다."""
        assert u'하이델베르크' == self.hangulize(u'Heidelberg')
        assert u'함부르크' == self.hangulize(u'Hamburg')

    def test_4th(self):
        """제4항: 
        1. 어말 또는 자음 앞에서는 '슈'로 적는다.
        2.  앞에서는 'ㅅ'으로 적는다.
        3. 그 밖의 모음 앞에서는 뒤따르는 모음에 따라 '샤, 쇼, 슈' 등으로 적는다.
        """
        assert u'멘슈' == self.hangulize(u'Mensch')
        assert u'미슐링' == self.hangulize(u'Mischling')
        assert u'쉴러' == self.hangulize(u'Schüler')
        assert u'쇤' == self.hangulize(u'schön')
        assert u'샤츠' == self.hangulize(u'Schatz')
        assert u'숀' == self.hangulize(u'schon')
        assert u'슐레' == self.hangulize(u'Schule')
        assert u'셸레' == self.hangulize(u'Schelle')

    def test_5th(self):
        """제5항: 로 발음되는 äu, eu는 '오이'로 적는다."""
        assert u'로이텐' == self.hangulize(u'läuten')
        assert u'프로일라인' == self.hangulize(u'Fräulein')
        assert u'오이로파' == self.hangulize(u'Europa')
        assert u'프로인딘' == self.hangulize(u'Freundin')

    def test_6th(self):
        """연음, -st, ich/achlaut, 움라우트, 강세음절의 r"""
        assert u'아인' == self.hangulize(u'ein')
        assert u'아이너' == self.hangulize(u'einer')
        assert u'아이넨' == self.hangulize(u'einen')
        assert u'이스트' == self.hangulize(u'ist')
        assert u'비스트' == self.hangulize(u'bist')
        assert u'부흐' == self.hangulize(u'buch')
        assert u'이히' == self.hangulize(u'ich')
        assert u'쾨니겐' == self.hangulize(u'königen')
        assert u'퓌어' == self.hangulize(u'für')
        assert u'데어' == self.hangulize(u'der')

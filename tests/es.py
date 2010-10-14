# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class SpanishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0204.jsp """

    def setUp(self):
        from hangulize.langs.es import Spanish
        self.lang = Spanish()

    def test_1st(self):
        """제1항: gu, qu
        gu, qu는 i, e 앞에서는 각각 'ㄱ, ㅋ'으로 적고, o 앞에서는 '구, 쿠'로
        적는다. 다만, a 앞에서는 그 a와 합쳐 '과, 콰'로 적는다.
        """
        assert u'게라' == self.hangulize(u'guerra')
        assert u'케소' == self.hangulize(u'queso')
        assert u'기푸스코아' == self.hangulize(u'Guipuzcoa')
        assert u'키스키야' == self.hangulize(u'quisquilla')
        assert u'안티구오' == self.hangulize(u'antiguo')
        assert u'쿠오렘' == self.hangulize(u'Quorem')
        assert u'니카라과' == self.hangulize(u'Nicaragua')
        assert u'콰라이' == self.hangulize(u'Quarai')

    def test_2nd(self):
        """제2항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만,
        -cc-는 'ㄱㅅ'으로 적는다.
        """
        assert u'카레라' == self.hangulize(u'carrera')
        assert u'카레테라' == self.hangulize(u'carreterra')
        assert u'악시온' == self.hangulize(u'accion')

    def test_3rd(self):
        """제3항: c, g
        c와 g 다음에 모음 e와 i가 올 때에는 c는 'ㅅ'으로, g는 'ㅎ'으로 적고,
        그 외는 'ㅋ'과 'ㄱ'으로 적는다.
        """
        assert u'세실리아' == self.hangulize(u'Cecilia')
        assert u'시프라' == self.hangulize(u'cifra')
        assert u'헤오르히코' == self.hangulize(u'georgico')
        assert u'히간타' == self.hangulize(u'giganta')
        assert u'코키토' == self.hangulize(u'coquito')
        assert u'가토' == self.hangulize(u'gato')

    def test_4th(self):
        """제4항: x
        x가 모음 앞에 오되 어두일 때에는 'ㅅ'으로 적고, 어중일 때에는
        'ㄱㅅ'으로 적는다.
        """
        assert u'실로포노' == self.hangulize(u'xilofono')
        assert u'락산테' == self.hangulize(u'laxante')

    def test_5th(self):
        """제5항: l
        어말 또는 자음 앞의 l은 받침 'ㄹ'로 적고, 어중의 1이 모음 앞에 올
        때에는 'ㄹㄹ'로 적는다.
        """
        assert u'오칼' == self.hangulize(u'ocal')
        assert u'콜크렌' == self.hangulize(u'colcren')
        assert u'블란돈' == self.hangulize(u'blandon')
        assert u'세실리아' == self.hangulize(u'Cecilia')

    def test_6th(self):
        """제6항: nc, ng
        c와 g 앞에 오는 n은 받침 'ㅇ'으로 적는다.
        """
        assert u'블랑코' == self.hangulize(u'blanco')
        assert u'융글라' == self.hangulize(u'yungla')

    def test_hangulize(self):
        assert u'뇨녜스' == self.hangulize(u'ñoñez')
        assert u'궤레로' == self.hangulize(u'güerrero')
        assert u'귀초' == self.hangulize(u'Güicho')
        assert u'가미뇨' == self.hangulize(u'Gamiño')
        assert u'앙헬레스' == self.hangulize(u'Ángeles')
        assert u'호세 오르테가 이 가세트' == \
               self.hangulize(u'José Ortega y Gasset')


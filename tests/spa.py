# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.spa import Spanish


class SpanishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0204.jsp """

    lang = Spanish()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0102.jsp """
        assert u'비스' == self.hangulize(u'biz')
        assert u'블란돈' == self.hangulize(u'blandon')
        assert u'브라세오' == self.hangulize(u'braceo')
        assert u'콜크렌' == self.hangulize(u'colcren')
        assert u'세실리아' == self.hangulize(u'Cecilia')
        assert u'콕시온' == self.hangulize(u'coccion')
        assert u'비스텍' == self.hangulize(u'bistec')
        assert u'딕타도' == self.hangulize(u'dictado')
        assert u'치차라' == self.hangulize(u'chicharra')
        assert u'펠리시다드' == self.hangulize(u'felicidad')
        assert u'푸가' == self.hangulize(u'fuga')
        assert u'프란' == self.hangulize(u'fran')
        assert u'강가' == self.hangulize(u'ganga')
        assert u'헤올로히아' == self.hangulize(u'geologia')
        assert u'융글라' == self.hangulize(u'yungla')
        assert u'이포' == self.hangulize(u'hipo')
        assert u'케아세르' == self.hangulize(u'quehacer')
        assert u'후에베스' == self.hangulize(u'jueves')
        assert u'렐로' == self.hangulize(u'reloj')
        assert u'카포크' == self.hangulize(u'kapok')
        assert u'라크라르' == self.hangulize(u'lacrar')
        assert u'룰리오' == self.hangulize(u'Lulio')
        assert u'오칼' == self.hangulize(u'ocal')
        assert u'야마' == self.hangulize(u'llama')
        assert u'유비아' == self.hangulize(u'lluvia')
        assert u'멤브레테' == self.hangulize(u'membrete')
        assert u'노체' == self.hangulize(u'noche')
        assert u'플란' == self.hangulize(u'flan')
        assert u'뇨녜스' == self.hangulize(u'ñoñez')
        assert u'마냐나' == self.hangulize(u'mañana')
        assert u'펩시나' == self.hangulize(u'pepsina')
        assert u'플란톤' == self.hangulize(u'plantón')
        assert u'키스키야' == self.hangulize(u'quisquilla')
        assert u'라스카도르' == self.hangulize(u'rascador')
        assert u'사스트레리아' == self.hangulize(u'sastreria')
        assert u'테트라에트로' == self.hangulize(u'tetraetro')
        assert u'비우데다드' == self.hangulize(u'viudedad')
        assert u'세논' == self.hangulize(u'xenón')
        assert u'락산테' == self.hangulize(u'laxante')
        assert u'육스타' == self.hangulize(u'yuxta')
        assert u'사갈' == self.hangulize(u'zagal')
        assert u'리키데스' == self.hangulize(u'liquidez')
        assert u'왈키리아스' == self.hangulize(u'walkirias')
        assert u'융글라' == self.hangulize(u'yungla')
        assert u'브라세오' == self.hangulize(u'braceo')
        assert u'렐로' == self.hangulize(u'reloj')
        assert u'룰리오' == self.hangulize(u'Lulio')
        assert u'오칼' == self.hangulize(u'ocal')
        assert u'비우데다드' == self.hangulize(u'viudedad')

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

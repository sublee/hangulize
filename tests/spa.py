# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.spa import Spanish


class SpanishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0204.jsp """

    lang = Spanish()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0102.jsp """
        self.assert_examples({
            u'biz': u'비스',
            u'blandon': u'블란돈',
            u'braceo': u'브라세오',
            u'colcren': u'콜크렌',
            u'Cecilia': u'세실리아',
            u'coccion': u'콕시온',
            u'bistec': u'비스텍',
            u'dictado': u'딕타도',
            u'chicharra': u'치차라',
            u'felicidad': u'펠리시다드',
            u'fuga': u'푸가',
            u'fran': u'프란',
            u'ganga': u'강가',
            u'geologia': u'헤올로히아',
            u'yungla': u'융글라',
            u'hipo': u'이포',
            u'quehacer': u'케아세르',
            u'jueves': u'후에베스',
            u'reloj': u'렐로',
            u'kapok': u'카포크',
            u'lacrar': u'라크라르',
            u'Lulio': u'룰리오',
            u'ocal': u'오칼',
            u'llama': u'야마',
            u'lluvia': u'유비아',
            u'membrete': u'멤브레테',
            u'noche': u'노체',
            u'flan': u'플란',
            u'ñoñez': u'뇨녜스',
            u'mañana': u'마냐나',
            u'pepsina': u'펩시나',
            u'plantón': u'플란톤',
            u'quisquilla': u'키스키야',
            u'rascador': u'라스카도르',
            u'sastreria': u'사스트레리아',
            u'tetraetro': u'테트라에트로',
            u'viudedad': u'비우데다드',
            u'xenón': u'세논',
            u'laxante': u'락산테',
            u'yuxta': u'육스타',
            u'zagal': u'사갈',
            u'liquidez': u'리키데스',
            u'walkirias': u'왈키리아스',
            u'yungla': u'융글라',
            u'braceo': u'브라세오',
            u'reloj': u'렐로',
            u'Lulio': u'룰리오',
            u'ocal': u'오칼',
            u'viudedad': u'비우데다드',
        })

    def test_1st(self):
        """제1항: gu, qu
        gu, qu는 i, e 앞에서는 각각 'ㄱ, ㅋ'으로 적고, o 앞에서는 '구, 쿠'로
        적는다. 다만, a 앞에서는 그 a와 합쳐 '과, 콰'로 적는다.
        """
        self.assert_examples({
            u'guerra': u'게라',
            u'queso': u'케소',
            u'Guipuzcoa': u'기푸스코아',
            u'quisquilla': u'키스키야',
            u'antiguo': u'안티구오',
            u'Quorem': u'쿠오렘',
            u'Nicaragua': u'니카라과',
            u'Quarai': u'콰라이',
        })

    def test_2nd(self):
        """제2항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만,
        -cc-는 'ㄱㅅ'으로 적는다.
        """
        self.assert_examples({
            u'carrera': u'카레라',
            u'carreterra': u'카레테라',
            u'accion': u'악시온',
        })

    def test_3rd(self):
        """제3항: c, g
        c와 g 다음에 모음 e와 i가 올 때에는 c는 'ㅅ'으로, g는 'ㅎ'으로 적고,
        그 외는 'ㅋ'과 'ㄱ'으로 적는다.
        """
        self.assert_examples({
            u'Cecilia': u'세실리아',
            u'cifra': u'시프라',
            u'georgico': u'헤오르히코',
            u'giganta': u'히간타',
            u'coquito': u'코키토',
            u'gato': u'가토',
        })

    def test_4th(self):
        """제4항: x
        x가 모음 앞에 오되 어두일 때에는 'ㅅ'으로 적고, 어중일 때에는
        'ㄱㅅ'으로 적는다.
        """
        self.assert_examples({
            u'xilofono': u'실로포노',
            u'laxante': u'락산테',
        })

    def test_5th(self):
        """제5항: l
        어말 또는 자음 앞의 l은 받침 'ㄹ'로 적고, 어중의 1이 모음 앞에 올
        때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            u'ocal': u'오칼',
            u'colcren': u'콜크렌',
            u'blandon': u'블란돈',
            u'Cecilia': u'세실리아',
        })

    def test_6th(self):
        """제6항: nc, ng
        c와 g 앞에 오는 n은 받침 'ㅇ'으로 적는다.
        """
        self.assert_examples({
            u'blanco': u'블랑코',
            u'yungla': u'융글라',
        })

    def test_hangulize(self):
        self.assert_examples({
            u'ñoñez': u'뇨녜스',
            u'güerrero': u'궤레로',
            u'Güicho': u'귀초',
            u'Gamiño': u'가미뇨',
            u'Ángeles': u'앙헬레스',
            u'José Ortega y Gasset': u'호세 오르테가 이 가세트',
        })
# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class PolishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0208.jsp """

    def setUp(self):
        from hangulize.langs.pl import Polish
        self.lang = Polish()

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'자메크' == self.hangulize(u'zamek')
        assert u'모크리' == self.hangulize(u'mokry')
        assert u'스웁스크' == self.hangulize(u'Słupsk')

    def test_2nd(self):
        """제2항: b, d, g
        1. 어말에 올 때에는 '프', '트', '크'로 적는다.
        2. 유성 자음 앞에서는 '브', '드', '그'로 적는다.
        3. 무성 자음 앞에서 b, g는 받침으로 적고, d는 '트'로 적는다.
        """
        assert u'오트' == self.hangulize(u'od')
        assert u'즈브로드니아' == self.hangulize(u'zbrodnia')
        assert u'그랍스키' == self.hangulize(u'Grabski')
        assert u'오트피스' == self.hangulize(u'odpis')

    def test_3rd(self):
        """제3항: w, z, ź, dz, ż, rz, sz
        1. w, z, ź, dz가 무성 자음 앞이나 어말에 올 때에는 '프, 스, 시, 츠'로
           적는다.
        2. ż와 rz는 모음 앞에 올 때에는 'ㅈ'으로 적되, 앞의 자음이 무성
           자음일 때에는 '시'로 적는다. 유성 자음 앞에 올 때에는 '주', 무성
           자음 앞에 올 때에는 '슈', 어말에 올 때에는 '시'로 적는다.
        3. sz는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        assert u'자바프카' == self.hangulize(u'zabawka')
        assert u'오브라스' == self.hangulize(u'obraz')
        assert u'제슈프' == self.hangulize(u'Rzeszów')
        assert u'프셰미실' == self.hangulize(u'Przemyśl')
        assert u'그주모트' == self.hangulize(u'grzmot')
        assert u'우슈코' == self.hangulize(u'łóżko')
        assert u'펭헤시' == self.hangulize(u'pęcherz')
        assert u'코슈트' == self.hangulize(u'koszt')
        assert u'코시' == self.hangulize(u'kosz')

    def test_4th(self):
        """제4항: ł
        1. ł는 뒤따르는 모음과 결합할 때 합쳐서 적는다. (ło는 '워'로 적는다.)
           다만, 자음 뒤에 올 때에는 두 음절로 갈라 적는다.
        2. oł는 '우'로 적는다.
        """
        assert u'워노' == self.hangulize(u'łono')
        assert u'그워바' == self.hangulize(u'głowa')
        assert u'프시야치우' == self.hangulize(u'przyjaciół')

    def test_5th(self):
        """제5항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        assert u'올레이' == self.hangulize(u'olej')

    def test_6th(self):
        """제6항: m
        어두의 m이 l, r 앞에 올 때에는 '으'를 붙여 적는다.
        """
        assert u'믈레코' == self.hangulize(u'mleko')
        assert u'므루프카' == self.hangulize(u'mrówka')

    def test_7th(self):
        """제7항: ę
        ę은 '엥'으로 적는다. 다만, 어말의 ę는 '에'로 적는다.
        """
        assert u'렝카' == self.hangulize(u'ręka')
        assert u'프로셰' == self.hangulize(u'proszę')

    def test_8th(self):
        """제8항
        'ㅈ', 'ㅊ'으로 표기되는 자음(c, z) 뒤의 이중 모음은 단모음으로 적는다.
        """
        assert u'스타차' == self.hangulize(u'stacja')
        assert u'프리제르' == self.hangulize(u'fryzjer')

    def test_etc(self):
        assert u'프시아치우' == self.hangulize(u'przjyaciół')


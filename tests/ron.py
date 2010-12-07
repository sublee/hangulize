# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ron import Romanian


class RomanianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0211.jsp """

    lang = Romanian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0109.jsp """
        assert u'비블리오테커' == self.hangulize(u'bibliotecă')
        assert u'알브' == self.hangulize(u'alb')
        assert u'큰테크' == self.hangulize(u'Cîntec')
        assert u'치네' == self.hangulize(u'Cine')
        assert u'팍투러' == self.hangulize(u'factură')
        assert u'몰도바' == self.hangulize(u'Moldova')
        assert u'브라드' == self.hangulize(u'Brad')
        assert u'폭샤니' == self.hangulize(u'Focşani')
        assert u'카르토프' == self.hangulize(u'Cartof')
        assert u'갈라치' == self.hangulize(u'Galaţi')
        assert u'지젤' == self.hangulize(u'Gigel')
        assert u'헤린그' == self.hangulize(u'hering')
        assert u'하체그' == self.hangulize(u'haţeg')
        assert u'두흐' == self.hangulize(u'duh')
        assert u'지우' == self.hangulize(u'Jiu')
        assert u'클루지' == self.hangulize(u'Cluj')
        assert u'킬로그람' == self.hangulize(u'kilogram')
        assert u'비블리오테커' == self.hangulize(u'bibliotecă')
        assert u'호텔' == self.hangulize(u'hotel')
        assert u'마라무레슈' == self.hangulize(u'Maramureş')
        assert u'아브람' == self.hangulize(u'Avram')
        assert u'누체트' == self.hangulize(u'Nucet')
        assert u'브란' == self.hangulize(u'Bran')
        assert u'품느' == self.hangulize(u'pumn')
        assert u'피아니스트' == self.hangulize(u'pianist')
        assert u'셉템브리에' == self.hangulize(u'septembrie')
        assert u'카프' == self.hangulize(u'cap')
        assert u'라디오' == self.hangulize(u'radio')
        assert u'도르' == self.hangulize(u'dor')
        assert u'시비우' == self.hangulize(u'Sibiu')
        assert u'파스' == self.hangulize(u'pas')
        assert u'샤그' == self.hangulize(u'şag')
        assert u'무레슈' == self.hangulize(u'Mureş')
        assert u'텔레포니스트' == self.hangulize(u'telefonist')
        assert u'빌레트' == self.hangulize(u'bilet')
        assert u'치가러' == self.hangulize(u'ţigară')
        assert u'브라츠' == self.hangulize(u'braţ')
        assert u'빅토리아' == self.hangulize(u'Victoria')
        assert u'브라쇼브' == self.hangulize(u'Braşov')
        assert u'탁시' == self.hangulize(u'taxi')
        assert u'에그자멘' == self.hangulize(u'examen')
        assert u'지아르' == self.hangulize(u'ziar')
        assert u'아우토부즈' == self.hangulize(u'autobuz')
        assert u'케이아' == self.hangulize(u'Cheia')
        assert u'게오르게' == self.hangulize(u'Gheorghe')
        assert u'아라드' == self.hangulize(u'Arad')
        assert u'바커우' == self.hangulize(u'Bacău')
        assert u'엘레나' == self.hangulize(u'Elena')
        assert u'피아니스트' == self.hangulize(u'pianist')
        assert u'큼피나' == self.hangulize(u'Cîmpina')
        assert u'로므니아' == self.hangulize(u'România')
        assert u'오라데아' == self.hangulize(u'Oradea')
        assert u'누체트' == self.hangulize(u'Nucet')
    
    def test_1st(self):
        """제1항: c, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'카프' == self.hangulize(u'cap')
        assert u'큰테크' == self.hangulize(u'Cîntec')
        assert u'팍투러' == self.hangulize(u'factură')
        assert u'셉템브리에' == self.hangulize(u'septembrie')

    def test_2nd(self):
        """제2항: c, g
        c, g는 e, i 앞에서는 각각 'ㅊ', 'ㅈ'으로, 그 밖의 모음 앞에서는 'ㅋ',
        'ㄱ'으로 적는다.
        """
        assert u'카프' == self.hangulize(u'cap')
        assert u'첸트루' == self.hangulize(u'centru')
        assert u'갈라치' == self.hangulize(u'Galaţi')
        assert u'지젤' == self.hangulize(u'Gigel')

    def test_3rd(self):
        """제3항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        assert u'클레이' == self.hangulize(u'clei')

    def test_4th(self):
        """제4항: n
        n이 어말에서 m 뒤에 올 때는 '으'를 붙여 적는다.
        """
        assert u'렘느' == self.hangulize(u'lemn')
        assert u'품느' == self.hangulize(u'pumn')

    def test_5th(self):
        """제5항: e
        e는 '에'로 적되, 인칭 대명사 및 동사 este, era 등의 어두 모음 e는
        '예'로 적는다.
        """
        assert u'에밀' == self.hangulize(u'Emil')
        assert u'예우' == self.hangulize(u'eu')
        assert u'옐' == self.hangulize(u'el')
        assert u'예스테' == self.hangulize(u'este')
        assert u'예라' == self.hangulize(u'era')

    def test_etc(self):
        assert u'스투르자' == self.hangulize(u'Sturdza')
        assert u'테오도르' == self.hangulize(u'Theodor')


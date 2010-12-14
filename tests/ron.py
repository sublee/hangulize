# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ron import Romanian


class RomanianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0211.jsp """

    lang = Romanian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0109.jsp """
        self.assert_examples({
            u'bibliotecă': u'비블리오테커',
            u'alb': u'알브',
            u'Cîntec': u'큰테크',
            u'Cine': u'치네',
            u'factură': u'팍투러',
            u'Moldova': u'몰도바',
            u'Brad': u'브라드',
            u'Focşani': u'폭샤니',
            u'Cartof': u'카르토프',
            u'Galaţi': u'갈라치',
            u'Gigel': u'지젤',
            u'hering': u'헤린그',
            u'haţeg': u'하체그',
            u'duh': u'두흐',
            u'Jiu': u'지우',
            u'Cluj': u'클루지',
            u'kilogram': u'킬로그람',
            u'bibliotecă': u'비블리오테커',
            u'hotel': u'호텔',
            u'Maramureş': u'마라무레슈',
            u'Avram': u'아브람',
            u'Nucet': u'누체트',
            u'Bran': u'브란',
            u'pumn': u'품느',
            u'pianist': u'피아니스트',
            u'septembrie': u'셉템브리에',
            u'cap': u'카프',
            u'radio': u'라디오',
            u'dor': u'도르',
            u'Sibiu': u'시비우',
            u'pas': u'파스',
            u'şag': u'샤그',
            u'Mureş': u'무레슈',
            u'telefonist': u'텔레포니스트',
            u'bilet': u'빌레트',
            u'ţigară': u'치가러',
            u'braţ': u'브라츠',
            u'Victoria': u'빅토리아',
            u'Braşov': u'브라쇼브',
            u'taxi': u'탁시',
            u'examen': u'에그자멘',
            u'ziar': u'지아르',
            u'autobuz': u'아우토부즈',
            u'Cheia': u'케이아',
            u'Gheorghe': u'게오르게',
            u'Arad': u'아라드',
            u'Bacău': u'바커우',
            u'Elena': u'엘레나',
            u'pianist': u'피아니스트',
            u'Cîmpina': u'큼피나',
            u'România': u'로므니아',
            u'Oradea': u'오라데아',
            u'Nucet': u'누체트',
        })

    def test_1st(self):
        """제1항: c, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            u'cap': u'카프',
            u'Cîntec': u'큰테크',
            u'factură': u'팍투러',
            u'septembrie': u'셉템브리에',
        })

    def test_2nd(self):
        """제2항: c, g
        c, g는 e, i 앞에서는 각각 'ㅊ', 'ㅈ'으로, 그 밖의 모음 앞에서는 'ㅋ',
        'ㄱ'으로 적는다.
        """
        self.assert_examples({
            u'cap': u'카프',
            u'centru': u'첸트루',
            u'Galaţi': u'갈라치',
            u'Gigel': u'지젤',
        })

    def test_3rd(self):
        """제3항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            u'clei': u'클레이',
        })

    def test_4th(self):
        """제4항: n
        n이 어말에서 m 뒤에 올 때는 '으'를 붙여 적는다.
        """
        self.assert_examples({
            u'lemn': u'렘느',
            u'pumn': u'품느',
        })

    def test_5th(self):
        """제5항: e
        e는 '에'로 적되, 인칭 대명사 및 동사 este, era 등의 어두 모음 e는
        '예'로 적는다.
        """
        self.assert_examples({
            u'Emil': u'에밀',
            u'eu': u'예우',
            u'el': u'옐',
            u'este': u'예스테',
            u'era': u'예라',
        })

    def test_etc(self):
        self.assert_examples({
            u'Sturdza': u'스투르자',
            u'Theodor': u'테오도르',
        })
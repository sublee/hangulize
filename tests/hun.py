# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.hun import Hungarian


class HungarianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0212.jsp """

    lang = Hungarian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0110.jsp """
        self.assert_examples({
            u'bab': u'버브',
            u'ablak': u'어블러크',
            u'citrom': u'치트롬',
            u'nyolcvan': u'뇰츠번',
            u'arc': u'어르츠',
            u'csavar': u'처버르',
            u'kulcs': u'쿨치',
            u'daru': u'더루',
            u'medve': u'메드베',
            u'gond': u'곤드',
            u'dzsem': u'젬',
            u'elfog': u'엘포그',
            u'gumi': u'구미',
            u'nyugta': u'뉴그터',
            u'csomag': u'초머그',
            u'gyár': u'자르',
            u'hagyma': u'허지머',
            u'nagy': u'너지',
            u'hal': u'헐',
            u'juh': u'유흐',
            u'béka': u'베커',
            u'keksz': u'켁스',
            u'szék': u'세크',
            u'len': u'렌',
            u'meleg': u'멜레그',
            u'dél': u'델',
            u'málna': u'말너',
            u'bomba': u'봄버',
            u'álom': u'알롬',
            u'néma': u'네머',
            u'bunda': u'분더',
            u'pihen': u'피헨',
            u'nyak': u'녀크',
            u'hányszor': u'하니소르',
            u'irány': u'이라니',
            u'árpa': u'아르퍼',
            u'csipke': u'칩케',
            u'hónap': u'호너프',
            u'róka': u'로커',
            u'barna': u'버르너',
            u'ár': u'아르',
            u'sál': u'샬',
            u'puska': u'푸슈커',
            u'aratás': u'어러타시',
            u'alszik': u'얼시크',
            u'asztal': u'어스털',
            u'húsz': u'후스',
            u'ajto': u'어이토',
            u'borotva': u'보로트버',
            u'csont': u'촌트',
            u'atya': u'어처',
            u'vesz': u'베스',
            u'évszázad': u'에브사저드',
            u'enyv': u'에니브',
            u'zab': u'저브',
            u'kezd': u'케즈드',
            u'blúz': u'블루즈',
            u'zsák': u'자크',
            u'tőzsde': u'퇴주데',
            u'rozs': u'로주',
            u'ajak': u'어여크',
            u'fej': u'페이',
            u'január': u'여누아르',
            u'lyuk': u'유크',
            u'mélység': u'메이셰그',
            u'király': u'키라이',
            u'lakat': u'러커트',
            u'máj': u'마이',
            u'mert': u'메르트',
            u'mész': u'메스',
            u'isten': u'이슈텐',
            u'sí': u'시',
            u'torna': u'토르너',
            u'róka': u'로커',
            u'sör': u'쇠르',
            u'nő': u'뇌',
            u'bunda': u'분더',
            u'hús': u'후시',
            u'füst': u'퓌슈트',
            u'fű': u'퓌',
        })

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            u'ablak': u'어블러크',
            u'csipke': u'칩케',
        })

    def test_2nd(self):
        """제2항
        bb, cc, dd, ff, gg, ggy, kk, ll, lly, nn, nny, pp, rr, ss, ssz, tt,
        tty는 b, c, d, f, g, gy, k, l, ly, n, ny, p, r, s, sz, t, ty와 같이
        적는다. 다만, 어중의 nn, nny와 모음 앞의 ll은 'ㄴㄴ', 'ㄴ니',
        'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            u'között': u'쾨죄트',
            u'dinnye': u'딘네',
            u'nulla': u'눌러',
        })

    def test_3rd(self):
        """제3항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            u'olaj': u'올러이',
        })

    def test_4th(self):
        """제4항: s
        s는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        self.assert_examples({
            u'Pest': u'페슈트',
            u'lapos': u'러포시',
        })

    def test_5th(self):
        """제5항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        self.assert_examples({
            u'nyer': u'네르',
            u'selyem': u'셰옘',
        })
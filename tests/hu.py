# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.hu import Hungarian


class HungarianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0212.jsp """

    lang = Hungarian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0110.jsp """
        assert u'버브' == self.hangulize(u'bab')
        assert u'어블러크' == self.hangulize(u'ablak')
        assert u'치트롬' == self.hangulize(u'citrom')
        assert u'뇰츠번' == self.hangulize(u'nyolcvan')
        assert u'어르츠' == self.hangulize(u'arc')
        assert u'처버르' == self.hangulize(u'csavar')
        assert u'쿨치' == self.hangulize(u'kulcs')
        assert u'더루' == self.hangulize(u'daru')
        assert u'메드베' == self.hangulize(u'medve')
        assert u'곤드' == self.hangulize(u'gond')
        assert u'젬' == self.hangulize(u'dzsem')
        assert u'엘포그' == self.hangulize(u'elfog')
        assert u'구미' == self.hangulize(u'gumi')
        assert u'뉴그터' == self.hangulize(u'nyugta')
        assert u'초머그' == self.hangulize(u'csomag')
        assert u'자르' == self.hangulize(u'gyár')
        assert u'허지머' == self.hangulize(u'hagyma')
        assert u'너지' == self.hangulize(u'nagy')
        assert u'헐' == self.hangulize(u'hal')
        assert u'유흐' == self.hangulize(u'juh')
        assert u'베커' == self.hangulize(u'béka')
        assert u'켁스' == self.hangulize(u'keksz')
        assert u'세크' == self.hangulize(u'szék')
        assert u'렌' == self.hangulize(u'len')
        assert u'멜레그' == self.hangulize(u'meleg')
        assert u'델' == self.hangulize(u'dél')
        assert u'말너' == self.hangulize(u'málna')
        assert u'봄버' == self.hangulize(u'bomba')
        assert u'알롬' == self.hangulize(u'álom')
        assert u'네머' == self.hangulize(u'néma')
        assert u'분더' == self.hangulize(u'bunda')
        assert u'피헨' == self.hangulize(u'pihen')
        assert u'녀크' == self.hangulize(u'nyak')
        assert u'하니소르' == self.hangulize(u'hányszor')
        assert u'이라니' == self.hangulize(u'irány')
        assert u'아르퍼' == self.hangulize(u'árpa')
        assert u'칩케' == self.hangulize(u'csipke')
        assert u'호너프' == self.hangulize(u'hónap')
        assert u'로커' == self.hangulize(u'róka')
        assert u'버르너' == self.hangulize(u'barna')
        assert u'아르' == self.hangulize(u'ár')
        assert u'샬' == self.hangulize(u'sál')
        assert u'푸슈커' == self.hangulize(u'puska')
        assert u'어러타시' == self.hangulize(u'aratás')
        assert u'얼시크' == self.hangulize(u'alszik')
        assert u'어스털' == self.hangulize(u'asztal')
        assert u'후스' == self.hangulize(u'húsz')
        assert u'어이토' == self.hangulize(u'ajto')
        assert u'보로트버' == self.hangulize(u'borotva')
        assert u'촌트' == self.hangulize(u'csont')
        assert u'어처' == self.hangulize(u'atya')
        assert u'베스' == self.hangulize(u'vesz')
        assert u'에브사저드' == self.hangulize(u'évszázad')
        assert u'에니브' == self.hangulize(u'enyv')
        assert u'저브' == self.hangulize(u'zab')
        assert u'케즈드' == self.hangulize(u'kezd')
        assert u'블루즈' == self.hangulize(u'blúz')
        assert u'자크' == self.hangulize(u'zsák')
        assert u'퇴주데' == self.hangulize(u'tőzsde')
        assert u'로주' == self.hangulize(u'rozs')
        assert u'어여크' == self.hangulize(u'ajak')
        assert u'페이' == self.hangulize(u'fej')
        assert u'여누아르' == self.hangulize(u'január')
        assert u'유크' == self.hangulize(u'lyuk')
        assert u'메이셰그' == self.hangulize(u'mélység')
        assert u'키라이' == self.hangulize(u'király')
        assert u'러커트' == self.hangulize(u'lakat')
        assert u'마이' == self.hangulize(u'máj')
        assert u'메르트' == self.hangulize(u'mert')
        assert u'메스' == self.hangulize(u'mész')
        assert u'이슈텐' == self.hangulize(u'isten')
        assert u'시' == self.hangulize(u'sí')
        assert u'토르너' == self.hangulize(u'torna')
        assert u'로커' == self.hangulize(u'róka')
        assert u'쇠르' == self.hangulize(u'sör')
        assert u'뇌' == self.hangulize(u'nő')
        assert u'분더' == self.hangulize(u'bunda')
        assert u'후시' == self.hangulize(u'hús')
        assert u'퓌슈트' == self.hangulize(u'füst')
        assert u'퓌' == self.hangulize(u'fű')
    
    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'어블러크' == self.hangulize(u'ablak')
        assert u'칩케' == self.hangulize(u'csipke')

    def test_2nd(self):
        """제2항
        bb, cc, dd, ff, gg, ggy, kk, ll, lly, nn, nny, pp, rr, ss, ssz, tt,
        tty는 b, c, d, f, g, gy, k, l, ly, n, ny, p, r, s, sz, t, ty와 같이
        적는다. 다만, 어중의 nn, nny와 모음 앞의 ll은 'ㄴㄴ', 'ㄴ니',
        'ㄹㄹ'로 적는다.
        """
        assert u'쾨죄트' == self.hangulize(u'között')
        assert u'딘네' == self.hangulize(u'dinnye')
        assert u'눌러' == self.hangulize(u'nulla')

    def test_3rd(self):
        """제3항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        assert u'올러이' == self.hangulize(u'olaj')

    def test_4th(self):
        """제4항: s
        s는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        assert u'페슈트' == self.hangulize(u'Pest')
        assert u'러포시' == self.hangulize(u'lapos')

    def test_5th(self):
        """제5항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        assert u'네르' == self.hangulize(u'nyer')
        assert u'셰옘' == self.hangulize(u'selyem')

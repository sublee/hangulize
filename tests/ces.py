# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ces import Czech


class CzechTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0209.jsp """

    lang = Czech()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0107.jsp """
        assert u'바르바' == self.hangulize(u'barva')
        assert u'옵호트' == self.hangulize(u'obchod')
        assert u'도브리' == self.hangulize(u'dobrý')
        assert u'예르자프' == self.hangulize(u'jeřab')
        assert u'치가레타' == self.hangulize(u'cigareta')
        assert u'네모츠니체' == self.hangulize(u'nemocnice')
        assert u'네모츠' == self.hangulize(u'nemoc')
        assert u'차페크' == self.hangulize(u'čapek')
        assert u'쿨레치니크' == self.hangulize(u'kulečnik')
        assert u'미치' == self.hangulize(u'míč')
        assert u'데흐' == self.hangulize(u'dech')
        assert u'디바들로' == self.hangulize(u'divadlo')
        assert u'레트' == self.hangulize(u'led')
        assert u'댜벨' == self.hangulize(u"ďábel")
        assert u'로티카' == self.hangulize(u"loďka")
        assert u'흐루티' == self.hangulize(u"hruď")
        assert u'피크' == self.hangulize(u'fík')
        assert u'크노플리크' == self.hangulize(u'knoflík')
        assert u'그라모폰' == self.hangulize(u'gramofon')
        assert u'하드르' == self.hangulize(u'hadr')
        assert u'흐미스' == self.hangulize(u'hmyz')
        assert u'부흐' == self.hangulize(u'bůh')
        assert u'호디티' == self.hangulize(u'choditi')
        assert u'흘라페츠' == self.hangulize(u'chlapec')
        assert u'프라흐' == self.hangulize(u'prach')
        assert u'카흐나' == self.hangulize(u'kachna')
        assert u'니크디' == self.hangulize(u'nikdy')
        assert u'파다크' == self.hangulize(u'padák')
        assert u'레프' == self.hangulize(u'lev')
        assert u'슈플하티' == self.hangulize(u'šplhati')
        assert u'포스텔' == self.hangulize(u'postel')
        assert u'모스트' == self.hangulize(u'most')
        assert u'므라크' == self.hangulize(u'mrak')
        assert u'포드짐' == self.hangulize(u'podzim')
        assert u'노하' == self.hangulize(u'noha')
        assert u'포드민카' == self.hangulize(u'podmínka')
        assert u'네미' == self.hangulize(u'němý')
        assert u'산키' == self.hangulize(u'sáňky')
        assert u'플젠' == self.hangulize(u'Plzeň')
        assert u'프라하' == self.hangulize(u'Praha')
        assert u'코롭테프' == self.hangulize(u'koroptev')
        assert u'스트로프' == self.hangulize(u'strop')
        assert u'크바시' == self.hangulize(u'quasi')
        assert u'루카' == self.hangulize(u'ruka')
        assert u'하르모니카' == self.hangulize(u'harmonika')
        assert u'미르' == self.hangulize(u'mír')
        assert u'르제카' == self.hangulize(u'řeka')
        assert u'나모르주니크' == self.hangulize(u'námořník')
        assert u'호르슈키' == self.hangulize(u'hořký')
        assert u'코우르시' == self.hangulize(u'kouř')
        assert u'세들로' == self.hangulize(u'sedlo')
        assert u'마슬로' == self.hangulize(u'máslo')
        assert u'노스' == self.hangulize(u'nos')
        assert u'샤티' == self.hangulize(u'šaty')
        assert u'슈테른베르크' == self.hangulize(u'šternberk')
        assert u'코시' == self.hangulize(u'koš')
        assert u'탐' == self.hangulize(u'tam')
        assert u'마트카' == self.hangulize(u'matka')
        assert u'볼레스트' == self.hangulize(u'bolest')
        assert u'텔로' == self.hangulize(u'tělo')
        assert u'슈테스티' == self.hangulize(u'štěstí')
        assert u'오베티' == self.hangulize(u"oběť")
        assert u'비소키' == self.hangulize(u'vysoký')
        assert u'크니호브나' == self.hangulize(u'knihovna')
        assert u'코프' == self.hangulize(u'kov')
        assert u'제록스' == self.hangulize(u'xerox')
        assert u'삭소폰' == self.hangulize(u'saxofón')
        assert u'자메크' == self.hangulize(u'zámek')
        assert u'포즈드니' == self.hangulize(u'pozdní')
        assert u'베스' == self.hangulize(u'bez')
        assert u'지슈카' == self.hangulize(u'žižka')
        assert u'주베르지나' == self.hangulize(u'žvěřina')
        assert u'브로시' == self.hangulize(u'Brož')
        assert u'야로' == self.hangulize(u'jaro')
        assert u'포코이' == self.hangulize(u'pokoj')
        assert u'발리크' == self.hangulize(u'balík')
        assert u'코마르' == self.hangulize(u'komár')
        assert u'데흐' == self.hangulize(u'dech')
        assert u'레토' == self.hangulize(u'léto')
        assert u'셰스트' == self.hangulize(u'šest')
        assert u'베크' == self.hangulize(u'věk')
        assert u'키노' == self.hangulize(u'kino')
        assert u'미라' == self.hangulize(u'míra')
        assert u'오베츠' == self.hangulize(u'obec')
        assert u'네르보즈니' == self.hangulize(u'nervózni')
        assert u'부벤' == self.hangulize(u'buben')
        assert u'우로크' == self.hangulize(u'úrok')
        assert u'둠' == self.hangulize(u'dům')
        assert u'야지크' == self.hangulize(u'jazýk')
        assert u'리니' == self.hangulize(u'líný')

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'모제크' == self.hangulize(u'mozek')
        assert u'코롭테프' == self.hangulize(u'koroptev')

    def test_2nd(self):
        """제2항: b, d, d', g
        1. 어말에 올 때에는 '프', '트', '티', '크'로 적는다.
        2. 유성 자음 앞에서는 '브', '드', '디', '그'로 적는다.
        3. 무성 자음 앞에서 b, g는 받침으로 적고, d, d'는 '트', '티'로 적는다.
        """
        assert u'레트' == self.hangulize(u'led')
        assert u'레드비나' == self.hangulize(u'ledvina')
        assert u'옵호트' == self.hangulize(u'obchod')
        assert u'오트파트키' == self.hangulize(u'odpadky')

    def test_3nd(self):
        """제3항: v, w, z, ř, ž, š
        1. v, w, z가 무성 자음 앞이나 어말에 올 때에는 '프, 프, 스'로 적는다.
        2. ř, ž가 유성 자음 앞에 올 때에는 '르주', '주', 무성 자음 앞에 올
           때에는 '르슈', '슈', 어말에 올 때에는 '르시', '시'로 적는다.
        3. š는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        assert u'흐미스' == self.hangulize(u'hmyz')
        assert u'나모르주니크' == self.hangulize(u'námořník')
        assert u'호르슈키' == self.hangulize(u'hořký')
        assert u'코우르시' == self.hangulize(u'kouř')
        assert u'푸슈카' == self.hangulize(u'puška')
        assert u'미시' == self.hangulize(u'myš')

    def test_4th(self):
        """제4항: l, lj
        어중의 l, lj가 모음 앞에 올 때에는 'ㄹㄹ', 'ㄹ리'로 적는다.
        """
        assert u'콜로' == self.hangulize(u'kolo')

    def test_5th(self):
        """제5항: m
        m이 r 앞에 올 때에는 '으'를 붙여 적는다.
        """
        assert u'후므르' == self.hangulize(u'humr')

    def test_6th(self):
        """제6항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        assert u'베크' == self.hangulize(u'věk')
        assert u'셰스트' == self.hangulize(u'šest')

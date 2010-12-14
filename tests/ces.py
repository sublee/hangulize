# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ces import Czech


class CzechTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0209.jsp """

    lang = Czech()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0107.jsp """
        self.assert_examples({
            u'barva': u'바르바',
            u'obchod': u'옵호트',
            u'dobrý': u'도브리',
            u'jeřab': u'예르자프',
            u'cigareta': u'치가레타',
            u'nemocnice': u'네모츠니체',
            u'nemoc': u'네모츠',
            u'čapek': u'차페크',
            u'kulečnik': u'쿨레치니크',
            u'míč': u'미치',
            u'dech': u'데흐',
            u'divadlo': u'디바들로',
            u'led': u'레트',
            u"ďábel": u'댜벨',
            u"loďka": u'로티카',
            u"hruď": u'흐루티',
            u'fík': u'피크',
            u'knoflík': u'크노플리크',
            u'gramofon': u'그라모폰',
            u'hadr': u'하드르',
            u'hmyz': u'흐미스',
            u'bůh': u'부흐',
            u'choditi': u'호디티',
            u'chlapec': u'흘라페츠',
            u'prach': u'프라흐',
            u'kachna': u'카흐나',
            u'nikdy': u'니크디',
            u'padák': u'파다크',
            u'lev': u'레프',
            u'šplhati': u'슈플하티',
            u'postel': u'포스텔',
            u'most': u'모스트',
            u'mrak': u'므라크',
            u'podzim': u'포드짐',
            u'noha': u'노하',
            u'podmínka': u'포드민카',
            u'němý': u'네미',
            u'sáňky': u'산키',
            u'Plzeň': u'플젠',
            u'Praha': u'프라하',
            u'koroptev': u'코롭테프',
            u'strop': u'스트로프',
            u'quasi': u'크바시',
            u'ruka': u'루카',
            u'harmonika': u'하르모니카',
            u'mír': u'미르',
            u'řeka': u'르제카',
            u'námořník': u'나모르주니크',
            u'hořký': u'호르슈키',
            u'kouř': u'코우르시',
            u'sedlo': u'세들로',
            u'máslo': u'마슬로',
            u'nos': u'노스',
            u'šaty': u'샤티',
            u'šternberk': u'슈테른베르크',
            u'koš': u'코시',
            u'tam': u'탐',
            u'matka': u'마트카',
            u'bolest': u'볼레스트',
            u'tělo': u'텔로',
            u'štěstí': u'슈테스티',
            u"oběť": u'오베티',
            u'vysoký': u'비소키',
            u'knihovna': u'크니호브나',
            u'kov': u'코프',
            u'xerox': u'제록스',
            u'saxofón': u'삭소폰',
            u'zámek': u'자메크',
            u'pozdní': u'포즈드니',
            u'bez': u'베스',
            u'žižka': u'지슈카',
            u'žvěřina': u'주베르지나',
            u'Brož': u'브로시',
            u'jaro': u'야로',
            u'pokoj': u'포코이',
            u'balík': u'발리크',
            u'komár': u'코마르',
            u'dech': u'데흐',
            u'léto': u'레토',
            u'šest': u'셰스트',
            u'věk': u'베크',
            u'kino': u'키노',
            u'míra': u'미라',
            u'obec': u'오베츠',
            u'nervózni': u'네르보즈니',
            u'buben': u'부벤',
            u'úrok': u'우로크',
            u'dům': u'둠',
            u'jazýk': u'야지크',
            u'líný': u'리니',
        })

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            u'mozek': u'모제크',
            u'koroptev': u'코롭테프',
        })

    def test_2nd(self):
        """제2항: b, d, d', g
        1. 어말에 올 때에는 '프', '트', '티', '크'로 적는다.
        2. 유성 자음 앞에서는 '브', '드', '디', '그'로 적는다.
        3. 무성 자음 앞에서 b, g는 받침으로 적고, d, d'는 '트', '티'로 적는다.
        """
        self.assert_examples({
            u'led': u'레트',
            u'ledvina': u'레드비나',
            u'obchod': u'옵호트',
            u'odpadky': u'오트파트키',
        })

    def test_3nd(self):
        """제3항: v, w, z, ř, ž, š
        1. v, w, z가 무성 자음 앞이나 어말에 올 때에는 '프, 프, 스'로 적는다.
        2. ř, ž가 유성 자음 앞에 올 때에는 '르주', '주', 무성 자음 앞에 올
           때에는 '르슈', '슈', 어말에 올 때에는 '르시', '시'로 적는다.
        3. š는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        self.assert_examples({
            u'hmyz': u'흐미스',
            u'námořník': u'나모르주니크',
            u'hořký': u'호르슈키',
            u'kouř': u'코우르시',
            u'puška': u'푸슈카',
            u'myš': u'미시',
        })

    def test_4th(self):
        """제4항: l, lj
        어중의 l, lj가 모음 앞에 올 때에는 'ㄹㄹ', 'ㄹ리'로 적는다.
        """
        self.assert_examples({
            u'kolo': u'콜로',
        })

    def test_5th(self):
        """제5항: m
        m이 r 앞에 올 때에는 '으'를 붙여 적는다.
        """
        self.assert_examples({
            u'humr': u'후므르',
        })

    def test_6th(self):
        """제6항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        self.assert_examples({
            u'věk': u'베크',
            u'šest': u'셰스트',
        })
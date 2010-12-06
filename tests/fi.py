# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.fi import Finnish


class FinnishTestCase(HangulizeTestCase):

    lang = Finnish()

    def test_people(self):
        assert u'알바르 알토' == self.hangulize(u'Alvar Aalto')
        assert u'유하니 아호' == self.hangulize(u'Juhani Aho')
        assert u'마르티 아흐티사리' == self.hangulize(u'Martti Ahtisaari')
        assert u'악셀리 갈렌칼렐라' == self.hangulize(u'Akseli Gallen-Kallela')
        assert u'베이코 하쿨리넨' == self.hangulize(u'Veikko Hakulinen')
        assert u'페카 할로넨' == self.hangulize(u'Pekka Halonen')
        assert u'타리아 할로넨' == self.hangulize(u'Tarja Halonen')
        assert u'사미 휘피애' == self.hangulize(u'Sami Hyypiä')
        assert u'미카 해키넨' == self.hangulize(u'Mika Häkkinen')
        assert u'유시 얘스켈래이넨' == self.hangulize(u'Jussi Jääskeläinen')
        assert u'아키 카우리스매키' == self.hangulize(u'Aki Kaurismäki')
        assert u'우르호 케코넨' == self.hangulize(u'Urho Kekkonen')
        assert u'미카 키프루소프' == self.hangulize(u'Miikka Kiprusoff')
        assert u'마리아리사 키르베스니에미' == \
               self.hangulize(u'Marja-Liisa Kirvesniemi')
        assert u'마우노 코이비스토' == self.hangulize(u'Mauno Koivisto')
        assert u'사쿠 코이부' == self.hangulize(u'Saku Koivu')
        assert u'한네스 콜레흐마이넨' == self.hangulize(u'Hannes Kolehmainen')
        assert u'야리 쿠리' == self.hangulize(u'Jari Kurri')
        assert u'야리 리트마넨' == self.hangulize(u'Jari Litmanen')
        assert u'에로 맨튀란타' == self.hangulize(u'Eero Mäntyranta')
        assert u'파보 누르미' == self.hangulize(u'Paavo Nurmi')
        assert u'빌레 리톨라' == self.hangulize(u'Ville Ritola')
        assert u'키미 래이쾨넨' == self.hangulize(u'Kimi Räikkönen')
        assert u'에로 사리넨' == self.hangulize(u'Eero Saarinen')
        assert u'테무 셀란네' == self.hangulize(u'Teemu Selanne')
        assert u'프란스 에밀 실란패' == self.hangulize(u'Frans Eemil Sillanpää')
        assert u'타리아 투루넨' == self.hangulize(u'Tarja Turunen')
        assert u'아르투리 일마리 비르타넨' == \
               self.hangulize(u'Artturi Ilmari Virtanen')
        assert u'위리외 배이샐래' == self.hangulize(u'Yrjö Väisälä')
        assert u'타피오 비르칼라' == self.hangulize(u'Tapio Wirkkala')

    def test_places(self):
        assert u'에스포' == self.hangulize(u'Espoo')
        assert u'헬싱키' == self.hangulize(u'Helsinki')
        assert u'요엔수' == self.hangulize(u'Joensuu')
        assert u'위배스퀼래' == self.hangulize(u'Jyväskylä')
        assert u'카야니' == self.hangulize(u'Kajaani')
        assert u'카리알라' == self.hangulize(u'Karjala')
        assert u'쿠오피오' == self.hangulize(u'Kuopio')
        assert u'라펜란타' == self.hangulize(u'Lappeenranta')
        assert u'미켈리' == self.hangulize(u'Mikkeli')
        assert u'노키아' == self.hangulize(u'Nokia')
        assert u'오울루' == self.hangulize(u'Oulu')
        assert u'로바니에미' == self.hangulize(u'Rovaniemi')
        assert u'사이마' == self.hangulize(u'Saimaa')
        assert u'사본린나' == self.hangulize(u'Savonlinna')
        assert u'수오멘린나' == self.hangulize(u'Suomenlinna')
        assert u'수오미' == self.hangulize(u'Suomi')
        assert u'탐페레' == self.hangulize(u'Tampere')
        assert u'타피올라' == self.hangulize(u'Tapiola')
        assert u'투르쿠' == self.hangulize(u'Turku')
        assert u'바사' == self.hangulize(u'Vaasa')
        assert u'반타' == self.hangulize(u'Vantaa')

    def test_mythology(self):
        assert u'아이노' == self.hangulize(u'Aino')
        assert u'일마리넨' == self.hangulize(u'Ilmarinen')
        assert u'요우카하이넨' == self.hangulize(u'Joukahainen')
        assert u'칼레발라' == self.hangulize(u'Kalevala')
        assert u'쿨레르보' == self.hangulize(u'Kullervo')
        assert u'렘밍캐이넨' == self.hangulize(u'Lemminkäinen')
        assert u'로우히' == self.hangulize(u'Louhi')
        assert u'마리아타' == self.hangulize(u'Marjatta')
        assert u'포흐욜라' == self.hangulize(u'Pohjola')
        assert u'삼포' == self.hangulize(u'Sampo')
        assert u'우코' == self.hangulize(u'Ukko')
        assert u'배이내뫼이넨' == self.hangulize(u'Väinämöinen')

    def test_miscellaneous(self):
        assert u'칸텔레' == self.hangulize(u'kantele')
        assert u'사우나' == self.hangulize(u'sauna')
        assert u'시수' == self.hangulize(u'sisu')

# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.fin import Finnish


class FinnishTestCase(HangulizeTestCase):

    lang = Finnish()

    def test_people(self):
        self.assert_examples({
            u'Alvar Aalto': u'알바르 알토',
            u'Juhani Aho': u'유하니 아호',
            u'Martti Ahtisaari': u'마르티 아흐티사리',
            u'Akseli Gallen-Kallela': u'악셀리 갈렌칼렐라',
            u'Veikko Hakulinen': u'베이코 하쿨리넨',
            u'Pekka Halonen': u'페카 할로넨',
            u'Tarja Halonen': u'타리아 할로넨',
            u'Sami Hyypiä': u'사미 휘피애',
            u'Mika Häkkinen': u'미카 해키넨',
            u'Jussi Jääskeläinen': u'유시 얘스켈래이넨',
            u'Aki Kaurismäki': u'아키 카우리스매키',
            u'Urho Kekkonen': u'우르호 케코넨',
            u'Miikka Kiprusoff': u'미카 키프루소프',
            u'Marja-Liisa Kirvesniemi': u'마리아리사 키르베스니에미',
            u'Mauno Koivisto': u'마우노 코이비스토',
            u'Saku Koivu': u'사쿠 코이부',
            u'Hannes Kolehmainen': u'한네스 콜레흐마이넨',
            u'Jari Kurri': u'야리 쿠리',
            u'Jari Litmanen': u'야리 리트마넨',
            u'Eero Mäntyranta': u'에로 맨튀란타',
            u'Paavo Nurmi': u'파보 누르미',
            u'Ville Ritola': u'빌레 리톨라',
            u'Kimi Räikkönen': u'키미 래이쾨넨',
            u'Eero Saarinen': u'에로 사리넨',
            u'Teemu Selanne': u'테무 셀란네',
            u'Frans Eemil Sillanpää': u'프란스 에밀 실란패',
            u'Tarja Turunen': u'타리아 투루넨',
            u'Artturi Ilmari Virtanen': u'아르투리 일마리 비르타넨',
            u'Yrjö Väisälä': u'위리외 배이샐래',
            u'Tapio Wirkkala': u'타피오 비르칼라',
        })

    def test_places(self):
        self.assert_examples({
            u'Espoo': u'에스포',
            u'Helsinki': u'헬싱키',
            u'Joensuu': u'요엔수',
            u'Jyväskylä': u'위배스퀼래',
            u'Kajaani': u'카야니',
            u'Karjala': u'카리알라',
            u'Kuopio': u'쿠오피오',
            u'Lappeenranta': u'라펜란타',
            u'Mikkeli': u'미켈리',
            u'Nokia': u'노키아',
            u'Oulu': u'오울루',
            u'Rovaniemi': u'로바니에미',
            u'Saimaa': u'사이마',
            u'Savonlinna': u'사본린나',
            u'Suomenlinna': u'수오멘린나',
            u'Suomi': u'수오미',
            u'Tampere': u'탐페레',
            u'Tapiola': u'타피올라',
            u'Turku': u'투르쿠',
            u'Vaasa': u'바사',
            u'Vantaa': u'반타',
        })

    def test_mythology(self):
        self.assert_examples({
            u'Aino': u'아이노',
            u'Ilmarinen': u'일마리넨',
            u'Joukahainen': u'요우카하이넨',
            u'Kalevala': u'칼레발라',
            u'Kullervo': u'쿨레르보',
            u'Lemminkäinen': u'렘밍캐이넨',
            u'Louhi': u'로우히',
            u'Marjatta': u'마리아타',
            u'Pohjola': u'포흐욜라',
            u'Sampo': u'삼포',
            u'Ukko': u'우코',
            u'Väinämöinen': u'배이내뫼이넨',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            u'kantele': u'칸텔레',
            u'sauna': u'사우나',
            u'sisu': u'시수',
        })
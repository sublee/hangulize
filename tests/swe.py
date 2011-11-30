# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.swe import Swedish


class SwedishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0213.jsp """

    lang = Swedish()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0111.jsp """
        self.assert_examples({
            u'bal': u'발',
            u'snabbt': u'스납트',
            u'Jacob': u'야코브',
            u'Carlsson': u'칼손',
            u'Celsius': u'셀시우스',
            u'Ericson': u'에릭손',
            u'charm': u'샤름',
            u'och': u'오크',
            u'dag': u'다그',
            u'dricka': u'드리카',
            u'Halmstad': u'할름스타드',
            u'Djurgården': u'유르고르덴',
            u'adjö': u'아예',
            u'Sundsvall': u'순스발',
            u'Falun': u'팔룬',
            u'luft': u'루프트',
            u'Gustav': u'구스타브',
            u'helgon': u'헬곤',
            u'Göteborg': u'예테보리',
            u'Geijer': u'예이예르',
            u'Gislaved': u'이슬라베드',
            u'älg': u'엘리',
            u'Strindberg': u'스트린드베리',
            u'Borg': u'보리',
            u'Magnus': u'망누스',
            u'Ragnar': u'랑나르',
            u'Agnes': u'앙네스',
            u'högst': u'획스트',
            u'Grönberg': u'그뢴베리',
            u'Gjerstad': u'예르스타드',
            u'Gjörwell': u'예르벨',
            u'Hälsingborg': u'헬싱보리',
            u'hyra': u'휘라',
            u'Dahl': u'달',
            u'Hjälmaren': u'옐마렌',
            u'Hjalmar': u'얄마르',
            u'Hjort': u'요르트',
            u'Jansson': u'얀손',
            u'Jönköping': u'옌셰핑',
            u'Johansson': u'요한손',
            u'börja': u'뵈리아',
            u'fjäril': u'피에릴',
            u'mjuk': u'미우크',
            u'mjöl': u'미엘',
            u'Karl': u'칼',
            u'Kock': u'코크',
            u'Kungsholm': u'쿵스홀름',
            u'Kerstin': u'셰르스틴',
            u'Norrköping': u'노르셰핑',
            u'Lysekil': u'뤼세실',
            u'oktober': u'옥토베르',
            u'Fredrik': u'프레드리크',
            u'kniv': u'크니브',
            u'vacker': u'바케르',
            u'Stockholm': u'스톡홀름',
            u'bock': u'보크',
            u'Kjell': u'셸',
            u'Kjula': u'슐라',
            u'Linköping': u'린셰핑',
            u'tala': u'탈라',
            u'tal': u'탈',
            u'Ljusnan': u'유스난',
            u'Södertälje': u'쇠데르텔리에',
            u'detalj': u'데탈리',
            u'Malmö': u'말뫼',
            u'samtal': u'삼탈',
            u'hummer': u'훔메르',
            u'Norrköping': u'노르셰핑',
            u'Vänern': u'베네른',
            u'land': u'란드',
            u'Karlshamn': u'칼스함',
            u'Borlänge': u'볼렝에',
            u'kung': u'쿵',
            u'lång': u'롱',
            u'anka': u'앙카',
            u'Sankt': u'상트',
            u'bank': u'방크',
            u'Piteå': u'피테오',
            u'knappt': u'크납트',
            u'Uppsala': u'웁살라',
            u'kamp': u'캄프',
            u'Malmqvist': u'말름크비스트',
            u'Lindqvist': u'린드크비스트',
            u'röd': u'뢰드',
            u'Wilander': u'빌란데르',
            u'Björk': u'비에르크',
            u'Erlander': u'엘란데르',
            u'Karlgren': u'칼그렌',
            u'Jarl': u'얄',
            u'sommar': u'솜마르',
            u'Storvik': u'스토르비크',
            u'dans': u'단스',
            u'Schack': u'샤크',
            u'Schein': u'셰인',
            u'revansch': u'레반슈',
            u'Nässjö': u'네셰',
            u'sjukhem': u'슈크헴',
            u'Sjöberg': u'셰베리',
            u'Skoglund': u'스코글룬드',
            u'Skellefteå': u'셸레프테오',
            u'Skövde': u'셰브데',
            u'Skeppsholmen': u'솁스홀멘',
            u'Hammarskjöld': u'함마르셸드',
            u'Skjöldebrand': u'셸데브란드',
            u'Stjärneborg': u'셰르네보리',
            u'Oxenstjerna': u'옥센셰르나',
            u'Göta': u'예타',
            u'Botkyrka': u'봇쉬르카',
            u'Trelleborg': u'트렐레보리',
            u'båt': u'보트',
            u'Luther': u'루테르',
            u'Thunberg': u'툰베리',
            u'lektion': u'렉숀',
            u'station': u'스타숀',
            u'tjeck': u'셰크',
            u'Tjåkkå': u'쇼코',
            u'tjäna': u'셰나',
            u'tjugo': u'슈고',
            u'Sverige': u'스베리예',
            u'Wasa': u'바사',
            u'Swedenborg': u'스베덴보리',
            u'Eslöv': u'에슬뢰브',
            u'Axel': u'악셀',
            u'Alexander': u'알렉산데르',
            u'sex': u'섹스',
            u'Zachris': u'사크리스',
            u'zon': u'손',
            u'Lorenzo': u'로렌소',
            u'Kalix': u'칼릭스',
            u'Falun': u'팔룬',
            u'Alvesta': u'알베스타',
            u'Enköping': u'엔셰핑',
            u'Svealand': u'스베알란드',
            u'Mälaren': u'멜라렌',
            u'Vänern': u'베네른',
            u'Trollhättan': u'트롤헤탄',
            u'Idre': u'이드레',
            u'Kiruna': u'키루나',
            u'Åmål': u'오몰',
            u'Västerås': u'베스테로스',
            u'Småland': u'스몰란드',
            u'Boden': u'보덴',
            u'Stockholm': u'스톡홀름',
            u'Örebro': u'외레브로',
            u'Östersund': u'외스테르순드',
            u'Björn': u'비에른',
            u'Linköping': u'린셰핑',
            u'Umeå': u'우메오',
            u'Luleå': u'룰레오',
            u'Lund': u'룬드',
            u'Ystad': u'위스타드',
            u'Nynäshamn': u'뉘네스함',
            u'Visby': u'비스뷔',
        })

    def test_1st(self):
        """제1항
        1. b, g가 무성 자음 앞에 올 때에는 받침 'ㅂ, ㄱ'으로 적는다.
        2. k, ck, p, t는 무성 자음 앞에서 받침 'ㄱ, ㄱ, ㅂ, ㅅ'으로 적는다.
        """
        self.assert_examples({
            u'snabbt': u'스납트',
            u'högst': u'획스트',
            u'oktober': u'옥토베르',
            u'Stockholm': u'스톡홀름',
            u'Uppsala': u'웁살라',
            u'Botkyrka': u'봇쉬르카',
        })

    def test_2nd(self):
        """제2항: c는 'ㅋ'으로 적되, e, i, a, y, o 앞에서는 'ㅅ'으로 적는다."""
        self.assert_examples({
            u'campa': u'캄파',
            u'Celsius': u'셀시우스',
        })

    def test_3rd(self):
        """제3항: g
        1. 모음 앞의 g는 'ㄱ'으로 적되, e, i, a, y, o 앞에서는 '이'로 적고
           뒤따르는 모음과 합쳐 적는다.
        2. lg, rg의 g는 '이'로 적는다
        3. n 앞의 g는 'ㅇ'으로 적는다.
        4. 무성 자음 앞의 g는 받침 'ㄱ'으로 적는다.
        5. 그 밖의 자음 앞과 어말에서는 '그'로 적는다.
        """
        self.assert_examples({
            u'Gustav': u'구스타브',
            u'Göteborg': u'예테보리',
            u'älg': u'엘리',
            u'Borg': u'보리',
            u'Magnus': u'망누스',
            u'högst': u'획스트',
            u'Ludvig': u'루드비그',
            u'Greta': u'그레타',
        })

    def test_4th(self):
        """제4항: j는 자음과 모음 사이에 올 때에 앞의 자음과 합쳐서 적는다."""
        self.assert_examples({
            u'fjäril': u'피에릴',
            u'mjuk': u'미우크',
            u'kedja': u'셰디아',
            u'Björn': u'비에른',
        })

    def test_5th(self):
        """제5항
        k는 'ㅋ'으로 적되, e, i, a, y, o 앞에서는 '시'로 적고 뒤따르는 모음과
        합쳐 적는다.
        """
        self.assert_examples({
            u'Kungsholm': u'쿵스홀름',
            u'Norrköping': u'노르셰핑',
        })

    def test_6th(self):
        """제6항
        어말 또는 자음 앞의 l은 받침 'ㄹ'로 적고, 어중의 l이 모음 앞에 올
        때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            u'folk': u'폴크',
            u'tal': u'탈',
            u'tala': u'탈라',
        })

    def test_7th(self):
        """제7항
        어두의 lj는 '이'로 적되 뒤따르는 모음과 합쳐 적고, 어중의 lj는
        'ㄹ리'로 적는다.
        """
        self.assert_examples({
            u'Ljusnan': u'유스난',
            u'Södertälje': u'쇠데르텔리에',
        })

    def test_8th(self):
        """제8항
        n은 어말에서 m 다음에 올 때 적지 않는다.
        """
        self.assert_examples({
            u'Karlshamn': u'칼스함',
            u'namn': u'남',
        })

    def test_9th(self):
        """제9항
        nk는 자음 t 앞에서는 'ㅇ'으로, 그 밖의 경우에는 'ㅇ크'로 적는다.
        """
        self.assert_examples({
            u'anka': u'앙카',
            u'Sankt': u'상트',
            u'punkt': u'풍트',
            u'bank': u'방크',
        })

    def test_10th(self):
        """제10항
        sk는 '스ㅋ'으로 적되 e, i, a, y, o 앞에서는 '시'로 적고, 뒤따르는
        모음과 합쳐 적는다.
        """
        self.assert_examples({
            u'Skoglund': u'스코글룬드',
            u'skuldra': u'스쿨드라',
            u'skål': u'스콜',
            u'skörd': u'셰르드',
            u'skydda': u'쉬다',
        })

    def test_11st(self):
        """제11항
        o는 '외'로 적되 g, j, k, kj, lj, skj 다음에서는 '에'로 적고, 앞의
        '이' 또는 '시'와 합쳐서 적는다. 다만, jo 앞에 그 밖의 자음이 올 때에는
        j는 앞의 자음과 합쳐 적고, o는 '에'로 적는다.
        """
        self.assert_examples({
            u'Örebro': u'외레브로',
            u'Göta': u'예타',
            u'Jönköping': u'옌셰핑',
            u'Björn': u'비에른',
            u'Björling': u'비엘링',
            u'mjöl': u'미엘',
        })

    def test_12nd(self):
        """제12항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 단, mm,
        nn은 모음 앞에서 'ㅁㅁ', 'ㄴㄴ'으로 적는다.
        """
        self.assert_examples({
            u'Kattegatt': u'카테가트',
            u'Norrköping': u'노르셰핑',
            u'Uppsala': u'웁살라',
            u'Bromma': u'브롬마',
            u'Dannemora': u'단네모라',
        })

    def test_people(self):
        self.assert_examples({
            u'Sankta Ragnhild': u'상타 랑힐드',
        })
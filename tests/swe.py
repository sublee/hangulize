# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.swe import Swedish


class SwedishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0213.jsp """

    lang = Swedish()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0111.jsp """
        assert u'발' == self.hangulize(u'bal')
        assert u'스납트' == self.hangulize(u'snabbt')
        assert u'야코브' == self.hangulize(u'Jacob')
        assert u'칼손' == self.hangulize(u'Carlsson')
        assert u'셀시우스' == self.hangulize(u'Celsius')
        assert u'에릭손' == self.hangulize(u'Ericson')
        assert u'샤름' == self.hangulize(u'charm')
        assert u'오크' == self.hangulize(u'och')
        assert u'다그' == self.hangulize(u'dag')
        assert u'드리카' == self.hangulize(u'dricka')
        assert u'할름스타드' == self.hangulize(u'Halmstad')
        assert u'유르고르덴' == self.hangulize(u'Djurgården')
        assert u'아예' == self.hangulize(u'adjö')
        assert u'순스발' == self.hangulize(u'Sundsvall')
        assert u'팔룬' == self.hangulize(u'Falun')
        assert u'루프트' == self.hangulize(u'luft')
        assert u'구스타브' == self.hangulize(u'Gustav')
        assert u'헬곤' == self.hangulize(u'helgon')
        assert u'예테보리' == self.hangulize(u'Göteborg')
        assert u'예이예르' == self.hangulize(u'Geijer')
        assert u'이슬라베드' == self.hangulize(u'Gislaved')
        assert u'엘리' == self.hangulize(u'älg')
        assert u'스트린드베리' == self.hangulize(u'Strindberg')
        assert u'보리' == self.hangulize(u'Borg')
        # assert u'망누스' == self.hangulize(u'Magnus')
        # => 망음누스
        # assert u'랑나르' == self.hangulize(u'Ragnar')
        # => 랑음나르
        # assert u'앙네스' == self.hangulize(u'Agnes')
        # => 앙음네스
        assert u'획스트' == self.hangulize(u'högst')
        assert u'그뢴베리' == self.hangulize(u'Grönberg')
        assert u'예르스타드' == self.hangulize(u'Gjerstad')
        assert u'예르벨' == self.hangulize(u'Gjörwell')
        assert u'헬싱보리' == self.hangulize(u'Hälsingborg')
        assert u'휘라' == self.hangulize(u'hyra')
        assert u'달' == self.hangulize(u'Dahl')
        assert u'옐마렌' == self.hangulize(u'Hjälmaren')
        assert u'얄마르' == self.hangulize(u'Hjalmar')
        assert u'요르트' == self.hangulize(u'Hjort')
        assert u'얀손' == self.hangulize(u'Jansson')
        assert u'옌셰핑' == self.hangulize(u'Jönköping')
        assert u'요한손' == self.hangulize(u'Johansson')
        assert u'뵈리아' == self.hangulize(u'börja')
        assert u'피에릴' == self.hangulize(u'fjäril')
        assert u'미우크' == self.hangulize(u'mjuk')
        assert u'미엘' == self.hangulize(u'mjöl')
        assert u'칼' == self.hangulize(u'Karl')
        assert u'코크' == self.hangulize(u'Kock')
        assert u'쿵스홀름' == self.hangulize(u'Kungsholm')
        assert u'셰르스틴' == self.hangulize(u'Kerstin')
        assert u'노르셰핑' == self.hangulize(u'Norrköping')
        assert u'뤼세실' == self.hangulize(u'Lysekil')
        assert u'옥토베르' == self.hangulize(u'oktober')
        assert u'프레드리크' == self.hangulize(u'Fredrik')
        assert u'크니브' == self.hangulize(u'kniv')
        assert u'바케르' == self.hangulize(u'vacker')
        assert u'스톡홀름' == self.hangulize(u'Stockholm')
        assert u'보크' == self.hangulize(u'bock')
        assert u'셸' == self.hangulize(u'Kjell')
        assert u'슐라' == self.hangulize(u'Kjula')
        assert u'린셰핑' == self.hangulize(u'Linköping')
        assert u'탈라' == self.hangulize(u'tala')
        assert u'탈' == self.hangulize(u'tal')
        assert u'유스난' == self.hangulize(u'Ljusnan')
        assert u'쇠데르텔리에' == self.hangulize(u'Södertälje')
        assert u'데탈리' == self.hangulize(u'detalj')
        assert u'말뫼' == self.hangulize(u'Malmö')
        assert u'삼탈' == self.hangulize(u'samtal')
        assert u'훔메르' == self.hangulize(u'hummer')
        assert u'노르셰핑' == self.hangulize(u'Norrköping')
        assert u'베네른' == self.hangulize(u'Vänern')
        assert u'란드' == self.hangulize(u'land')
        assert u'칼스함' == self.hangulize(u'Karlshamn')
        assert u'볼렝에' == self.hangulize(u'Borlänge')
        assert u'쿵' == self.hangulize(u'kung')
        assert u'롱' == self.hangulize(u'lång')
        assert u'앙카' == self.hangulize(u'anka')
        assert u'상트' == self.hangulize(u'Sankt')
        assert u'방크' == self.hangulize(u'bank')
        assert u'피테오' == self.hangulize(u'Piteå')
        assert u'크납트' == self.hangulize(u'knappt')
        assert u'웁살라' == self.hangulize(u'Uppsala')
        assert u'캄프' == self.hangulize(u'kamp')
        assert u'말름크비스트' == self.hangulize(u'Malmqvist')
        assert u'린드크비스트' == self.hangulize(u'Lindqvist')
        assert u'뢰드' == self.hangulize(u'röd')
        assert u'빌란데르' == self.hangulize(u'Wilander')
        assert u'비에르크' == self.hangulize(u'Björk')
        assert u'엘란데르' == self.hangulize(u'Erlander')
        assert u'칼그렌' == self.hangulize(u'Karlgren')
        assert u'얄' == self.hangulize(u'Jarl')
        assert u'솜마르' == self.hangulize(u'sommar')
        assert u'스토르비크' == self.hangulize(u'Storvik')
        assert u'단스' == self.hangulize(u'dans')
        assert u'샤크' == self.hangulize(u'Schack')
        assert u'셰인' == self.hangulize(u'Schein')
        assert u'레반슈' == self.hangulize(u'revansch')
        assert u'네셰' == self.hangulize(u'Nässjö')
        assert u'슈크헴' == self.hangulize(u'sjukhem')
        assert u'셰베리' == self.hangulize(u'Sjöberg')
        assert u'스코글룬드' == self.hangulize(u'Skoglund')
        assert u'셸레프테오' == self.hangulize(u'Skellefteå')
        assert u'셰브데' == self.hangulize(u'Skövde')
        assert u'솁스홀멘' == self.hangulize(u'Skeppsholmen')
        assert u'함마르셸드' == self.hangulize(u'Hammarskjöld')
        assert u'셸데브란드' == self.hangulize(u'Skjöldebrand')
        assert u'셰르네보리' == self.hangulize(u'Stjärneborg')
        assert u'옥센셰르나' == self.hangulize(u'Oxenstjerna')
        assert u'예타' == self.hangulize(u'Göta')
        assert u'봇쉬르카' == self.hangulize(u'Botkyrka')
        assert u'트렐레보리' == self.hangulize(u'Trelleborg')
        assert u'보트' == self.hangulize(u'båt')
        assert u'루테르' == self.hangulize(u'Luther')
        assert u'툰베리' == self.hangulize(u'Thunberg')
        assert u'렉숀' == self.hangulize(u'lektion')
        assert u'스타숀' == self.hangulize(u'station')
        assert u'셰크' == self.hangulize(u'tjeck')
        assert u'쇼코' == self.hangulize(u'Tjåkkå')
        assert u'셰나' == self.hangulize(u'tjäna')
        assert u'슈고' == self.hangulize(u'tjugo')
        assert u'스베리예' == self.hangulize(u'Sverige')
        assert u'바사' == self.hangulize(u'Wasa')
        assert u'스베덴보리' == self.hangulize(u'Swedenborg')
        assert u'에슬뢰브' == self.hangulize(u'Eslöv')
        assert u'악셀' == self.hangulize(u'Axel')
        assert u'알렉산데르' == self.hangulize(u'Alexander')
        assert u'섹스' == self.hangulize(u'sex')
        assert u'사크리스' == self.hangulize(u'Zachris')
        assert u'손' == self.hangulize(u'zon')
        assert u'로렌소' == self.hangulize(u'Lorenzo')
        assert u'칼릭스' == self.hangulize(u'Kalix')
        assert u'팔룬' == self.hangulize(u'Falun')
        assert u'알베스타' == self.hangulize(u'Alvesta')
        assert u'엔셰핑' == self.hangulize(u'Enköping')
        assert u'스베알란드' == self.hangulize(u'Svealand')
        assert u'멜라렌' == self.hangulize(u'Mälaren')
        assert u'베네른' == self.hangulize(u'Vänern')
        assert u'트롤헤탄' == self.hangulize(u'Trollhättan')
        assert u'이드레' == self.hangulize(u'Idre')
        assert u'키루나' == self.hangulize(u'Kiruna')
        assert u'오몰' == self.hangulize(u'Åmål')
        assert u'베스테로스' == self.hangulize(u'Västerås')
        assert u'스몰란드' == self.hangulize(u'Småland')
        assert u'보덴' == self.hangulize(u'Boden')
        assert u'스톡홀름' == self.hangulize(u'Stockholm')
        assert u'외레브로' == self.hangulize(u'Örebro')
        assert u'외스테르순드' == self.hangulize(u'Östersund')
        assert u'비에른' == self.hangulize(u'Björn')
        assert u'린셰핑' == self.hangulize(u'Linköping')
        assert u'우메오' == self.hangulize(u'Umeå')
        assert u'룰레오' == self.hangulize(u'Luleå')
        assert u'룬드' == self.hangulize(u'Lund')
        assert u'위스타드' == self.hangulize(u'Ystad')
        assert u'뉘네스함' == self.hangulize(u'Nynäshamn')
        assert u'비스뷔' == self.hangulize(u'Visby')

    def test_1st(self):
        """제1항
        1. b, g가 무성 자음 앞에 올 때에는 받침 'ㅂ, ㄱ'으로 적는다.
        2. k, ck, p, t는 무성 자음 앞에서 받침 'ㄱ, ㄱ, ㅂ, ㅅ'으로 적는다.
        """
        assert u'스납트' == self.hangulize(u'snabbt')
        assert u'획스트' == self.hangulize(u'högst')
        assert u'옥토베르' == self.hangulize(u'oktober')
        assert u'스톡홀름' == self.hangulize(u'Stockholm')
        assert u'웁살라' == self.hangulize(u'Uppsala')
        assert u'봇쉬르카' == self.hangulize(u'Botkyrka')

    def test_2nd(self):
        """제2항: c는 'ㅋ'으로 적되, e, i, a, y, o 앞에서는 'ㅅ'으로 적는다."""
        assert u'캄파' == self.hangulize(u'campa')
        assert u'셀시우스' == self.hangulize(u'Celsius')

    def test_3rd(self):
        """제3항: g
        1. 모음 앞의 g는 'ㄱ'으로 적되, e, i, a, y, o 앞에서는 '이'로 적고
           뒤따르는 모음과 합쳐 적는다.
        2. lg, rg의 g는 '이'로 적는다
        3. n 앞의 g는 'ㅇ'으로 적는다.
        4. 무성 자음 앞의 g는 받침 'ㄱ'으로 적는다.
        5. 그 밖의 자음 앞과 어말에서는 '그'로 적는다.
        """
        assert u'구스타브' == self.hangulize(u'Gustav')
        assert u'예테보리' == self.hangulize(u'Göteborg')
        assert u'엘리' == self.hangulize(u'älg')
        assert u'보리' == self.hangulize(u'Borg')
        # assert u'망누스' == self.hangulize(u'Magnus')
        # => 망음누스
        assert u'획스트' == self.hangulize(u'högst')
        assert u'루드비그' == self.hangulize(u'Ludvig')
        assert u'그레타' == self.hangulize(u'Greta')

    def test_4th(self):
        """제4항: j는 자음과 모음 사이에 올 때에 앞의 자음과 합쳐서 적는다."""
        assert u'피에릴' == self.hangulize(u'fjäril')
        assert u'미우크' == self.hangulize(u'mjuk')
        assert u'셰디아' == self.hangulize(u'kedja')
        assert u'비에른' == self.hangulize(u'Björn')

    def test_5th(self):
        """제5항
        k는 'ㅋ'으로 적되, e, i, a, y, o 앞에서는 '시'로 적고 뒤따르는 모음과
        합쳐 적는다.
        """
        assert u'쿵스홀름' == self.hangulize(u'Kungsholm')
        assert u'노르셰핑' == self.hangulize(u'Norrköping')

    def test_6th(self):
        """제6항
        어말 또는 자음 앞의 l은 받침 'ㄹ'로 적고, 어중의 l이 모음 앞에 올
        때에는 'ㄹㄹ'로 적는다.
        """
        assert u'폴크' == self.hangulize(u'folk')
        assert u'탈' == self.hangulize(u'tal')
        assert u'탈라' == self.hangulize(u'tala')

    def test_7th(self):
        """제7항
        어두의 lj는 '이'로 적되 뒤따르는 모음과 합쳐 적고, 어중의 lj는
        'ㄹ리'로 적는다.
        """
        assert u'유스난' == self.hangulize(u'Ljusnan')
        assert u'쇠데르텔리에' == self.hangulize(u'Södertälje')

    def test_8th(self):
        """제8항
        n은 어말에서 m 다음에 올 때 적지 않는다.
        """
        assert u'칼스함' == self.hangulize(u'Karlshamn')
        assert u'남' == self.hangulize(u'namn')

    def test_9th(self):
        """제9항
        nk는 자음 t 앞에서는 'ㅇ'으로, 그 밖의 경우에는 'ㅇ크'로 적는다.
        """
        assert u'앙카' == self.hangulize(u'anka')
        assert u'상트' == self.hangulize(u'Sankt')
        assert u'풍트' == self.hangulize(u'punkt')
        assert u'방크' == self.hangulize(u'bank')

    def test_10th(self):
        """제10항
        sk는 '스ㅋ'으로 적되 e, i, a, y, o 앞에서는 '시'로 적고, 뒤따르는
        모음과 합쳐 적는다.
        """
        assert u'스코글룬드' == self.hangulize(u'Skoglund')
        assert u'스쿨드라' == self.hangulize(u'skuldra')
        assert u'스콜' == self.hangulize(u'skål')
        assert u'셰르드' == self.hangulize(u'skörd')
        assert u'쉬다' == self.hangulize(u'skydda')

    def test_11st(self):
        """제11항
        o는 '외'로 적되 g, j, k, kj, lj, skj 다음에서는 '에'로 적고, 앞의
        '이' 또는 '시'와 합쳐서 적는다. 다만, jo 앞에 그 밖의 자음이 올 때에는
        j는 앞의 자음과 합쳐 적고, o는 '에'로 적는다.
        """
        assert u'외레브로' == self.hangulize(u'Örebro')
        assert u'예타' == self.hangulize(u'Göta')
        assert u'옌셰핑' == self.hangulize(u'Jönköping')
        assert u'비에른' == self.hangulize(u'Björn')
        assert u'비엘링' == self.hangulize(u'Björling')
        assert u'미엘' == self.hangulize(u'mjöl')

    def test_12nd(self):
        """제12항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 단, mm,
        nn은 모음 앞에서 'ㅁㅁ', 'ㄴㄴ'으로 적는다.
        """
        assert u'카테가트' == self.hangulize(u'Kattegatt')
        assert u'노르셰핑' == self.hangulize(u'Norrköping')
        assert u'웁살라' == self.hangulize(u'Uppsala')
        assert u'브롬마' == self.hangulize(u'Bromma')
        assert u'단네모라' == self.hangulize(u'Dannemora')

    def test_people(self):
        assert u'상타 랑힐드' == self.hangulize(u'Sankta Ragnhild')

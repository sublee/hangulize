# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.pol import Polish


class PolishTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0208.jsp """

    lang = Polish()

    def test_people(self):
        self.assert_examples({
            u'Jerzy Andrzejewski': u'예지 안제예프스키',
            u'Stefan Banach': u'스테판 바나흐',
            u'Stanisław Barańczak': u'스타니스와프 바란차크',
            u'Marek Belka': u'마레크 벨카',
            u'Seweryn Bialer': u'세베린 비알레르',
            u'Bolesław Bierut': u'볼레스와프 비에루트',
            u'Zbigniew Boniek': u'즈비그니에프 보니에크',
            u'Bogdan Borusewicz': u'보그단 보루세비치',
            u'Zbigniew Bujak': u'즈비그니에프 부야크',
            u'Jerzy Buzek': u'예지 부제크',
            u'Włodzimierz Cimoszewicz': u'브워지미에시 치모셰비치',
            u'Józef Cyrankiewicz': u'유제프 치란키에비치',
            u'Ignacy Daszyński': u'이그나치 다신스키',
            u'Kazimierz Deyna': u'카지미에시 데이나',
            u'Roman Dmowski': u'로만 드모프스키',
            u'Jerzy Dudek': u'예지 두데크',
            u'Dariusz Dziekanowski': u'다리우시 지에카노프스키',
            u'Feliks Dzierżyński': u'펠릭스 지에르진스키',
            u'Kazimierz Fajans': u'카지미에시 파얀스',
            u'Magdalena Frackowiak': u'마그달레나 프라츠코비아크',
            u'Kazimierz Funk': u'카지미에시 푼크',
            u'Edward Gierek': u'에드바르트 기에레크',
            u'Józef Glemp': u'유제프 글렘프',
            u'Leopold Godowsky': u'레오폴트 고도프스키',
            u'Witold Gombrowicz': u'비톨트 곰브로비치',
            u'Władysław Gomułka': u'브와디스와프 고무우카',
            u'Jerzy Grotowski': u'예지 그로토프스키',
            u'Zbigniew Herbert': u'즈비그니에프 헤르베르트',
            u'Leonid Hurwicz': u'레오니트 후르비치',
            u'Jarosław Iwaszkiewicz': u'야로스와프 이바슈키에비치',
            u'Aleksander Jabłoński': u'알렉산데르 야브원스키',
            u'Jadwiga Andegaweńska': u'야드비가 안데가벤스카',
            u'Jagiełło': u'야기에워',
            u'Wanda Jakubowska': u'반다 야쿠보프스카',
            u'Henryk Jankowski': u'헨리크 얀코프스키',
            u'Wojciech Jaruzelski': u'보이치에흐 야루젤스키',
            u'Otylia Jędrzejczak': u'오틸리아 옝제이차크',
            u'Jan Andrzej Paweł Kaczmarek': \
                u'얀 안제이 파베우 카치마레크',
            u'Jarosław Kaczyński': u'야로스와프 카친스키',
            u'Lech Kaczyński': u'레흐 카친스키',
            u'Stanisław Kania': u'스타니스와프 카니아',
            u'Krzysztof Kieślowski': u'크시슈토프 키에실로프스키',
            u'Stefan Kisielewski': u'스테판 키시엘레프스키',
            u'Leszek Kołakowski': u'레셰크 코와코프스키',
            u'Bronisław Komorowski': u'브로니스와프 코모로프스키',
            u'Paweł Korzeniowski': u'파베우 코제니오프스키',
            u'Tadeusz Kościuszko': u'타데우시 코시치우슈코',
            u'Justyna Kowalczyk': u'유스티나 코발치크',
            u'Zygmunt Krasiński': u'지그문트 크라신스키',
            u'Jacek Krzynówek': u'야체크 크시누베크',
            u'Jacek Kuroń': u'야체크 쿠론',
            u'Aleksander Kwaśniewski': u'알렉산데르 크바시니에프스키',
            u'Wanda Landowska': u'반다 란도프스카',
            u'Grzegorz Lato': u'그제고시 라토',
            u'Joachim Lelewel': u'요아힘 렐레벨',
            u'Włodzimierz Lubański': u'브워지미에시 루반스키',
            u'Jan Łukasiewicz': u'얀 우카시에비치',
            u'Bronisław Malinowski': u'브로니스와프 말리노프스키',
            u'Adam Małysz': u'아담 마위시',
            u'Kazimierz Marcinkiewicz': u'카지미에시 마르친키에비치',
            u'Tadeusz Mazowiecki': u'타데우시 마조비에츠키',
            u'Zbigniew Messner': u'즈비그니에프 메스네르',
            u'Adam Michnik': u'아담 미흐니크',
            u'Adam Mickiewicz': u'아담 미츠키에비치',
            u'Stanisław Mikołajczyk': u'스타니스와프 미코와이치크',
            u'Leszek Miller': u'레셰크 밀레르',
            u'Czesław Miłosz': u'체스와프 미워시',
            u'Sławomir Mrożek': u'스와보미르 므로제크',
            u'Cyprian Kamil Norwid': u'치프리안 카밀 노르비트',
            u'Edward Ochab': u'에드바르트 오하프',
            u'Eliza Orzeszkowa': u'엘리자 오제슈코바',
            u'Ignacy Jan Paderewski': u'이그나치 얀 파데레프스키',
            u'Krzysztof Penderecki': u'크시슈토프 펜데레츠키',
            u'Józef Piłsudski': u'유제프 피우수트스키',
            u'Jacek Podsiadło': u'야체크 포트시아드워',
            u'Anja Rubik': u'아냐 루비크',
            u'Mateusz Sawrymowicz': u'마테우시 사브리모비치',
            u'Wacław Sierpiński': u'바츠와프 시에르핀스키',
            u'Maria Skłodowska': u'마리아 스크워도프스카',
            u'Włodzimierz Smolarek': u'브워지미에시 스몰라레크',
            u'Katarzyna Sowula': u'카타지나 소불라',
            u'Andrzej Stasiuk': u'안제이 스타시우크',
            u'Andrzej Szarmach': u'안제이 샤르마흐',
            u'Wojciech Szczęsny': u'보이치에흐 슈쳉스니',
            u'Piotr Szewc': u'피오트르 셰프츠',
            u'Sławomir Szmal': u'스와보미르 슈말',
            u'Rafał Szukała': u'라파우 슈카와',
            u'Alfred Tarski': u'알프레트 타르스키',
            u'Stefan Themerson': u'스테판 테메르손',
            u'Olga Tokarczuk': u'올가 토카르추크',
            u'Jan Tomaszewski': u'얀 토마셰프스키',
            u'Donald Tusk': u'도날트 투스크',
            u'Andrzej Wajda': u'안제이 바이다',
            u'Lech Wałęsa': u'레흐 바웬사',
            u'Mia Wasikowska': u'미아 바시코프스카',
            u'Wanda Wasilewska': u'반다 바실레프스카',
            u'Adam Ważyk': u'아담 바지크',
            u'Aleksander Wielopolski': u'알렉산데르 비엘로폴스키',
            u'Henryk Wieniawski': u'헨리크 비에니아프스키',
            u'Ernest Wilimowski': u'에르네스트 빌리모프스키',
            u'Stanisław Ignacy Witkiewicz': \
                u'스타니스와프 이그나치 비트키에비치',
            u'Michał Witkowski': u'미하우 비트코프스키',
            u'Karol Wojtyła': u'카롤 보이티와',
            u'Katarzyna Woźniak': u'카타지나 보지니아크',
            u'Stanisław Wyspiański': u'스타니스와프 비스피안스키',
            u'Stefan Wyszyński': u'스테판 비신스키',
            u'Ludwik Łazarz Zamenhof': u'루드비크 와자시 자멘호프',
            u'Krystian Zimerman': u'크리스티안 지메르만',
            u'Luiza Złotkowska': u'루이자 즈워트코프스카',
            u'Florian Znaniecki': u'플로리안 즈나니에츠키',
            u'Stefan Żeromski': u'스테판 제롬스키',
            u'Maciej Żurawski': u'마치에이 주라프스키',
        })

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0106.jsp """
        self.assert_examples({
            u'burak': u'부라크',
            u'szybko': u'십코',
            u'dobrze': u'도브제',
            u'chleb': u'흘레프',
            u'cel': u'첼',
            u'Balicki': u'발리츠키',
            u'noc': u'노츠',
            u'dać': u'다치',
            u'dach': u'다흐',
            u'zdrowy': u'즈드로비',
            u'słodki': u'스워트키',
            u'pod': u'포트',
            u'fasola': u'파솔라',
            u'befsztyk': u'베프슈티크',
            u'góra': u'구라',
            u'grad': u'그라트',
            u'targ': u'타르크',
            u'herbata': u'헤르바타',
            u'Hrubieszów': u'흐루비에슈프',
            u'kino': u'키노',
            u'daktyl': u'닥틸',
            u'król': u'크룰',
            u'bank': u'반크',
            u'lis': u'리스',
            u'kolano': u'콜라노',
            u'motyl': u'모틸',
            u'most': u'모스트',
            u'zimno': u'짐노',
            u'sam': u'삼',
            u'nerka': u'네르카',
            u'dokument': u'도쿠멘트',
            u'dywan': u'디반',
            u'Gdańsk': u'그단스크',
            u'Poznań': u'포즈난',
            u'para': u'파라',
            u'Słupsk': u'스웁스크',
            u'chłop': u'흐워프',
            u'rower': u'로베르',
            u'garnek': u'가르네크',
            u'sznur': u'슈누르',
            u'serce': u'세르체',
            u'srebro': u'스레브로',
            u'pas': u'파스',
            u'ślepy': u'실레피',
            u'dziś': u'지시',
            u'tam': u'탐',
            u'matka': u'마트카',
            u'but': u'부트',
            u'Warszawa': u'바르샤바',
            u'piwnica': u'피브니차',
            u'krew': u'크레프',
            u'zamek': u'자메크',
            u'zbrodnia': u'즈브로드니아',
            u'wywóz': u'비부스',
            u'gwoździk': u'그보지지크',
            u'więź': u'비엥시',
            u'żyto': u'지토',
            u'różny': u'루주니',
            u'łyżka': u'위슈카',
            u'straż': u'스트라시',
            u'chory': u'호리',
            u'kuchnia': u'쿠흐니아',
            u'dach': u'다흐',
            u'dziura': u'지우라',
            u'dzwon': u'즈본',
            u'mosiądz': u'모시옹츠',
            u'niedźwiedź': u'니에치비에치',
            u'drzewo': u'제보',
            u'łodż': u'워치',
            u'czysty': u'치스티',
            u'beczka': u'베치카',
            u'klucz': u'클루치',
            u'szary': u'샤리',
            u'musztarda': u'무슈타르다',
            u'kapelusz': u'카펠루시',
            u'rzeka': u'제카',
            u'Przemyśl': u'프셰미실',
            u'kołnierz': u'코우니에시',
            u'jasny': u'야스니',
            u'kraj': u'크라이',
            u'łono': u'워노',
            u'głowa': u'그워바',
            u'bułka': u'부우카',
            u'kanał': u'카나우',
            u'trawa': u'트라바',
            u'trąba': u'트롱바',
            u'mąka': u'몽카',
            u'kąt': u'콩트',
            u'tą': u'통',
            u'zero': u'제로',
            u'kępa': u'켕파',
            u'węgorz': u'벵고시',
            u'Częstochowa': u'쳉스토호바',
            u'proszę': u'프로셰',
            u'zima': u'지마',
            u'udo': u'우도',
            u'próba': u'프루바',
            u'kula': u'쿨라',
            u'daktyl': u'닥틸',
        })

    def test_1st(self):
        """제1항: k, p
        어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        self.assert_examples({
            u'zamek': u'자메크',
            u'mokry': u'모크리',
            u'Słupsk': u'스웁스크',
        })

    def test_2nd(self):
        """제2항: b, d, g
        1. 어말에 올 때에는 '프', '트', '크'로 적는다.
        2. 유성 자음 앞에서는 '브', '드', '그'로 적는다.
        3. 무성 자음 앞에서 b, g는 받침으로 적고, d는 '트'로 적는다.
        """
        self.assert_examples({
            u'od': u'오트',
            u'zbrodnia': u'즈브로드니아',
            u'Grabski': u'그랍스키',
            u'odpis': u'오트피스',
        })

    def test_3rd(self):
        """제3항: w, z, ź, dz, ż, rz, sz
        1. w, z, ź, dz가 무성 자음 앞이나 어말에 올 때에는 '프, 스, 시, 츠'로
           적는다.
        2. ż와 rz는 모음 앞에 올 때에는 'ㅈ'으로 적되, 앞의 자음이 무성
           자음일 때에는 '시'로 적는다. 유성 자음 앞에 올 때에는 '주', 무성
           자음 앞에 올 때에는 '슈', 어말에 올 때에는 '시'로 적는다.
        3. sz는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        self.assert_examples({
            u'zabawka': u'자바프카',
            u'obraz': u'오브라스',
            u'Rzeszów': u'제슈프',
            u'Przemyśl': u'프셰미실',
            u'grzmot': u'그주모트',
            u'łóżko': u'우슈코',
            u'pęcherz': u'펭헤시',
            u'koszt': u'코슈트',
            u'kosz': u'코시',
        })

    def test_4th(self):
        """제4항: ł
        1. ł는 뒤따르는 모음과 결합할 때 합쳐서 적는다. (ło는 '워'로 적는다.)
           다만, 자음 뒤에 올 때에는 두 음절로 갈라 적는다.
        2. oł는 '우'로 적는다.
        """
        self.assert_examples({
            u'łono': u'워노',
            u'głowa': u'그워바',
            u'przyjaciół': u'프시야치우',
        })

    def test_5th(self):
        """제5항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            u'olej': u'올레이',
        })

    def test_6th(self):
        """제6항: m
        어두의 m이 l, r 앞에 올 때에는 '으'를 붙여 적는다.
        """
        self.assert_examples({
            u'mleko': u'믈레코',
            u'mrówka': u'므루프카',
        })

    def test_7th(self):
        """제7항: ę
        ę은 '엥'으로 적는다. 다만, 어말의 ę는 '에'로 적는다.
        """
        self.assert_examples({
            u'ręka': u'렝카',
            u'proszę': u'프로셰',
        })

    def test_8th(self):
        """제8항
        'ㅈ', 'ㅊ'으로 표기되는 자음(c, z) 뒤의 이중 모음은 단모음으로 적는다.
        """
        self.assert_examples({
            u'stacja': u'스타차',
            u'fryzjer': u'프리제르',
        })

    def test_etc(self):
        self.assert_examples({
            u'przjyaciół': u'프시아치우',
        })
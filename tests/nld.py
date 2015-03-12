# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.nld import Dutch


class DutchTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0220.jsp """

    lang = Dutch()

    def test_etc(self):
        self.assert_examples({
            u'tuig': u'타위흐',
        })

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0118.jsp """
        self.assert_examples({
            u'Borst': u'보르스트',
            u'Bram': u'브람',
            u'Jacob': u'야코프',
            u'Campen': u'캄펀',
            u'Nicolaas': u'니콜라스',
            u'topic': u'토픽',
            u'scrupel': u'스크뤼펄',
            u'cyaan': u'시안',
            u'Ceelen': u'세일런',
            u'Volcher': u'폴허르',
            u'Utrecht': u'위트레흐트',
            u'Delft': u'델프트',
            u'Edgar': u'엣하르',
            u'Hendrik': u'헨드릭',
            u'Helmond': u'헬몬트',
            u'Flevoland': u'플레볼란트',
            u'Graaf': u'흐라프',
            u'Goes': u'후스',
            u'Limburg': u'림뷔르흐',
            u'Heineken': u'헤이네컨',
            u'Hendrik': u'헨드릭',
            u'Jongkind': u'용킨트',
            u'Jan': u'얀',
            u'Jeroen': u'예룬',
            u'Kok': u'콕',
            u'Alkmaar': u'알크마르',
            u'Zierikzee': u'지릭제이',
            u'kwaliteit': u'크발리테이트',
            u'kwellen': u'크벨런',
            u'kwitantie': u'크비탄시',
            u'Lasso': u'라소',
            u'Friesland': u'프리슬란트',
            u'sabel': u'사벌',
            u'Meerssen': u'메이르선',
            u'Zalm': u'잘름',
            u'Nijmegen': u'네이메헌',
            u'Jansen': u'얀선',
            u'Inge': u'잉어',
            u'Groningen': u'흐로닝언',
            u'Peper': u'페퍼르',
            u'Kapteyn': u'캅테인',
            u'Koopmans': u'코프만스',
            u'Rotterdam': u'로테르담',
            u'Asser': u'아서르',
            u'Spinoza': u'스피노자',
            u'Hals': u'할스',
            u'Schiphol': u'스히폴',
            u'Escher': u'에스허르',
            u'typisch': u'티피스',
            u'sjaal': u'샬',
            u'huisje': u'하위셔',
            u'ramsj': u'람시',
            u'fetisj': u'페티시',
            u'Tinbergen': u'틴베르헌',
            u'Gerrit': u'헤릿',
            u'Petrus': u'페트뤼스',
            u'Aartsen': u'아르천',
            u'Beets': u'베이츠',
            u'Veltman': u'펠트만',
            u'Einthoven': u'에인트호번',
            u'Weltevree': u'벨테브레이',
            u'Wim': u'빔',
            u'cyaan': u'시안',
            # u'Lyonnet': u'리오넷',
            u'typisch': u'티피스',
            u'Verwey': u'페르베이',
            u'Zeeman': u'제이만',
            u'Huizinga': u'하위징아',
            u'Asser': u'아서르',
            u'Frans': u'프란스',
            u'Egmont': u'에흐몬트',
            u'Frederik': u'프레데릭',
            u'Heineken': u'헤이네컨',
            u'Lubbers': u'뤼버르스',
            u'Campen': u'캄펀',
            u'Nicolaas': u'니콜라스',
            u'Tobias': u'토비아스',
            u'Pieter': u'피터르',
            u'Vries': u'프리스',
            u'Onnes': u'오너스',
            u'Vondel': u'폰덜',
            u'Boer': u'부르',
            u'Boerhaave': u'부르하버',
            u'Utrecht': u'위트레흐트',
            u'Petrus': u'페트뤼스',
            u'Europort': u'외로포르트',
            u'Deurne': u'되르너',
            u'ruw': u'뤼',
            u'duwen': u'뒤언',
            u'Euwen': u'에위언',
            u'Bouts': u'바우츠',
            u'Bouwman': u'바우만',
            u'Paul': u'파울',
            u'Lauwersmeer': u'라우에르스메이르',
            u'Heike': u'헤이커',
            u'Bolkestein': u'볼케스테인',
            u'IJssel': u'에이설',
            u'Huizinga': u'하위징아',
            u'Zuid-Holland': u'자위트홀란트',
            u'Buys': u'바위스',
            u'draaien': u'드라이언',
            u'fraai': u'프라이',
            u'zaait': u'자이트',
            u'Maaikes': u'마이커스',
            u'Booisman': u'보이스만',
            u'Hooites': u'호이터스',
            u'Boeijinga': u'부잉아',
            u'moeite': u'무이터',
            u'Leeuwenhoek': u'레이우엔훅',
            u'Meeuwes': u'메이우어스',
            u'Lieuwma': u'리우마',
            u'Rieuwers': u'리우어르스',
        })

    def test_1st(self):
        """제1항
        무성 파열음 p, t, k는 자음 앞이나 어말에 올 경우에는 각각 받침
        ‘ㅂ, ㅅ, ㄱ'으로 적는다. 다만, 앞 모음이 이중 모음이거나 장모음(같은
        모음을 겹쳐 적는 경우)인 경우와 앞이나 뒤의 자음이 유음이나 비음인
        경우에는 ‘프, 트, 크'로 적는다.
        """
        self.assert_examples({
            u'Wit': u'빗',
            u'Gennip': u'헤닙',
            u'Kapteyn': u'캅테인',
            u'september': u'셉템버르',
            u'Petrus': u'페트뤼스',
            u'Arcadelt': u'아르카덜트',
            u'Hoop': u'호프',
            u'Eijkman': u'에이크만',
        })

    def test_2nd(self):
        """제2항
        유성 파열음 b, d가 어말에 올 경우에는 각각 ‘프, 트'로 적고, 어중에 올
        경우에는 앞이나 뒤의 자음이 유음이나 비음인 경우와 앞 모음이
        이중모음이거나 장모음(같은 모음을 겹쳐 적는 경우)인 경우에는 ‘브, 드'로
        적는다. 그 외에는 모두 받침 ‘ㅂ, ㅅ'으로 적는다.
        """
        self.assert_examples({
            u'Bram': u'브람',
            u'Hendrik': u'헨드릭',
            u'Jakob': u'야코프',
            u'Edgar': u'엣하르',
            u'Zeeland': u'제일란트',
            u'Koenraad': u'쿤라트',
        })

    def test_3rd(self):
        """제3항
        v가 어두에 올 경우에는 ‘ㅍ, 프'로 적고, 그 외에는 모두 ‘ㅂ, 브'로
        적는다.
        """
        self.assert_examples({
            u'Veltman': u'펠트만',
            u'Vries': u'프리스',
            u'Grave': u'흐라버',
            u'Weltevree': u'벨테브레이',
        })

    def test_4th(self):
        """제4항
        c는 차용어에 쓰이므로 해당 언어의 발음에 따라 ‘ㅋ'이나 ‘ㅅ'으로 적는다.
        """
        self.assert_examples({
            u'Nicolaas': u'니콜라스',
            u'Hendricus': u'헨드리퀴스',
            u'cyaan': u'시안',
            u'Franciscus': u'프란시스퀴스',
        })

    def test_5th(self):
        """제5항
        g, ch는 ‘ㅎ'으로 적되, 차용어의 경우에는 해당 언어의 발음에 따라
        적는다.
        """
        self.assert_examples({
            u'gulden': u'휠던',
            u'Haag': u'하흐',
            u'Hooch': u'호흐',
            u'Volcher': u'폴허르',
            u'Eugene': u'외젠',
            u'Michael': u'미카엘',
        })

    def test_6th(self):
        """제6항
        -tie는 ‘시'로 적는다.
        """
        self.assert_examples({
            u'natie': u'나시',
            u'politie': u'폴리시',
        })

    def test_7th(self):
        """제7항
        어중의 l이 모음 앞에 오거나 모음이 따르지 않는 비음 앞에 올 때에는
        ‘?'로 적는다. 다만, 비음 뒤의 l은 모음 앞에 오더라도 ‘ㄹ'로 적는다.
        """
        self.assert_examples({
            u'Tiele': u'틸러',
            u'Zalm': u'잘름',
            u'Berlage': u'베를라허',
            u'Venlo': u'펜로',
        })

    def test_8th(self):
        """제8항: nk
        k 앞에 오는 n은 받침 ‘ㅇ'으로 적는다.
        """
        self.assert_examples({
            u'Frank': u'프랑크',
            u'Hiddink': u'히딩크',
            u'Benk': u'벵크',
            u'Wolfswinkel': u'볼프스빙컬',
        })

    def test_9th(self):
        """제9항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다.
        """
        self.assert_examples({
            u'Hobbema': u'호베마',
            u'Ballot': u'발롯',
            u'Emmen': u'에먼',
            u'Gennip': u'헤닙',
        })

    def test_10th(self):
        """제10항
        e는 ‘에'로 적는다. 다만, 이음절 이상에서 마지막 음절에 오는 e와 어말의
        e는 모두 ‘어'로 적는다.
        """
        self.assert_examples({
            u'Dennis': u'데니스',
            u'Breda': u'브레다',
            u'Stevin': u'스테빈',
            u'Peter': u'페터르',
            u'Heineken': u'헤이네컨',
            u'Campen': u'캄펀',
        })

    def test_11st(self):
        """제11항
        같은 모음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만 ee는
        ‘에이'로 적는다.
        """
        self.assert_examples({
            u'Hooch': u'호흐',
            u'Mondriaan': u'몬드리안',
            u'Kees': u'케이스',
            u'Meerssen': u'메이르선',
        })

    def test_12nd(self):
        """제12항
        -ig는 ‘어흐'로 적는다.
        """
        self.assert_examples({
            u'tachtig': u'타흐터흐',
            u'hartig': u'하르터흐',
        })

    def test_13rd(self):
        """제13항
        -berg는 ‘베르흐'로 적는다.
        """
        self.assert_examples({
            u'Duisenberg': u'다위센베르흐',
            u'Mengelberg': u'멩엘베르흐',
        })

    def test_14th(self):
        """제14항
        over-는 ‘오버르'로 적는다.
        """
        self.assert_examples({
            u'Overijssel': u'오버레이설',
            u'overkomst': u'오버르콤스트',
        })

    def test_15th(self):
        """제15항
        모음 è, é, ê, ë는 ‘에'로 적고, ï 는 ‘이' 로 적는다.
        """
        self.assert_examples({
            u'carré': u'카레',
            # u'casuïst': u'카수이스트',
            u'drieëntwintig': u'드리엔트빈터흐',
        })

    def test_people(self):
        self.assert_examples({
            u'Jozias van Aartsen': u'요지아스 판아르천',
            u'Sharon den Adel': u'샤론 덴아덜',
            u'Dick Advocaat': u'딕 아드보카트',
            u'Karel Appel': u'카럴 아펄',
            u'Jakob Arcadelt': u'야코프 아르카덜트',
            u'Naomi van As': u'나오미 판아스',
            u'Tobias Michael Carel Asser': u'토비아스 미카엘 카럴 아서르',
            u'Ryan Babel': u'라이언 바벌',
            u'Jan Peter Balkenende': u'얀 페터르 발케넨더',
            u'Willem Barentsz': u'빌럼 바렌츠',
            u'Marco van Basten': u'마르코 판바스턴',
            u'Beatrix Wilhelmina Armgard': u'베아트릭스 빌헬미나 아름하르트',
            u'Nicolaas Beets': u'니콜라스 베이츠',
            u'Dennis Bergkamp': u'데니스 베르흐캄프',
            u'Hendrik Petrus Berlage': u'헨드릭 페트뤼스 베를라허',
            u'Bernhard Leopold': u'베른하르트 레오폴트',
            u'Leo Beenhakker': u'레오 베인하커르',
            u'Willem Blaeu': u'빌럼 블라우',
            u'Nicolaas Bloembergen': u'니콜라스 블룸베르헌',
            u'Evert Bloemsma': u'에버르트 블룸스마',
            u'Herman Boerhaave': u'헤르만 부르하버',
            u'Frits Bolkestein': u'프리츠 볼케스테인',
            u'Mark van Bommel': u'마르크 판보멀',
            u'Corrie ten Boom': u'코리 텐봄',
            u'Els Borst': u'엘스 보르스트',
            u'Theo Bos': u'테오 보스',
            u'Dirck Bouts': u'디르크 바우츠',
            u'Giovanni van Bronckhorst': u'조바니 판브롱크호르스트',
            u'Pieter Brueghel': u'피터르 브뤼헐',
            u'Armin van Buuren': u'아르민 판뷔런',
            u'Buys Ballot': u'바위스 발롯',
            u'Frank de Boer': u'프랑크 더부르',
            u'Gerard ter Borch': u'헤라르트 테르보르흐',
            u'Hans van den Broek': u'한스 판덴브룩',
            u'Inge de Bruijn': u'잉어 더브라윈',
            u'Jacob van Campen': u'야코프 판캄펀',
            u'Pieter Camper': u'피터르 캄퍼르',
            u'Phillip Cocu': u'필립 코퀴',
            u'Volcher Coiter': u'폴허르 코이터르',
            u'Anton Corbijn': u'안톤 코르베인',
            u'Johan Cruijff': u'요한 크라위프',
            u'Paul Crutzen': u'파울 크뤼천',
            u'Edgar Davids': u'엣하르 다비츠',
            u'Edith van Dijk': u'에딧 판데이크',
            u'Edsger Dijkstra': u'에츠허르 데이크스트라',
            u'Theo van Doesburg': u'테오 판두스뷔르흐',
            u'Kees van Dongen': u'케이스 판동언',
            u'Wim Duisenberg': u'빔 다위센베르흐',
            u'Christiaan Eijkman': u'크리스티안 에이크만',
            u'Willem Einthoven': u'빌럼 에인트호번',
            u'Pim Fortuyn': u'핌 포르타윈',
            u'Louis van Gaal': u'루이 판할',
            u'Yuri van Gelder': u'유리 판헬더르',
            u'Karien van Gennip': u'카린 판헤닙',
            u'Yvonne van Gennip': u'이보너 판헤닙',
            u'Annette Gerritsen': u'아네터 헤리천',
            u'Arnold Geulincx': u'아르놀트 횔링크스',
            u'Hans van Ginkel': u'한스 판힝컬',
            u'Hugo van der Goes': u'휘호 판데르후스',
            u'Theo van Gogh': u'테오 반고흐',
            u'Vincent van Gogh': u'빈센트 반고흐',
            u'Herman Gorter': u'헤르만 호르터르',
            u'Jan Gossaert': u'얀 호사르트',
            u'Reinier de Graaf': u'레이니어르 더흐라프',
            u'Frank de Grave': u'프랑크 더흐라버',
            u'Hugo de Groot': u'휘호 더흐로트',
            u'Ruud Gullit': u'뤼트 휠릿',
            u'Frans Hals': u'프란스 할스',
            u'Hendrik Hamel': u'헨드릭 하멜',
            u'Herman Heijermans': u'헤르만 헤이예르만스',
            u'Jan Baptista van Helmont': u'얀 밥티스타 판헬몬트',
            u'Guus Hiddink': u'휘스 히딩크',
            u'Meindert Hobbema': u'메인더르트 호베마',
            u'Jacobus Henricus van ’t Hoff': u'야코뷔스 헨리퀴스 판엇호프',
            u'Pieter de Hooch': u'피터르 더호흐',
            u'Gerard ’t Hooft': u'헤라르트 엇호프트',
            u'Pieter van den Hoogenband': u'피터르 판덴호헨반트',
            u'Jaap de Hoop Scheffer': u'야프 더호프 스헤퍼르',
            u'Johan Huizinga': u'요한 하위징아',
            u'Mark Huizinga': u'마르크 하위징아',
            u'Klaas-Jan Huntelaar': u'클라스얀 휜텔라르',
            u'Christiaan Huygens': u'크리스티안 하위헌스',
            u'Jan Ingenhousz': u'얀 잉엔하우스',
            u'Jozef Israëls': u'요제프 이스라엘스',
            u'Cornelis Jansen': u'코르넬리스 얀선',
            u'Famke Janssen': u'팜커 얀선',
            u'Johan Jongkind': u'요한 용킨트',
            u'Annemarie Jorritsma': u'아네마리 요리츠마',
            u'Juliana Louise Emma Marie Wilhelmina':
            u'율리아나 루이서 에마 마리 빌헬미나',
            u'Heike Kamerlingh Onnes': u'헤이커 카메를링 오너스',
            u'Jacobus Cornelius Kapteyn': u'야코뷔스 코르넬리위스 캅테인',
            u'Petrus Jacobus Kipp': u'페트뤼스 야코뷔스 킵',
            u'Patrick Kluivert': u'파트릭 클라위버르트',
            u'Ronald Koeman': u'로날트 쿠만',
            u'Wim Kok': u'빔 콕',
            u'Willem Johan Kolff': u'빌럼 요한 콜프',
            u'Pieter Kooijmans': u'피터르 코이만스',
            u'Rem Koolhaas': u'렘 콜하스',
            u'Willem de Kooning': u'빌럼 더코닝',
            u'Tjalling Koopmans': u'티알링 코프만스',
            u'Benk Korthals': u'벵크 코르탈스',
            u'Sven Kramer': u'스벤 크라머르',
            u'Dirk Kuyt': u'디르크 카위트',
            u'Lamoraal van Egmont': u'라모랄 판에흐몬트',
            u'Orlando di Lasso': u'오를란도 디라소',
            u'Jan Leeghwater': u'얀 레이흐바터르',
            u'Antoni van Leeuwenhoek': u'안토니 판레이우엔훅',
            u'Lucas van Leyden': u'뤼카스 판레이던',
            u'Jan Huygen van Linschoten': u'얀 하위헌 판린스호턴',
            u'Hendrik Willem van Loon': u'헨드릭 빌럼 판론',
            u'Hendrik Antoon Lorentz': u'헨드릭 안톤 로렌츠',
            u'Ruud Lubbers': u'뤼트 뤼버르스',
            u'Karel van Mander': u'카럴 판만더르',
            u'Bert van Marwijk': u'베르트 판마르베이크',
            u'Joris Mathijsen': u'요리스 마테이선',
            u'Simon van der Meer': u'시몬 판데르메이르',
            u'Willem Mengelberg': u'빌럼 멩엘베르흐',
            u'Paul Menkveld': u'파울 멩크벨트',
            u'Gabriël Metsu': u'가브리엘 메취',
            u'Rinus Michels': u'리뉘스 미헐스',
            u'Piet Mondriaan': u'핏 몬드리안',
            u'Harry Mulisch': u'하리 뮐리스',
            u'Ruud van Nistelrooy': u'뤼트 판니스텔로이',
            u'Teun de Nooijer': u'퇸 더노이여르',
            u'Cees Nooteboom': u'케이스 노테봄',
            u'André Ooijer': u'안드레 오이여르',
            u'Jan Hendrik Oort': u'얀 헨드릭 오르트',
            u'Adriaen van Ostade': u'아드리안 판오스타더',
            u'Marc Overmars': u'마르크 오버르마르스',
            u'Joachim Patinir': u'요아힘 파티니르',
            u'Bram Peper': u'브람 페퍼르',
            u'Robin van Persie': u'로빈 판페르시',
            u'Frank Rijkaard': u'프랑크 레이카르트',
            u'Rembrandt Harmenszoon van Rijn': u'렘브란트 하르먼스존 판레인',
            u'Arjen Robben': u'아르연 로번',
            u'Guido van Rossum': u'히도 판로쉼',
            u'André Rouvoet': u'안드레 라우붓',
            u'Jacob van Ruisdael': u'야코프 판라위스달',
            u'Mark Rutte': u'마르크 뤼터',
            u'Michiel de Ruyter': u'미힐 더라위터르',
            u'Edwin van der Sar': u'에드빈 판데르사르',
            u'Nicolien Sauerbreij': u'니콜린 사우에르브레이',
            u'Clarence Seedorf': u'클라렌서 세이도르프',
            u'Geertgen tot Sint Jans': u'헤이르트헌 톳신트얀스',
            u'Claus Sluter': u'클라우스 슬뤼터르',
            u'Rik Smits': u'릭 스미츠',
            u'Wesley Sneijder': u'베슬리 스네이더르',
            u'Willebrord Snel van Royen': u'빌레브로르트 스넬 판로이언',
            u'Baruch Spinoza': u'바뤼흐 스피노자',
            u'Jan Steen': u'얀 스테인',
            u'Simon Stevin': u'시몬 스테빈',
            u'Jan Swammerdam': u'얀 스바메르담',
            u'Jan Pieterszoon Sweelinck': u'얀 피터르스존 스베일링크',
            u'Abel Tasman': u'아벌 타스만',
            u'Cornelis Petrus Tiele': u'코르넬리스 페트뤼스 틸러',
            u'Tiësto': u'티에스토',
            u'Jan Tinbergen': u'얀 틴베르헌',
            u'Nikolaas Tinbergen': u'니콜라스 틴베르헌',
            u'Mark Tuitert': u'마르크 타위터르트',
            u'Gerard Unger': u'헤라르트 윙어르',
            u'Joop den Uyl': u'요프 덴아윌',
            u'Rafaël van der Vaart': u'라파엘 판데르파르트',
            u'Adriaen van de Velde': u'아드리안 판더펠더',
            u'Marleen Veldhuis': u'마를레인 펠드하위스',
            u'Martinus Veltman': u'마르티뉘스 펠트만',
            u'Esther Vergeer': u'에스터르 페르헤이르',
            u'Paul Verhoeven': u'파울 페르후번',
            u'Johannes Vermeer': u'요하네스 페르메이르',
            u'Albert Verwey': u'알버르트 페르베이',
            u'Joost van den Vondel': u'요스트 판덴폰덜',
            u'Marianne Vos': u'마리아너 포스',
            u'Hugo de Vries': u'휘호 더프리스',
            u'Johannes Diderik van der Waals': u'요하네스 디데릭 판데르발스',
            u'Maarten van der Weijden': u'마르턴 판데르베이던',
            u'Jan Weltevree': u'얀 벨테브레이',
            u'Rogier van der Weyden': u'로히어르 판데르베이던',
            u'Geert Wilders': u'헤이르트 빌더르스',
            u'Adriaan Willaert': u'아드리안 빌라르트',
            u'Willem-Alexander Claus George Ferdinand':
            u'빌럼알렉산더르 클라우스 헤오르허 페르디난트',
            u'Michael Dudok de Wit': u'미카엘 뒤독 더빗',
            u'Johan de Witt': u'요한 더빗',
            u'Joost Wolfswinkel': u'요스트 볼프스빙컬',
            u'Ireen Wüst': u'이레인 뷔스트',
            u'Gerrit Zalm': u'헤릿 잘름',
            u'Pieter Zeeman': u'피터르 제이만',
            u'Frits Zernike': u'프리츠 제르니커',
            u'Joop Zoetemelk': u'요프 주테멜크',
        })

    def test_places(self):
        self.assert_examples({
            u'Almelo': u'알멜로',
            u'Alphen aan den Rijn': u'알펀안덴레인',
            u'Ameland': u'아멜란트',
            u'Amersfoort': u'아메르스포르트',
            u'Amstelveen': u'암스텔베인',
            u'Amsterdam': u'암스테르담',
            u'Andelst': u'안델스트',
            u'Apeldoorn': u'아펠도른',
            u'Appingedam': u'아핑에담',
            u'Arnhem': u'아른험',
            u'Assen': u'아선',
            u'Asten': u'아스턴',
            u'Barneveld': u'바르네벨트',
            u'Bedum': u'베뒴',
            u'Beilen': u'베일런',
            u'Bergen op Zoom': u'베르헌옵좀',
            u'Berkel': u'베르컬',
            u'Berkhout': u'베르크하우트',
            u'Best': u'베스트',
            u'Beverwijk': u'베베르베이크',
            u'Birdaard': u'비르다르트',
            u'Bolsward': u'볼스바르트',
            u'Borne': u'보르너',
            u'Boxtel': u'복스털',
            u'Breda': u'브레다',
            u'Breskens': u'브레스컨스',
            u'Burgh-Haamstede': u'뷔르흐함스테더',
            u'Capelle aan de Ijssel': u'카펠러안더에이설',
            u'Castricum': u'카스트리큄',
            u'Coevorden': u'쿠보르던',
            u'Creil': u'크레일',
            u'Culemborg': u'퀼렘보르흐',
            u'Delfzijl': u'델프제일',
            u'Den Bosch': u'덴보스',
            u'Den Burg': u'덴뷔르흐',
            u'Den Haag': u'덴하흐',
            u'Den Helder': u'덴헬더르',
            u'Deventer': u'데벤터르',
            u'Diremond': u'디레몬트',
            u'Doesburg': u'두스뷔르흐',
            u'Doetinchem': u'두틴험',
            u'Dokkum': u'도큄',
            u'Dordrecht': u'도르드레흐트',
            u'Drachten': u'드라흐턴',
            u'Drenthe': u'드렌터',
            u'Dronten': u'드론턴',
            u'Ede': u'에더',
            u'Eemskanaal': u'에임스카날',
            u'Eenrum': u'에인륌',
            u'Eibergen': u'에이베르헌',
            u'Eindhoven': u'에인트호번',
            u'Emmeloord': u'에멜로르트',
            u'Enkhuizen': u'엥크하위전',
            u'Enschede': u'엔스헤데',
            u'Erp': u'에르프',
            u'Etten-Leur': u'에턴뢰르',
            u'Ferwerd': u'페르버르트',
            u'Franeker': u'프라네커르',
            u'Gelderland': u'헬데를란트',
            u'Gorinchem': u'호린험',
            u'Gouda': u'하우다',
            u'Haarlem': u'하를럼',
            u'Halsteren': u'할스테런',
            u'Hapert': u'하퍼르트',
            u'Hardenberg': u'하르덴베르흐',
            u'Harderwijk': u'하르데르베이크',
            u'Harlingen': u'하를링언',
            u'Heerde': u'헤이르더',
            u'Heerenveen': u'헤이렌베인',
            u'Heerhugowaard': u'헤이르휘호바르트',
            u'Heerlen': u'헤이를런',
            u'Hellevoetsluis': u'헬레부츨라위스',
            u'Hengelo': u'헹엘로',
            u'Herkenbosch': u'헤르켄보스',
            u'Hillegom': u'힐레홈',
            u'Hilversum': u'힐베르쉼',
            u'Hoek van Holland': u'훅판홀란트',
            u'Hollum': u'홀륌',
            u'Hoogerheide': u'호헤르헤이더',
            u'Hoogeveen': u'호헤베인',
            u'Hoogezand-Sappemeer': u'호헤잔트사페메이르',
            u'Hoog-Keppel': u'호흐케펄',
            u'Hoorn': u'호른',
            u'IJmuiden': u'에이마위던',
            u'IJsselmeer': u'에이설메이르',
            u'Kampen': u'캄펀',
            u'Katwijk aan Zee': u'카트베이크안제이',
            u'Kerkrade': u'케르크라더',
            u'Kessel': u'케설',
            u'Kloosterhaar': u'클로스테르하르',
            u'Kollum': u'콜륌',
            u'Koudekerke': u'카우데케르커',
            u'Kraggenburg': u'크라헨뷔르흐',
            u'Lauwersmeer': u'라우에르스메이르',
            u'Leeuwarden': u'레이우아르던',
            u'Leiden': u'레이던',
            u'Lelystad': u'렐리스타트',
            u'Luyksgestel': u'라위크스헤스털',
            u'Maarssen': u'마르선',
            u'Maastricht': u'마스트리흐트',
            u'Markermeer': u'마르케르메이르',
            u'Marsdiep': u'마르스딥',
            u'Mechelen': u'메헬런',
            u'Meppel': u'메펄',
            u'Middelburg': u'미델뷔르흐',
            u'Middelharnis': u'미델하르니스',
            u'Naarden': u'나르던',
            u'Nieuwegein': u'니우에헤인',
            u'Nieuwe Niedorp': u'니우어니도르프',
            u'Nijkerk': u'네이커르크',
            u'Nijverdal': u'네이베르달',
            u'Noord-Brabant': u'노르트브라반트',
            u'Noord-Holland': u'노르트홀란트',
            u'Oenkerk': u'웅커르크',
            u'Oldenzaal': u'올덴잘',
            u'Ommen': u'오먼',
            u'Oosterhout': u'오스테르하우트',
            u'Oosterschelde': u'오스테르스헬더',
            u'Oost-Vlieland': u'오스트플릴란트',
            u'Oss': u'오스',
            u'Philippine': u'필리피너',
            u'Purmerend': u'퓌르메런트',
            u'Raalte': u'랄터',
            u'Roermond': u'루르몬트',
            u'Roordahuizum': u'로르다하위쥠',
            u'Roosendaal': u'로센달',
            u'Schagen': u'스하헌',
            u'Scharendijke': u'스하렌데이커',
            u'Schiermonnikoog': u'스히르모니코흐',
            u'Schoonhoven': u'스혼호번',
            u'’s-Gravenhage': u"'스흐라벤하허",
            u'’s-Hertogenbosch': u"'스헤르토헨보스",
            u'Sittarad': u'시타라트',
            u'Sloten': u'슬로턴',
            u'Sluis': u'슬라위스',
            u'Sneek': u'스네이크',
            u'Spijkenisse': u'스페이케니서',
            u'Steeswijk': u'스테이스베이크',
            u'Stein': u'스테인',
            u'Terneuzen': u'테르뇌전',
            u'Terschelling': u'테르스헬링',
            u'Texel': u'텍설',
            u'Tiel': u'틸',
            u'Tilburg': u'틸뷔르흐',
            u'Torenberg': u'토렌베르흐',
            u'Uden': u'위던',
            u'Uithuizen': u'아위트하위전',
            u'Urk': u'위르크',
            u'Valkenswaard': u'팔켄스바르트',
            u'Veendam': u'페인담',
            u'Veenendal': u'페이넨달',
            u'Veldhoven': u'펠트호번',
            u'Vlaardingen': u'플라르딩언',
            u'Vlieland': u'플릴란트',
            u'Vlissingen': u'플리싱언',
            u'Vriezenveen': u'프리젠베인',
            u'Waal': u'발',
            u'Waalwijk': u'발베이크',
            u'Wadden': u'바던',
            u'Waddeneilanden': u'바데네일란던',
            u'Waddenzee': u'바덴제이',
            u'Waddinxveen': u'바딩크스베인',
            u'Wageningen': u'바헤닝언',
            u'Wanroij': u'반로이',
            u'Weert': u'베이르트',
            u'Westerschelde': u'베스테르스헬더',
            u'Westkapelle': u'베스트카펠러',
            u'West-Terschelling': u'베스트테르스헬링',
            u'Wieringerwerf': u'비링에르버르프',
            u'Wijchen': u'베이헌',
            u'Winterswijk': u'빈테르스베이크',
            u'Witmarsum': u'비트마르쉼',
            u'Wolvega': u'볼베하',
            u'Wonschoten': u'본스호턴',
            u'Zaandam': u'잔담',
            u'Zandvoort': u'잔드보르트',
            u'Zevenaar': u'제베나르',
            u'Zevenbergen': u'제벤베르헌',
            u'Zutphan': u'쥣판',
            u'Zwolle': u'즈볼러',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            u'brik': u'브릭',
            u'Delft Stedelijk': u'델프트 스테델레이크',
            u'De Stijl': u'더스테일',
            u'gulden': u'휠던',
            u'Elfstedentocht': u'엘프스테덴토흐트',
        })

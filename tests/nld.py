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
        #    u'Lyonnet': u'리오넷',
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
        #    u'Nicolaas': u'니콜라스 ',
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
            u'Ijssel': u'에이설',
            u'Huizinga': u'하위징아',
        #    u'Zuid-Holland': u'자위트홀란트',
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
        g, ch는 ‘ㅎ'으로 적되, 차용어의 경우에는 해당 언어의 발음에 따라 적는다.
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
        #    u'casuïst': u'카수이스트',
            u'drieëntwintig': u'드리엔트빈터흐',
        })

    def test_people(self):
        self.assert_examples({
            u'Naomi van As': u'나오미 판아스',
            u'Marco van Basten': u'마르코 판바스턴',
            u'Vincent van Gogh': u'빈센트 반고흐',
            u'Rem Koolhaas': u'렘 콜하스',
            u'Teun de Nooijer': u'퇸 더노이여르',
            u'Johannes Diderik van der Waals': u'요하네스 디데릭 판데르발스',
        })

    def test_places(self):
        self.assert_examples({
            u'Alphen aan den Rijn': u'알펀안덴레인',
            u'Amsterdam': u'암스테르담',
            u'Den Bosch': u'덴보스',
            u'Den Haag': u'덴하흐',
        })

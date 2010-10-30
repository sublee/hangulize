# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class DutchTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0220.jsp """

    def setUp(self):
        from hangulize.langs.nl import Dutch
        self.lang = Dutch()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0118.jsp """
        assert u'보르스트' == self.hangulize(u'Borst')
        assert u'브람' == self.hangulize(u'Bram')
        assert u'야코프' == self.hangulize(u'Jacob')
        assert u'캄펀' == self.hangulize(u'Campen')
        assert u'니콜라스' == self.hangulize(u'Nicolaas')
        assert u'토픽' == self.hangulize(u'topic')
        assert u'스크뤼펄' == self.hangulize(u'scrupel')
        assert u'시안' == self.hangulize(u'cyaan')
        assert u'세일런' == self.hangulize(u'Ceelen')
        assert u'폴허르' == self.hangulize(u'Volcher')
        assert u'위트레흐트' == self.hangulize(u'Utrecht')
        assert u'델프트' == self.hangulize(u'Delft')
        assert u'엣하르' == self.hangulize(u'Edgar')
        assert u'헨드릭' == self.hangulize(u'Hendrik')
        assert u'헬몬트' == self.hangulize(u'Helmond')
        assert u'플레볼란트' == self.hangulize(u'Flevoland')
        assert u'흐라프' == self.hangulize(u'Graaf')
        assert u'후스' == self.hangulize(u'Goes')
        assert u'림뷔르흐' == self.hangulize(u'Limburg')
        assert u'헤이네컨' == self.hangulize(u'Heineken')
        assert u'헨드릭' == self.hangulize(u'Hendrik')
        assert u'용킨트' == self.hangulize(u'Jongkind')
        assert u'얀' == self.hangulize(u'Jan')
        assert u'예룬' == self.hangulize(u'Jeroen')
        assert u'콕' == self.hangulize(u'Kok')
        assert u'알크마르' == self.hangulize(u'Alkmaar')
        assert u'지릭제이' == self.hangulize(u'Zierikzee')
        assert u'크발리테이트' == self.hangulize(u'kwaliteit')
        assert u'크벨런' == self.hangulize(u'kwellen')
        assert u'크비탄시' == self.hangulize(u'kwitantie')
        assert u'라소' == self.hangulize(u'Lasso')
        assert u'프리슬란트' == self.hangulize(u'Friesland')
        assert u'사벌' == self.hangulize(u'sabel')
        assert u'메이르선' == self.hangulize(u'Meerssen')
        assert u'잘름' == self.hangulize(u'Zalm')
        assert u'네이메헌' == self.hangulize(u'Nijmegen')
        assert u'얀선' == self.hangulize(u'Jansen')
        assert u'잉어' == self.hangulize(u'Inge')
        assert u'흐로닝언' == self.hangulize(u'Groningen')
        assert u'페퍼르' == self.hangulize(u'Peper')
        assert u'캅테인' == self.hangulize(u'Kapteyn')
        assert u'코프만스' == self.hangulize(u'Koopmans')
        assert u'로테르담' == self.hangulize(u'Rotterdam')
        assert u'아서르' == self.hangulize(u'Asser')
        assert u'스피노자' == self.hangulize(u'Spinoza')
        assert u'할스' == self.hangulize(u'Hals')
        assert u'스히폴' == self.hangulize(u'Schiphol')
        assert u'에스허르' == self.hangulize(u'Escher')
        assert u'티피스' == self.hangulize(u'typisch')
        assert u'샬' == self.hangulize(u'sjaal')
        assert u'하위셔' == self.hangulize(u'huisje')
        assert u'람시' == self.hangulize(u'ramsj')
        assert u'페티시' == self.hangulize(u'fetisj')
        assert u'틴베르헌' == self.hangulize(u'Tinbergen')
        assert u'헤릿' == self.hangulize(u'Gerrit')
        assert u'페트뤼스' == self.hangulize(u'Petrus')
        assert u'아르천' == self.hangulize(u'Aartsen')
        assert u'베이츠' == self.hangulize(u'Beets')
        assert u'펠트만' == self.hangulize(u'Veltman')
        assert u'에인트호번' == self.hangulize(u'Einthoven')
        assert u'벨테브레이' == self.hangulize(u'Weltevree')
        assert u'빔' == self.hangulize(u'Wim')
        assert u'시안' == self.hangulize(u'cyaan')
        #assert u'리오넷' == self.hangulize(u'Lyonnet')
        assert u'티피스' == self.hangulize(u'typisch')
        assert u'페르베이' == self.hangulize(u'Verwey')
        assert u'제이만' == self.hangulize(u'Zeeman')
        assert u'하위징아' == self.hangulize(u'Huizinga')
        assert u'아서르' == self.hangulize(u'Asser')
        assert u'프란스' == self.hangulize(u'Frans')
        assert u'에흐몬트' == self.hangulize(u'Egmont')
        assert u'프레데릭' == self.hangulize(u'Frederik')
        assert u'헤이네컨' == self.hangulize(u'Heineken')
        assert u'뤼버르스' == self.hangulize(u'Lubbers')
        assert u'캄펀' == self.hangulize(u'Campen')
        #assert u'니콜라스 ' == self.hangulize(u'Nicolaas')
        assert u'토비아스' == self.hangulize(u'Tobias')
        assert u'피터르' == self.hangulize(u'Pieter')
        assert u'프리스' == self.hangulize(u'Vries')
        assert u'오너스' == self.hangulize(u'Onnes')
        assert u'폰덜' == self.hangulize(u'Vondel')
        assert u'부르' == self.hangulize(u'Boer')
        assert u'부르하버' == self.hangulize(u'Boerhaave')
        assert u'위트레흐트' == self.hangulize(u'Utrecht')
        assert u'페트뤼스' == self.hangulize(u'Petrus')
        assert u'외로포르트' == self.hangulize(u'Europort')
        assert u'되르너' == self.hangulize(u'Deurne')
        assert u'뤼' == self.hangulize(u'ruw')
        assert u'뒤언' == self.hangulize(u'duwen')
        assert u'에위언' == self.hangulize(u'Euwen')
        assert u'바우츠' == self.hangulize(u'Bouts')
        assert u'바우만' == self.hangulize(u'Bouwman')
        assert u'파울' == self.hangulize(u'Paul')
        assert u'라우에르스메이르' == self.hangulize(u'Lauwersmeer')
        assert u'헤이커' == self.hangulize(u'Heike')
        assert u'볼케스테인' == self.hangulize(u'Bolkestein')
        assert u'에이설' == self.hangulize(u'Ijssel')
        assert u'하위징아' == self.hangulize(u'Huizinga')
        #assert u'자위트홀란트' == self.hangulize(u'Zuid-Holland')
        assert u'바위스' == self.hangulize(u'Buys')
        assert u'드라이언' == self.hangulize(u'draaien')
        assert u'프라이' == self.hangulize(u'fraai')
        assert u'자이트' == self.hangulize(u'zaait')
        assert u'마이커스' == self.hangulize(u'Maaikes')
        assert u'보이스만' == self.hangulize(u'Booisman')
        assert u'호이터스' == self.hangulize(u'Hooites')
        assert u'부잉아' == self.hangulize(u'Boeijinga')
        assert u'무이터' == self.hangulize(u'moeite')
        assert u'레이우엔훅' == self.hangulize(u'Leeuwenhoek')
        assert u'메이우어스' == self.hangulize(u'Meeuwes')
        assert u'리우마' == self.hangulize(u'Lieuwma')
        assert u'리우어르스' == self.hangulize(u'Rieuwers')

    def test_1st(self):
        """제1항
        무성 파열음 p, t, k는 자음 앞이나 어말에 올 경우에는 각각 받침 ‘ㅂ, ㅅ, ㄱ'으로 적는다. 다만, 앞 모음이 이중 모음이거나 장모음(같은 모음을 겹쳐 적는 경우)인 경우와 앞이나 뒤의 자음이 유음이나 비음인 경우에는 ‘프, 트, 크'로 적는다.
        """
        assert u'빗' == self.hangulize(u'Wit')
        assert u'헤닙' == self.hangulize(u'Gennip')
        assert u'캅테인' == self.hangulize(u'Kapteyn')
        assert u'셉템버르' == self.hangulize(u'september')
        assert u'페트뤼스' == self.hangulize(u'Petrus')
        assert u'아르카덜트' == self.hangulize(u'Arcadelt')
        assert u'호프' == self.hangulize(u'Hoop')
        assert u'에이크만' == self.hangulize(u'Eijkman')

    def test_2nd(self):
        """제2항
        유성 파열음 b, d가 어말에 올 경우에는 각각 ‘프, 트'로 적고, 어중에 올 경우에는 앞이나 뒤의 자음이 유음이나 비음인 경우와 앞 모음이 이중모음이거나 장모음(같은 모음을 겹쳐 적는 경우)인 경우에는 ‘브, 드'로 적는다. 그 외에는 모두 받침 ‘ㅂ, ㅅ'으로 적는다.
        """
        assert u'브람' == self.hangulize(u'Bram')
        assert u'헨드릭' == self.hangulize(u'Hendrik')
        assert u'야코프' == self.hangulize(u'Jakob')
        assert u'엣하르' == self.hangulize(u'Edgar')
        assert u'제일란트' == self.hangulize(u'Zeeland')
        assert u'쿤라트' == self.hangulize(u'Koenraad')

    def test_3rd(self):
        """제3항
        v가 어두에 올 경우에는 ‘ㅍ, 프'로 적고, 그 외에는 모두 ‘ㅂ, 브'로 적는다.
        """
        assert u'펠트만' == self.hangulize(u'Veltman')
        assert u'프리스' == self.hangulize(u'Vries')
        assert u'흐라버' == self.hangulize(u'Grave')
        assert u'벨테브레이' == self.hangulize(u'Weltevree')

    def test_4th(self):
        """제4항
        c는 차용어에 쓰이므로 해당 언어의 발음에 따라 ‘ㅋ'이나 ‘ㅅ'으로 적는다.
        """
        assert u'니콜라스' == self.hangulize(u'Nicolaas')
        assert u'헨드리퀴스' == self.hangulize(u'Hendricus')
        assert u'시안' == self.hangulize(u'cyaan')
        assert u'프란시스퀴스' == self.hangulize(u'Franciscus')

    def test_5th(self):
        """제5항
        g, ch는 ‘ㅎ'으로 적되, 차용어의 경우에는 해당 언어의 발음에 따라 적는다.
        """
        # gulden휠던
        assert u'하흐' == self.hangulize(u'Haag')
        assert u'호흐' == self.hangulize(u'Hooch')
        assert u'폴허르' == self.hangulize(u'Volcher')
        assert u'외젠' == self.hangulize(u'Eugene')
        assert u'미카엘' == self.hangulize(u'Michael')

    def test_6th(self):
        """제6항
        -tie는 ‘시'로 적는다.
        """
        assert u'나시' == self.hangulize(u'natie')
        assert u'폴리시' == self.hangulize(u'politie')

    def test_7th(self):
        """제7항
        어중의 l이 모음 앞에 오거나 모음이 따르지 않는 비음 앞에 올 때에는 ‘?'로 적는다. 다만, 비음 뒤의 l은 모음 앞에 오더라도 ‘ㄹ'로 적는다.
        """
        assert u'틸러' == self.hangulize(u'Tiele')
        assert u'잘름' == self.hangulize(u'Zalm')
        assert u'베를라허' == self.hangulize(u'Berlage')
        assert u'펜로' == self.hangulize(u'Venlo')

    def test_8th(self):
        """제8항: nk
        k 앞에 오는 n은 받침 ‘ㅇ'으로 적는다. 
        """
        assert u'프랑크' == self.hangulize(u'Frank')
        assert u'히딩크' == self.hangulize(u'Hiddink')
        assert u'벵크' == self.hangulize(u'Benk')
        assert u'볼프스빙컬' == self.hangulize(u'Wolfswinkel')

    def test_9th(self):
        """제9항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다.
        """
        assert u'호베마' == self.hangulize(u'Hobbema')
        assert u'발롯' == self.hangulize(u'Ballot')
        assert u'에먼' == self.hangulize(u'Emmen')
        assert u'헤닙' == self.hangulize(u'Gennip')

    def test_10th(self):
        """제10항
        e는 ‘에'로 적는다. 다만, 이음절 이상에서 마지막 음절에 오는 e와 어말의 e는 모두 ‘어'로 적는다.
        """
        assert u'데니스' == self.hangulize(u'Dennis')
        assert u'브레다' == self.hangulize(u'Breda')
        assert u'스테빈' == self.hangulize(u'Stevin')
        assert u'페터르' == self.hangulize(u'Peter')
        assert u'헤이네컨' == self.hangulize(u'Heineken')
        assert u'캄펀' == self.hangulize(u'Campen')

    def test_11st(self):
        """제11항
        같은 모음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만 ee는 ‘에이'로 적는다.
        """
        assert u'호흐' == self.hangulize(u'Hooch')
        assert u'몬드리안' == self.hangulize(u'Mondriaan')
        assert u'케이스' == self.hangulize(u'Kees')
        assert u'메이르선' == self.hangulize(u'Meerssen')

    def test_12nd(self):
        """제12항
        -ig는 ‘어흐'로 적는다.
        """
        assert u'타흐터흐' == self.hangulize(u'tachtig')
        assert u'하르터흐' == self.hangulize(u'hartig')

    def test_13rd(self):
        """제13항
        -berg는 ‘베르흐'로 적는다.
        """
        assert u'다위센베르흐' == self.hangulize(u'Duisenberg')
        assert u'멩엘베르흐' == self.hangulize(u'Mengelberg')

    def test_14th(self):
        """제14항
        over-는 ‘오버르'로 적는다.
        """
        assert u'오버레이설' == self.hangulize(u'Overijssel')
        assert u'오버르콤스트' == self.hangulize(u'overkomst')

    def test_15th(self):
        """제15항
        모음 è, é, ê, ë는 ‘에'로 적고, ï 는 ‘이' 로 적는다.
        """
        assert u'카레' == self.hangulize(u'carré')
        #assert u'카수이스트' == self.hangulize(u'casuïst')
        assert u'드리엔트빈터흐' == self.hangulize(u'drieëntwintig')

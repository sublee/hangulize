# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.sh import SerboCroatian


class SerboCroatianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0210.jsp """

    lang = SerboCroatian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0108.jsp """
        assert u'보그' == self.hangulize(u'bog')
        assert u'드로브냐크' == self.hangulize(u'drobnjak')
        assert u'포그레브' == self.hangulize(u'pogreb')
        assert u'치가라' == self.hangulize(u'cigara')
        assert u'노바츠' == self.hangulize(u'novac')
        assert u'첼리크' == self.hangulize(u'čelik')
        assert u'토치카' == self.hangulize(u'točka')
        assert u'콜라치' == self.hangulize(u'kolač')
        assert u'나치' == self.hangulize(u'naći')
        assert u'세스트리치' == self.hangulize(u'sestrić')
        assert u'데스노' == self.hangulize(u'desno')
        assert u'드르보' == self.hangulize(u'drvo')
        assert u'메드베드' == self.hangulize(u'medved')
        assert u'제프' == self.hangulize(u'džep')
        assert u'나루지바' == self.hangulize(u'narudžba')
        #assert u'주라지' == self.hangulize(u'Ðurađ')
        assert u'파사다' == self.hangulize(u'fasada')
        assert u'키플라' == self.hangulize(u'kifla')
        assert u'샤라프' == self.hangulize(u'šaraf')
        assert u'고스트' == self.hangulize(u'gost')
        assert u'두그메' == self.hangulize(u'dugme')
        assert u'크루그' == self.hangulize(u'krug')
        assert u'히탄' == self.hangulize(u'hitan')
        assert u'샤흐' == self.hangulize(u'šah')
        assert u'코리스트' == self.hangulize(u'korist')
        assert u'크루그' == self.hangulize(u'krug')
        assert u'야스투크' == self.hangulize(u'jastuk')
        assert u'레보' == self.hangulize(u'levo')
        assert u'발콘' == self.hangulize(u'balkon')
        assert u'샬' == self.hangulize(u'šal')
        assert u'레토' == self.hangulize(u'ljeto')
        assert u'파술' == self.hangulize(u'pasulj')
        assert u'말로' == self.hangulize(u'malo')
        assert u'므노고' == self.hangulize(u'mnogo')
        assert u'오삼' == self.hangulize(u'osam')
        assert u'노스' == self.hangulize(u'nos')
        assert u'반카' == self.hangulize(u'banka')
        assert u'로만' == self.hangulize(u'loman')
        assert u'네고시' == self.hangulize(u'Njegoš')
        assert u'스비반' == self.hangulize(u'svibanj')
        assert u'페타' == self.hangulize(u'peta')
        assert u'옵슈티나' == self.hangulize(u'opština')
        assert u'레프' == self.hangulize(u'lep')
        assert u'리바' == self.hangulize(u'riba')
        assert u'토르바' == self.hangulize(u'torba')
        assert u'미르' == self.hangulize(u'mir')
        assert u'세담' == self.hangulize(u'sedam')
        assert u'포슬레' == self.hangulize(u'posle')
        assert u'글라스' == self.hangulize(u'glas')
        assert u'샬' == self.hangulize(u'šal')
        assert u'블라스니슈트보' == self.hangulize(u'vlasništvo')
        assert u'브로시' == self.hangulize(u'broš')
        assert u'텔로' == self.hangulize(u'telo')
        assert u'오스트르보' == self.hangulize(u'ostrvo')
        assert u'푸트' == self.hangulize(u'put')
        assert u'바트라' == self.hangulize(u'vatra')
        assert u'올로브카' == self.hangulize(u'olovka')
        assert u'프롤리브' == self.hangulize(u'proliv')
        assert u'자보이' == self.hangulize(u'zavoj')
        assert u'포즈노' == self.hangulize(u'pozno')
        assert u'오브라즈' == self.hangulize(u'obraz')
        assert u'제나' == self.hangulize(u'žena')
        assert u'이즐로주바' == self.hangulize(u'izložba')
        assert u'무주' == self.hangulize(u'muž')
        assert u'포야스' == self.hangulize(u'pojas')
        assert u'자보이' == self.hangulize(u'zavoj')
        assert u'오델로' == self.hangulize(u'odjelo')
        assert u'바카르' == self.hangulize(u'bakar')
        assert u'체브' == self.hangulize(u'cev')
        assert u'딤' == self.hangulize(u'dim')
        assert u'몰림' == self.hangulize(u'molim')
        assert u'주바르' == self.hangulize(u'zubar')
    
    def test_1st(self):
        """제1항: k, p
        k, p는 어말과 유성 자음 앞에서는 '으'를 붙여 적고, 무성 자음 앞에서는
        받침으로 적는다.
        """
        assert u'야스투크' == self.hangulize(u'jastuk')
        assert u'야스투크' == self.hangulize(u'јастук')
        assert u'옵슈티나' == self.hangulize(u'opština')
        assert u'옵슈티나' == self.hangulize(u'општина')

    def test_2nd(self):
        """제2항: l
        어중의 l이 모음 앞에 올 때에는 'ㄹㄹ'로 적는다.
        """
        assert u'쿨라' == self.hangulize(u'kula')
        assert u'쿨라' == self.hangulize(u'кула')

    def test_3rd(self):
        """제3항: m
        어두의 m이 l, r, n 앞에 오거나 어중의 m이 r 앞에 올 때에는 '으'를
        붙여 적는다.
        """
        assert u'믈라드' == self.hangulize(u'mlad')
        assert u'믈라드' == self.hangulize(u'млад')
        assert u'므노고' == self.hangulize(u'mnogo')
        assert u'므노고' == self.hangulize(u'много')
        assert u'스므르트' == self.hangulize(u'smrt')
        assert u'스므르트' == self.hangulize(u'смрт')

    def test_4th(self):
        """제4항: š
        š는 자음 앞에서는 '슈', 어말에서는 '시'로 적는다.
        """
        assert u'슐리보비차' == self.hangulize(u'šljivovica')
        assert u'슐리보비차' == self.hangulize(u'шљивовица')
        assert u'니시' == self.hangulize(u'Niš')
        assert u'니시' == self.hangulize(u'Ниш')

    def test_5th(self):
        """제5항
        자음에 '예'가 결합되는 경우에는 '예' 대신에 '에'로 적는다. 다만,
        자음이 'ㅅ'인 경우에는 '셰'로 적는다.
        """
        assert u'베드로' == self.hangulize(u'bjedro')
        assert u'베드로' == self.hangulize(u'бједро')
        assert u'셰들로' == self.hangulize(u'sjedlo')
        assert u'셰들로' == self.hangulize(u'сједло')


# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.it import Italian


class ItalianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0205.jsp """

    lang = Italian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0103.jsp """
        assert u'볼로냐' == self.hangulize(u'Bologna')
        assert u'브라보' == self.hangulize(u'bravo')
        assert u'코모' == self.hangulize(u'Como')
        assert u'시칠리아' == self.hangulize(u'Sicilia')
        assert u'크레도' == self.hangulize(u'credo')
        assert u'피노키오' == self.hangulize(u'Pinocchio')
        assert u'케루비노' == self.hangulize(u'cherubino')
        assert u'단테' == self.hangulize(u'Dante')
        assert u'드리차' == self.hangulize(u'drizza')
        assert u'피렌체' == self.hangulize(u'Firenze')
        assert u'프레도' == self.hangulize(u'freddo')
        assert u'갈릴레오' == self.hangulize(u'Galileo')
        assert u'제노바' == self.hangulize(u'Genova')
        assert u'글로리아' == self.hangulize(u'gloria')
        assert u'안노' == self.hangulize(u'hanno')
        assert u'오' == self.hangulize(u'oh')
        assert u'밀라노' == self.hangulize(u'Milano')
        assert u'라르고' == self.hangulize(u'largo')
        assert u'팔코' == self.hangulize(u'palco')
        assert u'마키아벨리' == self.hangulize(u'Macchiavelli')
        assert u'맘마' == self.hangulize(u'mamma')
        assert u'캄파넬라' == self.hangulize(u'Campanella')
        assert u'네로' == self.hangulize(u'Nero')
        assert u'안나' == self.hangulize(u'Anna')
        assert u'디베르티멘토' == self.hangulize(u'divertimento')
        assert u'피사' == self.hangulize(u'Pisa')
        assert u'프리마' == self.hangulize(u'prima')
        assert u'콴도' == self.hangulize(u'quando')
        assert u'퀘토' == self.hangulize(u'queto')
        assert u'로마' == self.hangulize(u'Roma')
        assert u'마르코니' == self.hangulize(u'Marconi')
        assert u'소렌토' == self.hangulize(u'Sorrento')
        assert u'아스마' == self.hangulize(u'asma')
        assert u'사소' == self.hangulize(u'sasso')
        assert u'토리노' == self.hangulize(u'Torino')
        assert u'트란네' == self.hangulize(u'tranne')
        assert u'비바체' == self.hangulize(u'Vivace')
        assert u'마노브라' == self.hangulize(u'manovra')
        assert u'노체' == self.hangulize(u'nozze')
        assert u'만칸차' == self.hangulize(u'mancanza')
        assert u'아비투로' == self.hangulize(u'abituro')
        assert u'카프라' == self.hangulize(u'capra')
        assert u'에르타' == self.hangulize(u'erta')
        assert u'파드로네' == self.hangulize(u'padrone')
        assert u'인파미아' == self.hangulize(u'infamia')
        assert u'마니카' == self.hangulize(u'manica')
        assert u'오블리오' == self.hangulize(u'oblio')
        assert u'포에티카' == self.hangulize(u'poetica')
        assert u'우바' == self.hangulize(u'uva')
        assert u'스푸마' == self.hangulize(u'spuma')

    def test_1st(self):
        """제1항: gl
        i 앞에서는 'ㄹㄹ'로 적고, 그 밖의 경우에는 '글ㄹ'로 적는다.
        """
        assert u'팔리아' == self.hangulize(u'paglia')
        assert u'엘리' == self.hangulize(u'egli')
        assert u'글로리아' == self.hangulize(u'gloria')
        assert u'글로사' == self.hangulize(u'glossa')

    def test_2nd(self):
        """제2항: gn
        뒤따르는 모음과 합쳐 '냐', '녜', '뇨', '뉴', '니'로 적는다.
        """
        assert u'몬타냐' == self.hangulize(u'montagna')
        assert u'녜이스' == self.hangulize(u'gneiss')
        assert u'뇨코' == self.hangulize(u'gnocco')
        assert u'뉴' == self.hangulize(u'gnu')
        assert u'오니' == self.hangulize(u'ogni')

    def test_3rd(self):
        """제3항: sc
        sce는 '셰'로, sci는 '시'로 적고, 그 밖의 경우에는 '스ㅋ'으로 적는다.
        """
        assert u'크레셴도' == self.hangulize(u'crescendo')
        assert u'시볼로' == self.hangulize(u'scivolo')
        assert u'토스카' == self.hangulize(u'Tosca')
        assert u'스쿠도' == self.hangulize(u'scudo')

    def test_4th(self):
        """제4항
        같은 자음이 겹쳤을 때에는 겹치지 않은 경우와 같이 적는다. 다만, -mm-,
        -nn-의 경우는 'ㅁㅁ', 'ㄴㄴ'으로 적는다.
        """
        assert u'푸치니' == self.hangulize(u'Puccini')
        assert u'부파' == self.hangulize(u'buffa')
        assert u'알레그레토' == self.hangulize(u'allegretto')
        assert u'카로' == self.hangulize(u'carro')
        assert u'로소' == self.hangulize(u'rosso')
        assert u'메초' == self.hangulize(u'mezzo')
        assert u'곰마' == self.hangulize(u'gomma')
        assert u'비스논노' == self.hangulize(u'bisnonno')

    def test_5th(self):
        """제5항: c, g
        1. c와 g는 e, i 앞에서 각각 'ㅊ', 'ㅈ'으로 적는다.
        2. c와 g 다음에 ia, io, iu가 올 때에는 각각 '차, 초, 추',
           '자, 조, 주'로 적는다.
        """
        assert u'체네레' == self.hangulize(u'cenere')
        assert u'제네레' == self.hangulize(u'genere')
        assert u'치마' == self.hangulize(u'cima')
        assert u'지타' == self.hangulize(u'gita')
        assert u'카차' == self.hangulize(u'caccia')
        assert u'미초' == self.hangulize(u'micio')

    def test_6th(self):
        """제6항: qu
        qu는 뒤따르는 모음과 합쳐 '콰, 퀘, 퀴' 등으로 적는다. 다만, o 앞에서는
        '쿠'로 적는다.
        """
        assert u'소콰드로' == self.hangulize(u'soqquadro')
        assert u'퀠로' == self.hangulize(u'quello')
        assert u'퀴에토' == self.hangulize(u'quieto')
        assert u'쿠오타' == self.hangulize(u'quota')

    def test_7th(self):
        """제7항: l, ll
        어말 또는 자음 앞의 l, ll은 받침으로 적고, 어중의 l, ll이 모음 앞에
        올 때에는 'ㄹㄹ'로 적는다.
        """
        assert u'솔' == self.hangulize(u'sol')
        assert u'폴카' == self.hangulize(u'polca')
        assert u'카를로' == self.hangulize(u'Carlo')
        assert u'퀠로' == self.hangulize(u'quello')

    def test_hangulize(self):
        assert u'이탈리아' == self.hangulize(u'italia')
        assert u'인노첸티' == self.hangulize(u'Innocenti')
        assert u'체리고토' == self.hangulize(u'Cerigotto')
        assert u'유벤투스' == self.hangulize(u'Juventus')
        assert u'스키아보니아' == self.hangulize(u'Schiavonia')
        assert u'폴리' == self.hangulize(u'Fogli')
        assert u'카라바조' == self.hangulize(u'Caravaggio')
        assert u'네포스' == self.hangulize(u'nephos')
        assert u'스보차키셰' == self.hangulize(u'sbozzacchisce')
        assert u'스칼렌게' == self.hangulize(u'Scalenghe')
        assert u'파브리치오' == self.hangulize(u'Fabrizio')
        assert u'안기아리' == self.hangulize(u'Anghiari')
        assert u'소콰드로' == self.hangulize(u'soqquadro')
        assert u'볼로냐' == self.hangulize(u'Bologna')
        assert u'포니니' == self.hangulize(u'Fognini')
        assert u'이냐치오' == self.hangulize(u'Ignazio')
        assert u'지로 디탈리아' == self.hangulize(u"Giro d'Italia")
        assert u'페르 라베니레 디탈리아' == \
               self.hangulize(u"per l'avvenire d'Italia")
        assert u'렉스' == self.hangulize(u'Rex')

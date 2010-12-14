# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ita import Italian


class ItalianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0205.jsp """

    lang = Italian()

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0103.jsp """
        self.assert_examples({
            u'Bologna': u'볼로냐',
            u'bravo': u'브라보',
            u'Como': u'코모',
            u'Sicilia': u'시칠리아',
            u'credo': u'크레도',
            u'Pinocchio': u'피노키오',
            u'cherubino': u'케루비노',
            u'Dante': u'단테',
            u'drizza': u'드리차',
            u'Firenze': u'피렌체',
            u'freddo': u'프레도',
            u'Galileo': u'갈릴레오',
            u'Genova': u'제노바',
            u'gloria': u'글로리아',
            u'hanno': u'안노',
            u'oh': u'오',
            u'Milano': u'밀라노',
            u'largo': u'라르고',
            u'palco': u'팔코',
            u'Macchiavelli': u'마키아벨리',
            u'mamma': u'맘마',
            u'Campanella': u'캄파넬라',
            u'Nero': u'네로',
            u'Anna': u'안나',
            u'divertimento': u'디베르티멘토',
            u'Pisa': u'피사',
            u'prima': u'프리마',
            u'quando': u'콴도',
            u'queto': u'퀘토',
            u'Roma': u'로마',
            u'Marconi': u'마르코니',
            u'Sorrento': u'소렌토',
            u'asma': u'아스마',
            u'sasso': u'사소',
            u'Torino': u'토리노',
            u'tranne': u'트란네',
            u'Vivace': u'비바체',
            u'manovra': u'마노브라',
            u'nozze': u'노체',
            u'mancanza': u'만칸차',
            u'abituro': u'아비투로',
            u'capra': u'카프라',
            u'erta': u'에르타',
            u'padrone': u'파드로네',
            u'infamia': u'인파미아',
            u'manica': u'마니카',
            u'oblio': u'오블리오',
            u'poetica': u'포에티카',
            u'uva': u'우바',
            u'spuma': u'스푸마',
        })

    def test_1st(self):
        """제1항: gl
        i 앞에서는 'ㄹㄹ'로 적고, 그 밖의 경우에는 '글ㄹ'로 적는다.
        """
        self.assert_examples({
            u'paglia': u'팔리아',
            u'egli': u'엘리',
            u'gloria': u'글로리아',
            u'glossa': u'글로사',
        })

    def test_2nd(self):
        """제2항: gn
        뒤따르는 모음과 합쳐 '냐', '녜', '뇨', '뉴', '니'로 적는다.
        """
        self.assert_examples({
            u'montagna': u'몬타냐',
            u'gneiss': u'녜이스',
            u'gnocco': u'뇨코',
            u'gnu': u'뉴',
            u'ogni': u'오니',
        })

    def test_3rd(self):
        """제3항: sc
        sce는 '셰'로, sci는 '시'로 적고, 그 밖의 경우에는 '스ㅋ'으로 적는다.
        """
        self.assert_examples({
            u'crescendo': u'크레셴도',
            u'scivolo': u'시볼로',
            u'Tosca': u'토스카',
            u'scudo': u'스쿠도',
        })

    def test_4th(self):
        """제4항
        같은 자음이 겹쳤을 때에는 겹치지 않은 경우와 같이 적는다. 다만, -mm-,
        -nn-의 경우는 'ㅁㅁ', 'ㄴㄴ'으로 적는다.
        """
        self.assert_examples({
            u'Puccini': u'푸치니',
            u'buffa': u'부파',
            u'allegretto': u'알레그레토',
            u'carro': u'카로',
            u'rosso': u'로소',
            u'mezzo': u'메초',
            u'gomma': u'곰마',
            u'bisnonno': u'비스논노',
        })

    def test_5th(self):
        """제5항: c, g
        1. c와 g는 e, i 앞에서 각각 'ㅊ', 'ㅈ'으로 적는다.
        2. c와 g 다음에 ia, io, iu가 올 때에는 각각 '차, 초, 추',
           '자, 조, 주'로 적는다.
        """
        self.assert_examples({
            u'cenere': u'체네레',
            u'genere': u'제네레',
            u'cima': u'치마',
            u'gita': u'지타',
            u'caccia': u'카차',
            u'micio': u'미초',
        })

    def test_6th(self):
        """제6항: qu
        qu는 뒤따르는 모음과 합쳐 '콰, 퀘, 퀴' 등으로 적는다. 다만, o 앞에서는
        '쿠'로 적는다.
        """
        self.assert_examples({
            u'soqquadro': u'소콰드로',
            u'quello': u'퀠로',
            u'quieto': u'퀴에토',
            u'quota': u'쿠오타',
        })

    def test_7th(self):
        """제7항: l, ll
        어말 또는 자음 앞의 l, ll은 받침으로 적고, 어중의 l, ll이 모음 앞에
        올 때에는 'ㄹㄹ'로 적는다.
        """
        self.assert_examples({
            u'sol': u'솔',
            u'polca': u'폴카',
            u'Carlo': u'카를로',
            u'quello': u'퀠로',
        })

    def test_hangulize(self):
        self.assert_examples({
            u'italia': u'이탈리아',
            u'Innocenti': u'인노첸티',
            u'Cerigotto': u'체리고토',
            u'Juventus': u'유벤투스',
            u'Schiavonia': u'스키아보니아',
            u'Fogli': u'폴리',
            u'Caravaggio': u'카라바조',
            u'nephos': u'네포스',
            u'sbozzacchisce': u'스보차키셰',
            u'Scalenghe': u'스칼렌게',
            u'Fabrizio': u'파브리치오',
            u'Anghiari': u'안기아리',
            u'soqquadro': u'소콰드로',
            u'Bologna': u'볼로냐',
            u'Fognini': u'포니니',
            u'Ignazio': u'이냐치오',
            u"Giro d'Italia": u'지로 디탈리아',
            u"per l'avvenire d'Italia": u'페르 라베니레 디탈리아',
            u'Rex': u'렉스',
        })
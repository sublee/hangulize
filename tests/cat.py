# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.cat import Catalan


class CatalanTestCase(HangulizeTestCase):

    lang = Catalan()

    def test_people(self):
        self.assert_examples({
            u'Arantxa': u'아란차',
            u'Valentí Almirall': u'발렌티 알미랄',
            u'Jaume Bartumeu': u'자우메 바르투메우',
            u'Sergi Bruguera': u'세르지 브루게라',
            u'Montserrat Caballé': u'몬세라트 카발례',
            u'Santiago Calatrava': u'산티아고 칼라트라바',
            u'Joan Capdevila': u'조안 캅데빌라',
            u'Josep Carner': u'조제프 카르네르',
            u'Pau Casals': u'파우 카잘스',
            u'Lluís Companys': u'류이스 콤파니스',
            u'Àlex Corretja': u'알렉스 코레자',
            u'Albert Costa': u'알베르트 코스타',
            u'Salvador Dalí': u'살바도르 달리',
            u'Salvador Espriu': u'살바도르 에스프리우',
            u'Cesc Fàbregas': u'세스크 파브레가스',
            u'Pau Gasol': u'파우 가졸',
            u'Antoni Gaudí': u'안토니 가우디',
            u'Josep Guardiola': u'조제프 과르디올라',
            u'Xavi Hernández': u'샤비 에르난데스',
            u'Ramon Llull': u'라몬 률',
            u'Francesc Macià i Llussà': u'프란세스크 마시아 이 류사',
            u'Joan Maragall': u'조안 마라갈',
            u'Ausiàs March': u'아우지아스 마르크',
            u'Joanot Martorell': u'조아노트 마르토렐',
            u'Joan Miró': u'조안 미로',
            u'Gerard Piqué': u'제라르트 피케',
            u'Josep Pla': u'조제프 플라',
            u'Eudald Pradell': u'에우달 프라델',
            u'Carles Puyol': u'카를레스 푸욜',
            u'Mercè Rodoreda': u'메르세 로도레다',
            u'Jordi Savall': u'조르디 사발',
            u'Joan Manuel Serrat': u'조안 마누엘 세라트',
            u'Joaquim Sorolla': u'조아킴 소롤랴',
            u'Antoni Tàpies': u'안토니 타피에스',
            u'Josep Tarradellas': u'조제프 타라델랴스',
            u'Jordi Tarrés': u'조르디 타레스',
            u'Jacint Verdaguer': u'자신 베르다게르',
        })

    def test_places(self):
        self.assert_examples({
            u'Alacant': u'알라칸',
            u'Andorra': u'안도라',
            u'Andorra la Vella': u'안도라 라 벨랴',
            u'Barcelona': u'바르셀로나',
            u'Berga': u'베르가',
            u'Besalú': u'베잘루',
            u'Catalunya': u'카탈루냐',
            u'Cerdanya': u'세르다냐',
            u'Conflent': u'콘플렌',
            u'Eivissa': u'에이비사',
            u'Elx': u'엘시',
            u'Empúries': u'엠푸리에스',
            u'Figueres': u'피게레스',
            u'Girona': u'지로나',
            u'Lleida': u'례이다',
            u'Manresa': u'만레자',
            u'Montjuïc': u'몬주이크',
            u'Montserrat': u'몬세라트',
            u'Osona': u'오조나',
            u'Pallars': u'팔랴르스',
            u'Pallars Jussà': u'팔랴르스 주사',
            u'Pallars Sobirà': u'팔랴르스 소비라',
            u'Palma': u'팔마',
            u'Ribagorça': u'리바고르사',
            u'Rosselló': u'로셀료',
            u'Tarragona': u'타라고나',
            u'Urgell': u'우르젤',
            u'València': u'발렌시아',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            u'Barça': u'바르사',
            u'Camp Nou': u'캄 노우',
            u'Canigó': u'카니고',
            u'Espanyol': u'에스파뇰',
            u'estel·lar': u'에스텔라르',
            u'llengua': u'롕과',
            u'modernisme': u'모데르니즈메',
            u'Renaixença': u'레나셴사',
            u'Sagrada Família': u'사그라다 파밀리아',
        })
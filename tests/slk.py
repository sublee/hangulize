# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.slk import Slovak


class SlovakTestCase(HangulizeTestCase):

    lang = Slovak()

    def test_people(self):
        self.assert_examples({
            u'Ján Bahýľ': u'얀 바힐',
            u'Štefan Banič': u'슈테판 바니치',
            u'Anton Bernolák': u'안톤 베르놀라크',
            u'Peter Bondra': u'페테르 본드라',
            u'Zdeno Chára': u'즈데노 하라',
            u'Dominika Cibulková': u'도미니카 치불코바',
            u'Ján Čarnogurský': u'얀 차르노구르스키',
            u'Štefan Marko Daxner': u'슈테판 마르코 닥스네르',
            u'Pavol Demitra': u'파볼 데미트라',
            u'Alexander Dubček': u'알렉산데르 둡체크',
            u'Mikuláš Dzurinda': u'미쿨라시 주린다',
            u'Marián Gáborík': u'마리안 가보리크',
            u'Marek Hamšík': u'마레크 함시크',
            u'Daniela Hantuchová': u'다니엘라 한투호바',
            u'Andrej Hlinka': u'안드레이 흘린카',
            u'Milan Hodža': u'밀란 호자',
            u'Marian Hossa': u'마리안 호사',
            u'Dominik Hrbatý': u'도미니크 흐르바티',
            u'Pavol Hurajt': u'파볼 후라이트',
            u'Jozef Miloslav Hurban': u'요제프 밀로슬라우 후르반',
            u'Gustáv Husák': u'구스타우 후사크',
            u'Hviezdoslav': u'흐비에즈도슬라우',
            u'Dionýz Ilkovič': u'디오니스 일코비치',
            u'Elena Kaliská': u'엘레나 칼리스카',
            u'Michaela Kocianová': u'미하엘라 코치아노바',
            u'Karol Kučera': u'카롤 쿠체라',
            u'Anastasiya Kuzmina': u'아나스타시야 쿠즈미나',
            u'Michal Martikán': u'미할 마르티칸',
            u'Janko Matúška': u'얀코 마투슈카',
            u'Vladimír Mečiar': u'블라디미르 메치아르',
            u'Martina Moravcová': u'마르티나 모라우초바',
            u'Jozef Murgaš': u'요제프 무르가시',
            u'Natália Prekopová': u'나탈리아 프레코포바',
            u'Jozef Roháček': u'요제프 로하체크',
            u'Magdaléna Rybáriková': u'마그달레나 리바리코바',
            u'Zuzana Sekerová': u'주자나 세케로바',
            u'Aurel Stodola': u'아우렐 스토돌라',
            u'Eugen Suchoň': u'에우겐 수혼',
            u'Martin Škrtel': u'마르틴 슈크르텔',
            u'Milan Rastislav Štefánik': u'밀란 라스티슬라우 슈테파니크',
            u'Zuzana Štefečeková': u'주자나 슈테페체코바',
            u'Peter Šťastný': u'페테르 슈탸스트니',
            u'Ľudovít Štúr': u'류도비트 슈투르',
            u'Jozef Tiso': u'요제프 티소',
            u'Vavrinec': u'바우리네츠',
            u'Rudolf Vrba': u'루돌프 브르바',
            u'Vladimír Weiss': u'블라디미르 베이스',
        })

    def test_places(self):
        self.assert_examples({
            u'Banská Bystrica': u'반스카 비스트리차',
            u'Bardejov': u'바르데요우',
            u'Bratislava': u'브라티슬라바',
            u'Komárno': u'코마르노',
            u'Košice': u'코시체',
            u'Manínska tiesňava': u'마닌스카 티에스냐바',
            u'Martin': u'마르틴',
            u'Michalovce': u'미할로우체',
            u'Nitra': u'니트라',
            u'Poprad': u'포프라트',
            u'Považská': u'포바슈스카',
            u'Prešov': u'프레쇼우',
            u'Rožňava': u'로주냐바',
            u'Slavín': u'슬라빈',
            u'Spiš': u'스피시',
            u'Trenčín': u'트렌친',
            u'Trnava': u'트르나바',
            u'Váh': u'바흐',
            u'Vlkolínec': u'블콜리네츠',
            u'Vydrica': u'비드리차',
            u'Zvolen': u'즈볼렌',
            u'Žilina': u'질리나',
            u'Žehra': u'제흐라',
        })

    def test_miscellaneous(self):
        self.assert_examples({
            u'deväť': u'데베티',
            u'jahôd': u'야후오트',
            u'mäkčeň': u'멕첸',
            u'pätnásť': u'페트나스티',
        })
# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.bel import Belarusian


class BelarusianTestCase(HangulizeTestCase):

    lang = Belarusian()

    def test_people(self):
        assert u'알략세이 아발마사우' == self.hangulize(u'Аляксей Абалмасаў')
        assert u'빅토리야 아자렌카' == self.hangulize(u'Вікторыя Азарэнка')
        assert u'스뱌틀라나 알렉시예비치' == \
               self.hangulize(u'Святлана Алексіевіч')
        assert u'프란치샤크 알랴흐노비치' == \
               self.hangulize(u'Францішак Аляхновіч')
        assert u'안드레이 아람나우' == self.hangulize(u'Андрэй Арамнаў')
        assert u'알레크 아흐렘' == self.hangulize(u'Алег Ахрэм')
        assert u'막심 바흐다노비치' == self.hangulize(u'Максім Багдановіч')
        assert u'스뱌틀라나 바힌스카야' == self.hangulize(u'Святлана Багінская')
        assert u'프란치샤크 바후셰비치' == \
               self.hangulize(u'Францішак Багушэвіч')
        assert u'시몬 부드니' == self.hangulize(u'Сымон Будны')
        assert u'알략산드르 흘레프' == self.hangulize(u'Аляксандр Глеб')
        assert u'야우헨 흘레바우' == self.hangulize(u'Яўген Глебаў')
        assert u'알략세이 흐리신' == self.hangulize(u'Аляксей Грышын')
        assert u'빈첸트 두닌마르친케비치' == \
               self.hangulize(u'Вінцэнт Дунін-Марцінкевіч')
        assert u'예프라신냐 폴라츠카야' == self.hangulize(u'Ефрасіння Полацкая')
        assert u'카스투스 칼리노우스키' == self.hangulize(u'Кастусь Каліноўскі')
        assert u'카차리나 카르스텐' == self.hangulize(u'Кацярына Карстэн')
        assert u'야쿠프 콜라스' == self.hangulize(u'Якуб Колас')
        assert u'얀카 쿠팔라' == self.hangulize(u'Янка Купала')
        assert u'바츨라우 라스토우스키' == self.hangulize(u'Вацлаў Ластоўскі')
        assert u'알략산드르 루카셴카' == self.hangulize(u'Аляксандр Лукашэнка')
        assert u'이하르 루차노크' == self.hangulize(u'Ігар Лучанок')
        assert u'바짐 마흐네우' == self.hangulize(u'Вадзім Махнеў')
        assert u'율리야 네스차렌카' == self.hangulize(u'Юлія Несцярэнка')
        assert u'알략산드르 파투파' == self.hangulize(u'Аляксандр Патупа')
        assert u'이파치 파체이' == self.hangulize(u'Іпаці Пацей')
        assert u'알라이자 파슈케비치' == self.hangulize(u'Алаіза Пашкевіч')
        assert u'나탈랴 퍄트케비치' == self.hangulize(u'Наталля Пяткевіч')
        assert u'라지빌' == self.hangulize(u'Радзівіл')
        assert u'막심 라마샨카' == self.hangulize(u'Максім Рамашчанка')
        assert u'미하일 사비츠키' == self.hangulize(u'Міхаіл Савіцкі')
        assert u'레우 사페하' == self.hangulize(u'Леў Сапега')
        assert u'얀 세라다' == self.hangulize(u'Ян Серада')
        assert u'프란치스크 스카리나' == self.hangulize(u'Францыск Скарына')
        assert u'라만 스키르문트' == self.hangulize(u'Раман Скірмунт')
        assert u'먈레치 스마트리츠키' == self.hangulize(u'Мялецій Сматрыцкі')
        assert u'얀 스탄케비치' == self.hangulize(u'Ян Станкевіч')
        assert u'표다르 숨킨' == self.hangulize(u'Фёдар Сумкін')
        assert u'브라니슬라우 타라슈케비치' == \
               self.hangulize(u'Браніслаў Тарашкевіч')
        assert u'빅타르 투라우' == self.hangulize(u'Віктар Тураў')
        assert u'미칼라이 울라시크' == self.hangulize(u'Мікалай Улашчык')
        assert u'표다르 표다라우' == self.hangulize(u'Фёдар Фёдараў')
        assert u'얀 차초트' == self.hangulize(u'Ян Чачот')

    def test_places(self):
        assert u'바브루이스크' == self.hangulize(u'Бабруйск')
        assert u'바라나비치' == self.hangulize(u'Баранавічы')
        assert u'벨라베슈스카야 푸샤' == self.hangulize(u'Белавежская пушча')
        assert u'벨라루스' == self.hangulize(u'Беларусь')
        assert u'브레스트' == self.hangulize(u'Брэст')
        assert u'비쳅스크' == self.hangulize(u'Віцебск')
        assert u'호멜' == self.hangulize(u'Гомель')
        assert u'흐로드나' == self.hangulize(u'Гродна')
        assert u'카먀네츠' == self.hangulize(u'Камянец')
        assert u'마힐료우' == self.hangulize(u'Магілёў')
        assert u'민스크' == self.hangulize(u'Мінск')
        assert u'미르' == self.hangulize(u'Мір')
        assert u'무라반카' == self.hangulize(u'Мураванка')
        assert u'냐스비시' == self.hangulize(u'Нясвіж')
        assert u'폴라츠크' == self.hangulize(u'Полацк')
        assert u'신카비치' == self.hangulize(u'Сынкавічы')
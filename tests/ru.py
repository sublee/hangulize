# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.ru import Russian


class RussianTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0221.jsp """

    lang = Russian()

    def test_etc(self):
        assert u'프레미예르' == self.hangulize(u'Премьер')

    def test_basic(self):
        """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0119.jsp """
        assert u'볼로토프' == self.hangulize(u'Болотов')
        assert u'보브로프' == self.hangulize(u'Бобров')
        assert u'쿠릅스키' == self.hangulize(u'Курбский')
        assert u'글레프' == self.hangulize(u'Глеб')
        assert u'곤차로프' == self.hangulize(u'Гончаров')
        assert u'마네치카' == self.hangulize(u'Манечка')
        assert u'야쿠보비치' == self.hangulize(u'Якубович')
        assert u'드미트리' == self.hangulize(u'Дмитрий')
        assert u'베네딕토프' == self.hangulize(u'Бенедиктов')
        assert u'나홋카' == self.hangulize(u'Находка')
        assert u'보스호트' == self.hangulize(u'Восход')
        assert u'표도르' == self.hangulize(u'Фёдор')
        assert u'예프레모프' == self.hangulize(u'Ефремов')
        assert u'이오시프' == self.hangulize(u'Иосиф')
        assert u'고골' == self.hangulize(u'Гоголь')
        assert u'무소륵스키' == self.hangulize(u'Мусоргский')
        assert u'보그단' == self.hangulize(u'Богдан')
        assert u'안다르바크' == self.hangulize(u'Андарбаг')
        assert u'하바롭스크' == self.hangulize(u'Хабаровск')
        assert u'아흐마토바' == self.hangulize(u'Ахматова')
        assert u'오이스트라흐' == self.hangulize(u'Ойстрах')
        assert u'칼미크' == self.hangulize(u'Калмык')
        assert u'악사코프' == self.hangulize(u'Аксаков')
        assert u'크바스' == self.hangulize(u'Квас')
        assert u'블라디보스토크' == self.hangulize(u'Владивосток')
        assert u'레닌' == self.hangulize(u'Ленин')
        assert u'니콜라이' == self.hangulize(u'Николай')
        assert u'크릴로프' == self.hangulize(u'Крылов')
        assert u'파벨' == self.hangulize(u'Павел')
        assert u'미하일' == self.hangulize(u'Михаийл')
        assert u'막심' == self.hangulize(u'Максим')
        assert u'므첸스크' == self.hangulize(u'Мценск')
        assert u'나댜' == self.hangulize(u'Надя')
        assert u'스테판' == self.hangulize(u'Стефан')
        assert u'표트르' == self.hangulize(u'Пётр')
        assert u'로스톱치냐' == self.hangulize(u'Ростопчиня')
        assert u'프스코프' == self.hangulize(u'Псков')
        assert u'마이코프' == self.hangulize(u'Майкоп')
        assert u'리빈스크' == self.hangulize(u'Рыбинск')
        assert u'레르몬토프' == self.hangulize(u'Лермонтов')
        assert u'아르툠' == self.hangulize(u'Артём')
        assert u'바실리' == self.hangulize(u'Василий')
        assert u'스테판' == self.hangulize(u'Стефан')
        assert u'보리스' == self.hangulize(u'Борис')
        assert u'셸구노프' == self.hangulize(u'Шелгунов')
        assert u'시시코프' == self.hangulize(u'Шишков')
        assert u'셰르바코프' == self.hangulize(u'Щербаков')
        assert u'시레츠' == self.hangulize(u'Щирец')
        assert u'보르시' == self.hangulize(u'борщ')
        assert u'타티야나' == self.hangulize(u'Татьяна')
        assert u'흐밧코프' == self.hangulize(u'Хватков')
        assert u'트베리' == self.hangulize(u'Тверь')
        assert u'부랴트' == self.hangulize(u'Бурят')
        assert u'가치나' == self.hangulize(u'Гатчина')
        assert u'튜체프' == self.hangulize(u'Тютчев')
        assert u'카피차' == self.hangulize(u'Капица')
        assert u'츠베타예바' == self.hangulize(u'Цветаева')
        assert u'브랴츠크' == self.hangulize(u'Брятск')
        assert u'야쿠츠크' == self.hangulize(u'Якутск')
        assert u'베렙킨' == self.hangulize(u'Веревкин')
        assert u'도스토옙스키' == self.hangulize(u'Достоевский')
        assert u'블라디보스토크' == self.hangulize(u'Владивосток')
        assert u'마르코프' == self.hangulize(u'Марков')
        assert u'자이체프' == self.hangulize(u'Зайчев')
        assert u'쿠즈네초프' == self.hangulize(u'Кузнецов')
        assert u'아그리스' == self.hangulize(u'Агрыз')
        assert u'자돕스카야' == self.hangulize(u'Жадовская')
        assert u'즈다노프' == self.hangulize(u'Жданов')
        assert u'루시코프' == self.hangulize(u'Лужков')
        #assert u'케베시' == self.hangulize(u'Кебеж')
        assert u'유리' == self.hangulize(u'Юрий')
        assert u'안드레이' == self.hangulize(u'Андрей')
        assert u'벨리' == self.hangulize(u'Белый')
        assert u'악사코프' == self.hangulize(u'Аксаков')
        assert u'아바칸' == self.hangulize(u'Абакан')
        #assert u'페트로프' == self.hangulize(u'Петров')
        assert u'예브게니' == self.hangulize(u'Евгений')
        assert u'알렉세예프' == self.hangulize(u'Алексеев')
        assert u'예르텔' == self.hangulize(u'Эртель')
        assert u'이바노프' == self.hangulize(u'Иванов')
        #assert u'이오시프' == self.hangulize(u'Иосиф')
        assert u'호먀코프' == self.hangulize(u'Хомяков')
        assert u'오카' == self.hangulize(u'Ока')
        assert u'우샤코프' == self.hangulize(u'Ушаков')
        assert u'사라풀' == self.hangulize(u'Сарапул')
        assert u'살티코프' == self.hangulize(u'Салтыков')
        assert u'키라' == self.hangulize(u'Кыра')
        assert u'벨리' == self.hangulize(u'Белый')
        assert u'야신스키' == self.hangulize(u'Ясинский')
        assert u'아디게야' == self.hangulize(u'Адыгея')
        assert u'솔로비요프' == self.hangulize(u'Соловьёв')
        assert u'아르툠' == self.hangulize(u'Артём')
        assert u'유리' == self.hangulize(u'Юрий')
        assert u'유르가' == self.hangulize(u'Юрга')

    def test_1st(self):
        """제1항: p(п), t(т), k(к), b(б), d(д), g(г), f(ф), v(в)
        파열음과 마찰음 f(ф)·v(в)는 무성 자음 앞에서는 앞 음절의 받침으로
        적고, 유성 자음 앞에서는 ‘으'를 붙여 적는다.
        """
        assert u'삿코' == self.hangulize(u'Садко')
        assert u'아그리스' == self.hangulize(u'Агрыз')
        assert u'아크바우르' == self.hangulize(u'Акбаур')
        assert u'로스톱치냐' == self.hangulize(u'Ростопчиня')
        assert u'아크메이즘' == self.hangulize(u'Акмеизм')
        assert u'룹촙스크' == self.hangulize(u'Рубцовск')
        assert u'브랴츠크' == self.hangulize(u'Брятск')
        assert u'로팟카' == self.hangulize(u'Лопатка')
        assert u'예프레모프' == self.hangulize(u'Ефремов')
        assert u'도스토옙스키' == self.hangulize(u'Достоевский')

    def test_2nd(self):
        """제2항: z(з), zh(ж)
        z(з)와 zh(ж)는 유성 자음 앞에서는 ‘즈'로 적고 무성 자음 앞에서는
        각각 ‘스, 시'로 적는다.
        """
        assert u'나즈란' == self.hangulize(u'Назрань')
        #assert u'니즈니타길' == self.hangulize(u'Нижний Тагил')
        assert u'니즈니 타길' == self.hangulize(u'Нижний Тагил')
        assert u'오스트로고시스크' == self.hangulize(u'Острогожск')
        assert u'루시코프' == self.hangulize(u'Лужков')

    def test_3rd(self):
        """제3항
        지명의 -grad(град)와 -gorod(город)는 관용을 살려 각각 ‘-그라드',
        ‘-고로드'로 표기한다.
        """
        assert u'볼고그라드' == self.hangulize(u'Волгоград')
        assert u'칼리닌그라드' == self.hangulize(u'Калининград')
        assert u'슬라브고로드' == self.hangulize(u'Славгород')

    def test_4th(self):
        """제4항
        자음 앞의 -ds(дс)-는 ‘츠'로 적는다.
        """
        #assert u'페트로자보츠크' == self.hangulize(u'Петрозаводск')
        assert u'베르나츠키' == self.hangulize(u'Вернадский')

    def test_5th(self):
        """제5항
        어말 또는 자음 앞의 l(л)은 받침 ‘ㄹ'로 적고, 어중의 l이 모음 앞에
        올 때에는 ‘ㄹㄹ'로 적는다.
        """
        assert u'파벨' == self.hangulize(u'Павел')
        assert u'니콜라예비치' == self.hangulize(u'Николаевич')
        assert u'제믈랴' == self.hangulize(u'Земля')
        assert u'치믈랸스크' == self.hangulize(u'Цимлянск')

    def test_6th(self):
        """제6항
        l'(ль), m(м)이 어두 자음 앞에 오는 경우에는 각각 ‘리', ‘므'로 적는다.
        """
        assert u'리보브나' == self.hangulize(u'Льбовна')
        assert u'므첸스크' == self.hangulize(u'Мценск')

    def test_7th(self):
        """제7항
        같은 자음이 겹치는 경우에는 겹치지 않은 경우와 같이 적는다. 다만,
        mm(мм), nn(нн)은 모음 앞에서 ‘ㅁㅁ', ‘ㄴㄴ'으로 적는다.
        """
        assert u'기피우스' == self.hangulize(u'Гиппиус')
        assert u'아바쿰' == self.hangulize(u'Аввакум')
        assert u'오데사' == self.hangulize(u'Одесса')
        assert u'아콜' == self.hangulize(u'Акколь')
        assert u'솔로구프' == self.hangulize(u'Соллогуб')
        assert u'안나' == self.hangulize(u'Анна')
        assert u'감마' == self.hangulize(u'Гамма')

    def test_8th(self):
        """제8항
        e(е, э)는 자음 뒤에서는 ‘에'로 적고, 그 외의 경우에는 ‘예'로 적는다.
        """
        assert u'알렉세이' == self.hangulize(u'Алексей')
        assert u'예그베키노트' == self.hangulize(u'Егвекинот')

    def test_9th(self):
        """제9항: 연음 부호 '(ь)
        연음 부호 '(ь)은 ‘이'로 적는다. 다만 l', m', n'(ль, мь, нь)이 자음
        앞이나 어말에 오는 경우에는 적지 않는다.
        """
        assert u'리보브나' == self.hangulize(u'Льбовна')
        assert u'이고리' == self.hangulize(u'Игорь')
        assert u'일리야' == self.hangulize(u'Илья')
        assert u'디야코보' == self.hangulize(u'Дьяково')
        assert u'올가' == self.hangulize(u'Ольга')
        #assert u'페름' == self.hangulize(u'Пермь')
        assert u'랴잔' == self.hangulize(u'Рязань')
        assert u'고골' == self.hangulize(u'Гоголь')

    def test_10th(self):
        """제10항
        dz(дз), dzh(дж)는 각각 z, zh와 같이 적는다.
        """
        assert u'제르진스키' == self.hangulize(u'Дзержинский')
        assert u'타지키스탄' == self.hangulize(u'Таджикистан')

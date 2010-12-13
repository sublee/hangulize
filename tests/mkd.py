# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.mkd import Macedonian


class MacedonianTestCase(HangulizeTestCase):

    lang = Macedonian()

    def test_people(self):
        # assert u'메토디야 안도노프첸토' == \
        #        self.hangulize(u'Методија Андонов-Ченто')
        # => 메토디야 안도노브첸토
        assert u'디미트리예 부자로프스키' == \
               self.hangulize(u'Димитрије Бужаровски')
        assert u'블라도 부치코프스키' == self.hangulize(u'Владо Бучковски')
        assert u'키로 글리고로프' == self.hangulize(u'Киро Глигоров')
        assert u'카롤리나 고체바' == self.hangulize(u'Каролина Гочева')
        assert u'니콜라 그루에프스키' == self.hangulize(u'Никола Груевски')
        assert u'디미타르 디미트로프' == self.hangulize(u'Димитар Димитров')
        assert u'파르테니야 조그라프스키' == \
               self.hangulize(u'Партенија Зографски')
        assert u'교르게 이바노프' == self.hangulize(u'Ѓорге Иванов')
        assert u'밀란 이바노비치' == self.hangulize(u'Милан Ивановиќ')
        assert u'카타리나 이바노프스카' == self.hangulize(u'Катарина Ивановска')
        assert u'바제 일리요스키' == self.hangulize(u'Баже Илијоски')
        assert u'슬라프코 야네프스키' == self.hangulize(u'Славко Јаневски')
        assert u'보리안 요바노프스키' == self.hangulize(u'Борјан Јовановски')
        assert u'클리멘트 오흐리츠키' == self.hangulize(u'Климент Охридски')
        assert u'니콜라 클류세프' == self.hangulize(u'Никола Кљусев')
        assert u'라자르 콜리셰프스키' == self.hangulize(u'Лазар Колишевски')
        assert u'블라제 코네스키' == self.hangulize(u'Блаже Конески')
        assert u'하리 코스토프' == self.hangulize(u'Хари Костов')
        assert u'자르코 쿠윤지스키' == self.hangulize(u'Жарко Кујунџиски')
        assert u'키릴 라자로프' == self.hangulize(u'Кирил Лазаров')
        assert u'벤코 마르코프스키' == self.hangulize(u'Венко Марковски')
        assert u'디미타르 밀라디노프' == self.hangulize(u'Димитар Миладинов')
        assert u'콘스탄틴 밀라디노프' == self.hangulize(u'Константин Миладинов')
        assert u'크르스테 미시르코프' == self.hangulize(u'Крсте Мисирков')
        assert u'페타르 나우모스키' == self.hangulize(u'Петар Наумоски')
        assert u'콜레 네델코프스키' == self.hangulize(u'Коле Неделковски')
        assert u'사샤 오그네노프스키' == self.hangulize(u'Саша Огненовски')
        assert u'고란 판데프' == self.hangulize(u'Горан Пандев')
        assert u'지프코 포포프스키츠베틴' == \
               self.hangulize(u'Живко Поповски-Цветин')
        assert u'율리야 포르티안코' == self.hangulize(u'Јулија Портјанко')
        assert u'토셰 프로에스키' == self.hangulize(u'Тоше Проески')
        assert u'교르기 풀레프스키' == self.hangulize(u'Ѓорѓи Пулевски')
        assert u'코초 라친' == self.hangulize(u'Кочо Рацин')
        assert u'에스마 레제포바' == self.hangulize(u'Есма Реџепова')
        assert u'스테비차 리스티치' == self.hangulize(u'Стевица Ристиќ')
        assert u'두샨 사비치' == self.hangulize(u'Душан Савиќ')
        assert u'토도르 스칼로프스키' == self.hangulize(u'Тодор Скаловски')
        assert u'브르비차 스테파노프' == self.hangulize(u'Врбица Стефанов')
        assert u'고란 스테파노프스키' == self.hangulize(u'Горан Стефановски')
        assert u'보리스 트라이코프스키' == self.hangulize(u'Борис Трајковски')
        assert u'교르기 흐리스토프' == self.hangulize(u'Ѓорѓи Христов')
        assert u'브란코 츠르벤코프스키' == self.hangulize(u'Бранко Црвенковски')
        assert u'류보미르 추출로프스키' == self.hangulize(u'Љубомир Цуцуловски')
        assert u'콜레 차슐레' == self.hangulize(u'Коле Чашуле')
        assert u'지프코 친고' == self.hangulize(u'Живко Чинго')
        assert u'알렉산다르 잠바조프' == self.hangulize(u'Александар Џамбазов')

    def test_places(self):
        assert u'비톨라' == self.hangulize(u'Битола')
        assert u'벨레스' == self.hangulize(u'Велес')
        assert u'게브겔리야' == self.hangulize(u'Гевгелија')
        assert u'고스티바르' == self.hangulize(u'Гостивар')
        assert u'카바다르치' == self.hangulize(u'Кавадарци')
        assert u'키체보' == self.hangulize(u'Кичево')
        assert u'코키노' == self.hangulize(u'Кокино')
        assert u'코라프' == self.hangulize(u'Кораб')
        assert u'코차니' == self.hangulize(u'Кочани')
        assert u'크라토보' == self.hangulize(u'Кратово')
        assert u'쿠클리차' == self.hangulize(u'Куклица')
        assert u'쿠마노보' == self.hangulize(u'Куманово')
        assert u'마케도니야' == self.hangulize(u'Македонија')
        assert u'마르코비 쿨리' == self.hangulize(u'Маркови Кули')
        assert u'노프 도이란' == self.hangulize(u'Нов Дојран')
        assert u'오흐리트' == self.hangulize(u'Охрид')
        assert u'프릴레프' == self.hangulize(u'Прилеп')
        assert u'라도비시' == self.hangulize(u'Радовиш')
        assert u'스코피에' == self.hangulize(u'Скопје')
        assert u'슬라티노' == self.hangulize(u'Слатино')
        assert u'스트루가' == self.hangulize(u'Струга')
        assert u'스트루미차' == self.hangulize(u'Струмица')
        assert u'테토보' == self.hangulize(u'Тетово')
        assert u'샤르' == self.hangulize(u'Шар')
        assert u'슈티프' == self.hangulize(u'Штип')

    def test_miscellaneous(self):
        assert u'메탈루르크' == self.hangulize(u'Металург')

# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.aze import Azerbaijani


class AzerbaijaniTestCase(HangulizeTestCase):

    lang = Azerbaijani()

    def test_people(self):
        self.assert_examples({
            u'Namiq Abdullayev': u'나미크 아브둘라예프',
            u'Qəmər Almaszadə': u'게메르 알마스자데',
            u'Heydər Əliyev': u'헤이데르 엘리예프',
            u'İlham Əliyev': u'일함 엘리예프',
            u'Hüseyn Ərəblinski': u'휘세인 에레블린스키',
            u'Rəşid Behbudov': u'레시트 베흐부도프',
            u'Bülbül': u'뷜뷜',
            u'Cəfər Cabbarlı': u'제페르 자발르',
            u'Vaqif Cavadov': u'바기프 자바도프',
            u'Hüseyn Cavid': u'휘세인 자비트',
            u'Füzuli': u'퓌줄리',
            u'Üzeyir Hacıbəyov': u'위제이르 하즈베요프',
            u'Mehdi Hüseynzadə': u'메흐디 휘세인자데',
            u'Kərim Kərimov': u'케림 케리모프',
            u'Fərid Mansurov': u'페리트 만수로프',
            u'Elnur Məmmədli': u'엘누르 멤메들리',
            u'Məhəmməd Mövlazadə': u'메헴메트 뫼블라자데',
            u'Əzizə Mustafazadə': u'에지제 무스타파자데',
            u'Vaqif Mustafazadə': u'바기프 무스타파자데',
            u'Mikayıl Müşfiq': u'미카이을 뮈슈피크',
            u'Xurşidbanu Natəvan': u'후르시드바누 나테반',
            u'Hüseyn xan Naxçıvanski': u'휘세인 한 나흐츠반스키',
            u'Nəriman Nərimanov': u'네리만 네리마노프',
            u'İmadəddin Nəsimi': u'이마데딘 네시미',
            u'Mir-Möhsün Nəvvab': u'미르뫼흐쉰 네바프',
            u'Ramil Quliyev': u'라밀 굴리예프',
            u'Nigar Rəfibəyli': u'니가르 레피베일리',
            u'Artur Rəsizadə': u'아르투르 레시자데',
            u'Məhəmməd Əmin Rəsulzadə': u'메헴메트 에민 레술자데',
            u'Süleyman Rüstəm': u'쉴레이만 뤼스템',
            u'Rəsul Rza': u'레술 르자',
            u'Rəşad Sadıqov': u'레샤트 사드고프',
            u'Məmməd ağa Şahtaxtinski': u'멤메트 아가 샤흐타흐틴스키',
            u'Məhəmmədhüseyn Şəhriyar': u'메헴메트휘세인 셰흐리야르',
            u'Nigar Şıxlinskaya': u'니가르 시으흘린스카야',
            u'Zeynalabdin Tağıyev': u'제이날라브딘 타그예프',
            u'Aysel Teymurzadə': u'아이셀 테이무르자데',
            u'Səməd Vurğun': u'세메트 부르군',
            u'Fətəli xan Xoyski': u'페텔리 한 호이스키',
        })

    def test_places(self):
        self.assert_examples({
            u'Abşeron': u'압셰론',
            u'Ağdam': u'아그담',
            u'Azərbaycan': u'아제르바이잔',
            u'Bakı': u'바크',
            u'Gəncə': u'겐제',
            u'İçəri Şəhər': u'이체리 셰헤르',
            u'Lənkəran': u'렌케란',
            u'Mingəçevir': u'민게체비르',
            u'Naftalan': u'나프탈란',
            u'Naxçıvan': u'나흐츠반',
            u'Qəbələ': u'게벨레',
            u'Qobustan': u'고부스탄',
            u'Salyan': u'살리안',
            u'Sumqayıt': u'숨가이으트',
            u'Şəki': u'셰키',
            u'Şəmkir': u'솀키르',
            u'Şirvan': u'시르반',
            u'Talış': u'탈르슈',
            u'Tovuz': u'토부스',
            u'Xaçmaz': u'하치마스',
            u'Xınalıq': u'흐날르크',
            u'Xırdalan': u'흐르달란',
            u'Yevlax': u'예블라흐',
            u'Zaqatala': u'자가탈라',
        })

    def test_others(self):
        self.assert_examples({
            u'jurnal': u'주르날',
        })

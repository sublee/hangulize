# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.aze import Azerbaijani


class AzerbaijaniTestCase(HangulizeTestCase):

    lang = Azerbaijani()

    def test_people(self):
        assert u'나미크 아브둘라예프' == self.hangulize(u'Namiq Abdullayev')
        assert u'게메르 알마스자데' == self.hangulize(u'Qəmər Almaszadə')
        assert u'헤이데르 엘리예프' == self.hangulize(u'Heydər Əliyev')
        assert u'일함 엘리예프' == self.hangulize(u'İlham Əliyev')
        assert u'휘세인 에레블린스키' == self.hangulize(u'Hüseyn Ərəblinski')
        assert u'레시트 베흐부도프' == self.hangulize(u'Rəşid Behbudov')
        assert u'뷜뷜' == self.hangulize(u'Bülbül')
        assert u'제페르 자발르' == self.hangulize(u'Cəfər Cabbarlı')
        assert u'바기프 자바도프' == self.hangulize(u'Vaqif Cavadov')
        assert u'휘세인 자비트' == self.hangulize(u'Hüseyn Cavid')
        assert u'퓌줄리' == self.hangulize(u'Füzuli')
        assert u'위제이르 하즈베요프' == self.hangulize(u'Üzeyir Hacıbəyov')
        assert u'메흐디 휘세인자데' == self.hangulize(u'Mehdi Hüseynzadə')
        assert u'케림 케리모프' == self.hangulize(u'Kərim Kərimov')
        assert u'페리트 만수로프' == self.hangulize(u'Fərid Mansurov')
        assert u'엘누르 멤메들리' == self.hangulize(u'Elnur Məmmədli')
        assert u'메헴메트 뫼블라자데' == self.hangulize(u'Məhəmməd Mövlazadə')
        assert u'에지제 무스타파자데' == self.hangulize(u'Əzizə Mustafazadə')
        assert u'바기프 무스타파자데' == self.hangulize(u'Vaqif Mustafazadə')
        assert u'미카이을 뮈슈피크' == self.hangulize(u'Mikayıl Müşfiq')
        assert u'후르시드바누 나테반' == self.hangulize(u'Xurşidbanu Natəvan')
        assert u'휘세인 한 나흐츠반스키' == \
               self.hangulize(u'Hüseyn xan Naxçıvanski')
        assert u'네리만 네리마노프' == self.hangulize(u'Nəriman Nərimanov')
        assert u'이마데딘 네시미' == self.hangulize(u'İmadəddin Nəsimi')
        assert u'미르뫼흐쉰 네바프' == self.hangulize(u'Mir-Möhsün Nəvvab')
        assert u'라밀 굴리예프' == self.hangulize(u'Ramil Quliyev')
        assert u'니가르 레피베일리' == self.hangulize(u'Nigar Rəfibəyli')
        assert u'아르투르 레시자데' == self.hangulize(u'Artur Rəsizadə')
        assert u'메헴메트 에민 레술자데' == \
               self.hangulize(u'Məhəmməd Əmin Rəsulzadə')
        assert u'쉴레이만 뤼스템' == self.hangulize(u'Süleyman Rüstəm')
        assert u'레술 르자' == self.hangulize(u'Rəsul Rza')
        assert u'레샤트 사드고프' == self.hangulize(u'Rəşad Sadıqov')
        assert u'멤메트 아가 샤흐타흐틴스키' == \
               self.hangulize(u'Məmməd ağa Şahtaxtinski')
        assert u'메헴메트휘세인 셰흐리야르' == \
               self.hangulize(u'Məhəmmədhüseyn Şəhriyar')
        assert u'니가르 시으흘린스카야' == self.hangulize(u'Nigar Şıxlinskaya')
        assert u'제이날라브딘 타그예프' == \
               self.hangulize(u'Zeynalabdin Tağıyev')
        assert u'아이셀 테이무르자데' == self.hangulize(u'Aysel Teymurzadə')
        assert u'세메트 부르군' == self.hangulize(u'Səməd Vurğun')
        assert u'페텔리 한 호이스키' == self.hangulize(u'Fətəli xan Xoyski')

    def test_places(self):
        assert u'압셰론' == self.hangulize(u'Abşeron')
        assert u'아그담' == self.hangulize(u'Ağdam')
        assert u'아제르바이잔' == self.hangulize(u'Azərbaycan')
        assert u'바크' == self.hangulize(u'Bakı')
        assert u'겐제' == self.hangulize(u'Gəncə')
        assert u'이체리 셰헤르' == self.hangulize(u'İçəri Şəhər')
        assert u'렌케란' == self.hangulize(u'Lənkəran')
        assert u'민게체비르' == self.hangulize(u'Mingəçevir')
        assert u'나프탈란' == self.hangulize(u'Naftalan')
        assert u'나흐츠반' == self.hangulize(u'Naxçıvan')
        assert u'게벨레' == self.hangulize(u'Qəbələ')
        assert u'고부스탄' == self.hangulize(u'Qobustan')
        assert u'살리안' == self.hangulize(u'Salyan')
        assert u'숨가이으트' == self.hangulize(u'Sumqayıt')
        assert u'셰키' == self.hangulize(u'Şəki')
        assert u'솀키르' == self.hangulize(u'Şəmkir')
        assert u'시르반' == self.hangulize(u'Şirvan')
        assert u'탈르슈' == self.hangulize(u'Talış')
        assert u'토부스' == self.hangulize(u'Tovuz')
        assert u'하치마스' == self.hangulize(u'Xaçmaz')
        assert u'흐날르크' == self.hangulize(u'Xınalıq')
        assert u'흐르달란' == self.hangulize(u'Xırdalan')
        assert u'예블라흐' == self.hangulize(u'Yevlax')
        assert u'자가탈라' == self.hangulize(u'Zaqatala')

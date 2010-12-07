# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.lit import Lithuanian


class LithuanianTestCase(HangulizeTestCase):

    lang = Lithuanian()

    def test_people(self):
        assert u'발다스 아담쿠스' == self.hangulize(u'Valdas Adamkus')
        assert u'비르길리유스 알레크나' == self.hangulize(u'Virgilijus Alekna')
        assert u'알기르다스' == self.hangulize(u'Algirdas')
        assert u'유르기스 발트루샤이티스' == \
               self.hangulize(u'Jurgis Baltrušaitis')
        assert u'게디미나스 바라비카스' == \
               self.hangulize(u'Gediminas Baravykas')
        assert u'요나스 바사나비추스' == self.hangulize(u'Jonas Basanavičius')
        assert u'베르나르다스 브라즈조니스' == \
               self.hangulize(u'Bernardas Brazdžionis')
        assert u'엘레나 추다코바' == self.hangulize(u'Elena Čiudakova')
        assert u'추를료니스' == self.hangulize(u'Čiurlionis')
        assert u'토마스 다닐레비추스' == self.hangulize(u'Tomas Danilevičius')
        assert u'시모나스 다우칸타스' == self.hangulize(u'Simonas Daukantas')
        assert u'유르기스 돕케비추스' == self.hangulize(u'Jurgis Dobkevičius')
        assert u'게디미나스' == self.hangulize(u'Gediminas')
        assert u'비타스 게룰라이티스' == self.hangulize(u'Vitas Gerulaitis')
        assert u'마리야 김부티에네' == self.hangulize(u'Marija Gimbutienė')
        assert u'달랴 그리바우스카이테' == \
               self.hangulize(u'Dalia Grybauskaitė')
        assert u'라우리나스 구체비추스' == \
               self.hangulize(u'Laurynas Gucevičius')
        assert u'지드루나스 일가우스카스' == \
               self.hangulize(u'Žydrūnas Ilgauskas')
        assert u'요나스 야블론스키스' == self.hangulize(u'Jonas Jablonskis')
        assert u'에드가라스 양카우스카스' == \
               self.hangulize(u'Edgaras Jankauskas')
        assert u'샤루나스 야시케비추스' == \
               self.hangulize(u'Šarūnas Jasikevičius')
        assert u'요가일라' == self.hangulize(u'Jogaila')
        assert u'케스투티스' == self.hangulize(u'Kęstutis')
        assert u'리나스 클레이자' == self.hangulize(u'Linas Kleiza')
        assert u'콘스탄티나스' == self.hangulize(u'Konstantinas')
        assert u'요나스 쿠빌류스' == self.hangulize(u'Jonas Kubilius')
        assert u'빈차스 쿠디르카' == self.hangulize(u'Vincas Kudirka')
        assert u'마이로니스' == self.hangulize(u'Maironis')
        assert u'샤루나스 마르출료니스' == \
               self.hangulize(u'Šarūnas Marčiulionis')
        assert u'미칼로유스' == self.hangulize(u'Mikalojus')
        assert u'민다우가스' == self.hangulize(u'Mindaugas')
        assert u'아르미나스 나르베코바스' == \
               self.hangulize(u'Arminas Narbekovas')
        assert u'살로메야 네리스' == self.hangulize(u'Salomėja Nėris')
        assert u'마르티나스 마주비다스' == self.hangulize(u'Martynas Mažvydas')
        assert u'미콜라스 클레오파스 오긴스키스' == \
               self.hangulize(u'Mykolas Kleopas Oginskis')
        assert u'로베르타스 포슈쿠스' == self.hangulize(u'Robertas Poškus')
        assert u'카지미에라 프룬스키에네' == \
               self.hangulize(u'Kazimiera Prunskienė')
        assert u'요누샤스 라드빌라' == self.hangulize(u'Jonušas Radvila')
        assert u'뵬레타 랴우비슈키테' == self.hangulize(u'Violeta Riaubiškytė')
        assert u'아르비다스 사보니스' == self.hangulize(u'Arvydas Sabonis')
        assert u'안타나스 스메토나' == self.hangulize(u'Antanas Smetona')
        assert u'다류스 송가일라' == self.hangulize(u'Darius Songaila')
        assert u'마류스 스탕케비추스' == self.hangulize(u'Marius Stankevičius')
        assert u'비타우타스 스트라이지스' == \
               self.hangulize(u'Vytautas Straižys')
        assert u'데이비다스 솀베라스' == self.hangulize(u'Deividas Šemberas')
        assert u'라무나스 시슈카우스카스' == \
               self.hangulize(u'Ramūnas Šiškauskas')
        assert u'유오자스 우르프시스' == self.hangulize(u'Juozas Urbšys')
        assert u'비타우타스' == self.hangulize(u'Vytautas')

    def test_places(self):
        assert u'알리투스' == self.hangulize(u'Alytus')
        assert u'비르자이' == self.hangulize(u'Biržai')
        assert u'두빙갸이' == self.hangulize(u'Dubingiai')
        assert u'카우나스' == self.hangulize(u'Kaunas')
        assert u'케르나베' == self.hangulize(u'Kernavė')
        assert u'클라이페다' == self.hangulize(u'Klaipėda')
        assert u'마리얌폴레' == self.hangulize(u'Marijampolė')
        assert u'마제이캬이' == self.hangulize(u'Mažeikiai')
        assert u'파네베지스' == self.hangulize(u'Panevėžys')
        assert u'샤울랴이' == self.hangulize(u'Šiauliai')
        assert u'트라카이' == self.hangulize(u'Trakai')
        assert u'빌뉴스' == self.hangulize(u'Vilnius')

# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.lit import Lithuanian


class LithuanianTestCase(HangulizeTestCase):

    lang = Lithuanian()

    def test_people(self):
        self.assert_examples({
            u'Valdas Adamkus': u'발다스 아담쿠스',
            u'Virgilijus Alekna': u'비르길리유스 알레크나',
            u'Algirdas': u'알기르다스',
            u'Jurgis Baltrušaitis': u'유르기스 발트루샤이티스',
            u'Gediminas Baravykas': u'게디미나스 바라비카스',
            u'Jonas Basanavičius': u'요나스 바사나비추스',
            u'Bernardas Brazdžionis': u'베르나르다스 브라즈조니스',
            u'Elena Čiudakova': u'엘레나 추다코바',
            u'Čiurlionis': u'추를료니스',
            u'Tomas Danilevičius': u'토마스 다닐레비추스',
            u'Simonas Daukantas': u'시모나스 다우칸타스',
            u'Jurgis Dobkevičius': u'유르기스 돕케비추스',
            u'Gediminas': u'게디미나스',
            u'Vitas Gerulaitis': u'비타스 게룰라이티스',
            u'Marija Gimbutienė': u'마리야 김부티에네',
            u'Dalia Grybauskaitė': u'달랴 그리바우스카이테',
            u'Laurynas Gucevičius': u'라우리나스 구체비추스',
            u'Žydrūnas Ilgauskas': u'지드루나스 일가우스카스',
            u'Jonas Jablonskis': u'요나스 야블론스키스',
            u'Edgaras Jankauskas': u'에드가라스 양카우스카스',
            u'Šarūnas Jasikevičius': u'샤루나스 야시케비추스',
            u'Jogaila': u'요가일라',
            u'Kęstutis': u'케스투티스',
            u'Linas Kleiza': u'리나스 클레이자',
            u'Konstantinas': u'콘스탄티나스',
            u'Jonas Kubilius': u'요나스 쿠빌류스',
            u'Vincas Kudirka': u'빈차스 쿠디르카',
            u'Maironis': u'마이로니스',
            u'Šarūnas Marčiulionis': u'샤루나스 마르출료니스',
            u'Mikalojus': u'미칼로유스',
            u'Mindaugas': u'민다우가스',
            u'Arminas Narbekovas': u'아르미나스 나르베코바스',
            u'Salomėja Nėris': u'살로메야 네리스',
            u'Martynas Mažvydas': u'마르티나스 마주비다스',
            u'Mykolas Kleopas Oginskis': u'미콜라스 클레오파스 오긴스키스',
            u'Robertas Poškus': u'로베르타스 포슈쿠스',
            u'Kazimiera Prunskienė': u'카지미에라 프룬스키에네',
            u'Jonušas Radvila': u'요누샤스 라드빌라',
            u'Violeta Riaubiškytė': u'뵬레타 랴우비슈키테',
            u'Arvydas Sabonis': u'아르비다스 사보니스',
            u'Antanas Smetona': u'안타나스 스메토나',
            u'Darius Songaila': u'다류스 송가일라',
            u'Marius Stankevičius': u'마류스 스탕케비추스',
            u'Vytautas Straižys': u'비타우타스 스트라이지스',
            u'Deividas Šemberas': u'데이비다스 솀베라스',
            u'Ramūnas Šiškauskas': u'라무나스 시슈카우스카스',
            u'Juozas Urbšys': u'유오자스 우르프시스',
            u'Vytautas': u'비타우타스',
        })

    def test_places(self):
        self.assert_examples({
            u'Alytus': u'알리투스',
            u'Biržai': u'비르자이',
            u'Dubingiai': u'두빙갸이',
            u'Įsrutis': u'이스루티스',
            u'Kaunas': u'카우나스',
            u'Kernavė': u'케르나베',
            u'Klaipėda': u'클라이페다',
            u'Marijampolė': u'마리얌폴레',
            u'Mažeikiai': u'마제이캬이',
            u'Panevėžys': u'파네베지스',
            u'Šiauliai': u'샤울랴이',
            u'Trakai': u'트라카이',
            u'Vilnius': u'빌뉴스',
        })
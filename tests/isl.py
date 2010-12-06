# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.isl import Icelandic


class IcelandicTestCase(HangulizeTestCase):

    lang = Icelandic()

    def test_people(self):
        assert u'아그나르 헬가손' == self.hangulize(u'Agnar Helgason')
        assert u'아우구스타 에바 에를렌스도티르' == \
               self.hangulize(u'Ágústa Eva Erlendsdóttir')
        assert u'알베르트 그뷔드뮌손' == self.hangulize(u'Albert Guðmundsson')
        assert u'아리 소르길손' == self.hangulize(u'Ari Þorgilsson')
        assert u'아르드날뒤르 인드리다손' == \
               self.hangulize(u'Arnaldur Indriðason')
        assert u'아우르드니 마그누손' == self.hangulize(u'Árni Magnússon')
        assert u'아우르드니 시그푸손' == self.hangulize(u'Árni Sigfússon')
        assert u'아우스게이르 아우스게이르손' == \
               self.hangulize(u'Ásgeir Ásgeirsson')
        assert u'아우스게이르 헬가손' == self.hangulize(u'Ásgeir Helgason')
        assert u'아우스게이르 시귀르빈손' == \
               self.hangulize(u'Ásgeir Sigurvinsson')
        assert u'아우스뮌뒤르 스베인손' == self.hangulize(u'Ásmundur Sveinsson')
        assert u'발타사르 코르마우퀴르' == self.hangulize(u'Baltasar Kormákur')
        assert u'비외르골뷔르 그뷔드뮌손' == \
               self.hangulize(u'Björgólfur Guðmundsson')
        assert u'비외르골뷔르 소르 비외르골프손' == \
               self.hangulize(u'Björgólfur Thor Björgólfsson')
        assert u'비외르그빈 하들도르손' == \
               self.hangulize(u'Björgvin Halldórsson')
        assert u'비외르크 그뷔드뮌스도티르' == \
               self.hangulize(u'Björk Guðmundsdóttir')
        assert u'비외르든 비아르드나손' == self.hangulize(u'Björn Bjarnason')
        assert u'비외르든 흘리뉘르 하랄손' == \
               self.hangulize(u'Björn Hlynur Haraldsson')
        assert u'브라이이 올라프손' == self.hangulize(u'Bragi Ólafsson')
        assert u'다비드 오드손' == self.hangulize(u'Davíð Oddsson')
        assert u'다비드 스테파운손' == self.hangulize(u'Davíð Stefánsson')
        assert u'에게르트 파울손' == self.hangulize(u'Eggert Pálsson')
        assert u'에이뒤르 스마우리 그뷔드요흔센' == \
               self.hangulize(u'Eiður Smári Guðjohnsen')
        assert u'에이나르 바우르다르손' == self.hangulize(u'Einar Bárðarson')
        assert u'에이나르 베네딕츠손' == self.hangulize(u'Einar Benediktsson')
        assert u'에이나르 하우코나르손' == self.hangulize(u'Einar Hákonarson')
        assert u'에이나르 혜르들레이프손 크바란' == \
               self.hangulize(u'Einar Hjörleifsson Kvaran')
        assert u'에이나르 욘손' == self.hangulize(u'Einar Jónsson')
        assert u'에이나르 카우라손' == self.hangulize(u'Einar Kárason')
        assert u'에이나르 마우르 그뷔드뮌손' == \
               self.hangulize(u'Einar Már Guðmundsson')
        assert u'에이나르 외르든 베네딕츠손' == \
               self.hangulize(u'Einar Örn Benediktsson')
        assert u'에이리퀴르 뢰이디' == self.hangulize(u'Eiríkur rauði')
        assert u'에이리퀴르 회익손' == self.hangulize(u'Eiríkur Hauksson')
        assert u'에밀리아나 토리니 다비스도티르' == \
               self.hangulize(u'Emilíana Torrini Davíðsdóttir')
        assert u'프레이디스 에이릭스도티르' == \
               self.hangulize(u'Freydís Eiríksdóttir')
        assert u'프리드리크 올라프손' == self.hangulize(u'Friðrik Ólafsson')
        assert u'프리드리크 소르 프리드릭손' == \
               self.hangulize(u'Friðrik Þór Friðriksson')
        assert u'가르다르' == self.hangulize(u'Garðar')
        assert u'게이르 힐마르' == self.hangulize(u'Geir Hilmar')
        assert u'기슬리 그뷔드욘손' == self.hangulize(u'Gisli Gudjonsson')
        assert u'기슬리 외르든 가르다르손' == \
               self.hangulize(u'Gísli Örn Garðarsson')
        assert u'기슬리 파울손' == self.hangulize(u'Gísli Pálsson')
        assert u'그뷔드뮌뒤르 아라손' == self.hangulize(u'Guðmundur Arason')
        assert u'그뷔드뮌뒤르 하갈린' == self.hangulize(u'Guðmundur Hagalín')
        assert u'그뷔드리뒤르 소르비아르드나르도티르' == \
               self.hangulize(u'Guðríður Þorbjarnardóttir')
        assert u'귄프리뒤르 욘스도티르' == \
               self.hangulize(u'Gunnfríður Jónsdóttir')
        assert u'하프디스 휠드' == self.hangulize(u'Hafdís Huld')
        assert u'하들도르 아우스그림손' == self.hangulize(u'Halldór Ásgrímsson')
        assert u'하들도르 블뢴달' == self.hangulize(u'Halldór Blöndal')
        assert u'하들도르 킬리안 락스네스' == \
               self.hangulize(u'Halldór Kiljan Laxness')
        assert u'하들그리뮈르 헬가손' == self.hangulize(u'Hallgrímur Helgason')
        assert u'한네스 하프스테인' == self.hangulize(u'Hannes Hafstein')
        assert u'한네스 홀름스테이든 기쉬라르손' == \
               self.hangulize(u'Hannes Hólmsteinn Gissurarson')
        assert u'한니발 발디마르손' == self.hangulize(u'Hannibal Valdimarsson')
        assert u'회이퀴르 토마손' == self.hangulize(u'Haukur Tómasson')
        assert u'헤이다르 헬귀손' == self.hangulize(u'Heiðar Helguson')
        assert u'헬기 발디마르손' == self.hangulize(u'Helgi Valdimarsson')
        assert u'헤르만 흐레이다르손' == self.hangulize(u'Hermann Hreiðarsson')
        assert u'힐마르 외르든 힐마르손' == \
               self.hangulize(u'Hilmar Örn Hilmarsson')
        assert u'힐미르 스나이르 그뷔드나손' == \
               self.hangulize(u'Hilmir Snær Guðnason')
        assert u'홀름프리뒤르 카르들스도티르' == \
               self.hangulize(u'Hólmfríður Karlsdóttir')
        assert u'흐라픈 귄뢰익손' == self.hangulize(u'Hrafn Gunnlaugsson')
        assert u'흐레이다르 마우르 시귀르손' == \
               self.hangulize(u'Hreiðar Már Sigurðsson')
        assert u'잉골뷔르 아르드나르손' == self.hangulize(u'Ingólfur Arnarson')
        assert u'이슬레이뷔르 기쉬라르손' == \
               self.hangulize(u'Ísleifur Gissurarson')
        assert u'이바르 잉기마르손' == self.hangulize(u'Ívar Ingimarsson')
        assert u'요한나 시귀르다르도티르' == \
               self.hangulize(u'Jóhanna Sigurðardóttir')
        assert u'요한네스 카르들 그뷔드욘손' == \
               self.hangulize(u'Jóhannes Karl Gudjonsson')
        assert u'요한네스 우르 쾨틀륌' == self.hangulize(u'Jóhannes úr Kötlum')
        assert u'욘 아우스게이르 요한네손' == \
               self.hangulize(u'Jón Ásgeir Jóhannesson')
        assert u'욘 발드빈 한니발손' == \
               self.hangulize(u'Jón Baldvin Hannibalsson')
        assert u'욘 칼만 스테파운손' == self.hangulize(u'Jón Kalman Stefánsson')
        assert u'욘 레이프스' == self.hangulize(u'Jón Leifs')
        assert u'욘 로프츠손' == self.hangulize(u'Jón Loftsson')
        assert u'욘 파우들 시그마르손' == self.hangulize(u'Jón Páll Sigmarsson')
        assert u'욘 시귀르손' == self.hangulize(u'Jón Sigurðsson')
        assert u'욘 소로드센' == self.hangulize(u'Jón Thoroddsen')
        assert u'요나스 하들그림손' == self.hangulize(u'Jónas Hallgrímsson')
        assert u'카우리 스테파운손' == self.hangulize(u'Kári Stefánsson')
        assert u'캬르탄 올라프손' == self.hangulize(u'Kjartan Ólafsson')
        assert u'콜베이든 튀마손' == self.hangulize(u'Kolbeinn Tumason')
        assert u'크리스틴 마리아 발뒤르스도티르' == \
               self.hangulize(u'Kristín Marja Baldursdóttir')
        assert u'크리스티아운 엘디아우르든' == \
               self.hangulize(u'Kristján Eldjárn')
        assert u'레이뷔르 에이릭손' == self.hangulize(u'Leifur Eiríksson')
        assert u'린다 피에튀르스도티르' == self.hangulize(u'Linda Pétursdóttir')
        assert u'로프튀르 사이뮌손' == self.hangulize(u'Loftur Sæmundsson')
        assert u'마그누스 마그누손' == self.hangulize(u'Magnús Magnússon')
        assert u'마그누스 소르스테인손' == \
               self.hangulize(u'Magnús Þorsteinsson')
        assert u'마그누스 베르 마그누손' == \
               self.hangulize(u'Magnús Ver Magnússon')
        assert u'마르그리에트 헤르만스 외이다르도티르' == \
               self.hangulize(u'Margrét Hermanns Auðardóttir')
        assert u'마르그리에트 빌햐울름스도티르' == \
               self.hangulize(u'Margrét Vilhjálmsdóttir')
        assert u'마르쿠스 외르든 안톤손' == \
               self.hangulize(u'Markús Örn Antonsson')
        assert u'뮈이이손' == self.hangulize(u'Mugison')
        assert u'니나 되그 필리퓌스도티르' == \
               self.hangulize(u'Nína Dögg Filippusdóttir')
        assert u'올라뷔르 다리 올라프손' == \
               self.hangulize(u'Ólafur Darri Ólafsson')
        assert u'올라뷔르 에이이들 올라프손' == \
               self.hangulize(u'Ólafur Egill Ólafsson')
        assert u'올라뷔르 요한 올라프손' == \
               self.hangulize(u'Ólafur Jóhann Ólafsson')
        assert u'올라뷔르 라그나르 그림손' == \
               self.hangulize(u'Ólafur Ragnar Grímsson')
        assert u'외르바르 소레이야르손 스마우라손' == \
               self.hangulize(u'Örvar Þóreyjarson Smárason')
        assert u'파우들 스쿨라손' == self.hangulize(u'Páll Skúlason')
        assert u'라그나르 비아르드나손' == self.hangulize(u'Ragnar Bjarnason')
        assert u'라그나르 브라가손' == self.hangulize(u'Ragnar Bragason')
        assert u'라근헤이뒤르 그뢴달' == self.hangulize(u'Ragnheiður Gröndal')
        assert u'실비아 노트' == self.hangulize(u'Silvía Nótt')
        assert u'시귀르뒤르 헬가손' == self.hangulize(u'Sigurður Helgason')
        assert u'시귀르뒤르 노르달' == self.hangulize(u'Sigurður Nordal')
        assert u'시귀르뒤르 소라린손' == self.hangulize(u'Sigurður Þórarinsson')
        assert u'숀' == self.hangulize(u'Sjón')
        assert u'스노리 햐르타르손' == self.hangulize(u'Snorri Hjartarson')
        assert u'스노리 스튀르들뤼손' == self.hangulize(u'Snorri Sturluson')
        assert u'스테잉그리뮈르 헤르만손' == \
               self.hangulize(u'Steingrímur Hermannsson')
        assert u'스테이뉜 시귀르다르도티르' == \
               self.hangulize(u'Steinunn Sigurðardóttir')
        assert u'스테파운 그뷔드뮌뒤르 그뷔드뮌손' == \
               self.hangulize(u'Stefán Guðmundur Guðmundsson')
        assert u'스베이든 비외르든손' == self.hangulize(u'Sveinn Björnsson')
        assert u'소라 마그누스도티르' == self.hangulize(u'Þóra Magnúsdóttir')
        assert u'소라린 엘디아우르든' == self.hangulize(u'Þórarinn Eldjárn')
        assert u'소르베르귀르 소르다르손' == \
               self.hangulize(u'Þórbergur Þórðarson')
        assert u'소르핀뉘르 카르들세프니' == \
               self.hangulize(u'Þorfinnur Karlsefni')
        assert u'소르게이르 소르켈손 리오스베트닝가고디' == \
               self.hangulize(u'Þorgeirr Þorkelsson Ljósvetningagoði')
        assert u'소르케들 아틀라손' == self.hangulize(u'Thorkell Atlason')
        assert u'소르스테이든 길바손' == self.hangulize(u'Þorsteinn Gylfason')
        assert u'소르스테이든 파울손' == self.hangulize(u'Þorsteinn Pálsson')
        assert u'소르발뒤르 에이릭손' == self.hangulize(u'Þorvaldur Eiríksson')
        assert u'틴나 귄뢰익스도티르' == \
               self.hangulize(u'Tinna Gunnlaugsdóttir')
        assert u'토마스 그뷔드뮌손' == self.hangulize(u'Tómas Guðmundsson')
        assert u'윈뉘르 비르드나 빌햐울름스도티르' == \
               self.hangulize(u'Unnur Birna Vilhjálmsdóttir')
        assert u'발라 플로사도티르' == self.hangulize(u'Vala Flosadottir')
        assert u'비그디스 핀보가도티르' == \
               self.hangulize(u'Vigdís Finnbogadóttir')
        assert u'비그디스 그림스도티르' == self.hangulize(u'Vigdís Grímsdóttir')
        assert u'빅토르 아르드나르 잉골프손' == \
               self.hangulize(u'Viktor Arnar Ingólfsson')
        assert u'빌햐울뮈르 아우르드나손' == \
               self.hangulize(u'Vilhjálmur Árnason')
        assert u'빌햐울뮈르 스테파운손' == \
               self.hangulize(u'Vilhjálmur Stefánsson')

    def test_places(self):
        assert u'아크라네스' == self.hangulize(u'Akranes')
        assert u'아퀴레이리' == self.hangulize(u'Akureyri')
        assert u'블뢴도스' == self.hangulize(u'Blöndós')
        assert u'볼룽가르비크' == self.hangulize(u'Bolungarvík')
        assert u'보르가피외르뒤르' == self.hangulize(u'Borgafjörður')
        assert u'보르가네스' == self.hangulize(u'Borganes')
        assert u'달비크' == self.hangulize(u'Dalvík')
        assert u'디우피보귀르' == self.hangulize(u'Djúpivogur')
        assert u'에이일스타디르' == self.hangulize(u'Egilsstaðir')
        assert u'에이야피아들라예퀴들' == self.hangulize(u'Eyjafjallajökull')
        assert u'고다포스' == self.hangulize(u'Goðafoss')
        assert u'그림세이' == self.hangulize(u'Grímsey')
        assert u'그린다비크' == self.hangulize(u'Grindavík')
        assert u'하프나르피외르뒤르' == self.hangulize(u'Hafnarfjörður')
        assert u'회픈 이 호르드나피르디' == self.hangulize(u'Höfn í Hornafirði')
        assert u'호프스예퀴들' == self.hangulize(u'Hofsjökull')
        assert u'홀마비크' == self.hangulize(u'Hólmavík')
        assert u'후사비크' == self.hangulize(u'Húsavík')
        assert u'크밤스타웅기' == self.hangulize(u'Hvammstangi')
        assert u'크비타' == self.hangulize(u'Hvíta')
        assert u'크볼스뵈들뤼르' == self.hangulize(u'Hvolsvöllur')
        assert u'이사피외르뒤르' == self.hangulize(u'Ísafjörður')
        assert u'케플라비크' == self.hangulize(u'Keflavík')
        assert u'코파보귀르' == self.hangulize(u'Kópavogur')
        assert u'라가르플리올트' == self.hangulize(u'Lagarfljólt')
        assert u'라웅그예퀴들' == self.hangulize(u'Langjökull')
        assert u'모스펠스바이르' == self.hangulize(u'Mosfellsbær')
        assert u'미르달스예퀴들' == self.hangulize(u'Mýrdalsjökull')
        assert u'미바튼' == self.hangulize(u'Mývatn')
        assert u'네스쾨이프스타뒤르' == self.hangulize(u'Neskaupstaður')
        assert u'니아르드비크' == self.hangulize(u'Njarðvík')
        assert u'올라프스피외르뒤르' == self.hangulize(u'Ólafsfjörður')
        assert u'올라프스비크' == self.hangulize(u'Ólafsvík')
        assert u'뢰이바르회픈' == self.hangulize(u'Raufarhöfn')
        assert u'레이캬네스' == self.hangulize(u'Reykjanes')
        assert u'레이캬비크' == self.hangulize(u'Reykjavík')
        assert u'쇠이다우르크로퀴르' == self.hangulize(u'Sauðárkrókur')
        assert u'셀포스' == self.hangulize(u'Selfoss')
        assert u'세이디스피외르뒤르' == self.hangulize(u'Seyðisfjörður')
        assert u'시글뤼피외르뒤르' == self.hangulize(u'Siglufjörður')
        assert u'스캬울반다플리오트' == self.hangulize(u'Skjálfandafljót')
        assert u'스티키스홀뮈르' == self.hangulize(u'Stykkishólmur')
        assert u'쉬르트세이' == self.hangulize(u'Surtsey')
        assert u'바트나예퀴들' == self.hangulize(u'Vatnajökull')
        assert u'비크' == self.hangulize(u'Vík')
        assert u'보프나피외르뒤르' == self.hangulize(u'Vopnafjörður')
        assert u'싱그베들리르' == self.hangulize(u'Þingvellir')
        assert u'시오르사우' == self.hangulize(u'Þjórsá')
        assert u'소리스바튼' == self.hangulize(u'Þórisvatn')
        assert u'소를라욱스회픈' == self.hangulize(u'Þorlákshöfn')
        assert u'소르스회픈' == self.hangulize(u'Þórshöfn')

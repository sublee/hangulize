# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.tur import Turkish


class TurkishTestCase(HangulizeTestCase):

    lang = Turkish()

    def test_people(self):
        assert u'사이트 파이크 아바스야느크' == \
               self.hangulize(u'Sait Faik Abasıyanık')
        assert u'알리 쿠슈추' == self.hangulize(u'Ali Kuşçu')
        assert u'하미트 알튼토프' == self.hangulize(u'Hamit Altıntop')
        assert u'무스타파 케말 아타튀르크' == \
               self.hangulize(u'Mustafa Kemal Atatürk')
        assert u'가라베트 아미라 발리안' == \
               self.hangulize(u'Garabet Amira Balyan')
        assert u'크리코르 발리안' == self.hangulize(u'Krikor Balyan')
        assert u'니고오스 발리안' == self.hangulize(u'Nigoğos Balyan')
        assert u'바타니' == self.hangulize(u'Battani')
        assert u'휘세인 찰라얀' == self.hangulize(u'Hüseyin Çağlayan')
        assert u'쉴레이만 첼레비' == self.hangulize(u'Süleyman Çelebi')
        assert u'라우프 덴크타슈' == self.hangulize(u'Rauf Denktaş')
        assert u'뷜렌트 에제비트' == self.hangulize(u'Bülent Ecevit')
        assert u'아흐메트 미타트 에펜디' == \
               self.hangulize(u'Ahmet Mithat Efendi')
        assert u'유누스 엠레' == self.hangulize(u'Yunus Emre')
        assert u'레제프 타이이프 에르도안' == \
               self.hangulize(u'Recep Tayyip Erdoğan')
        assert u'세르타브 에레네르' == self.hangulize(u'Sertab Erener')
        assert u'테브피크 피크레트' == self.hangulize(u'Tevfik Fikret')
        assert u'에르투룰 가지' == self.hangulize(u'Ertuğrul Gazi')
        assert u'지야 괴칼프' == self.hangulize(u'Ziya Gökalp')
        assert u'아브둘라흐 귈' == self.hangulize(u'Abdullah Gül')
        assert u'셰놀 귀네슈' == self.hangulize(u'Şenol Güneş')
        assert u'레샤트 누리 귄테킨' == self.hangulize(u'Reşat Nuri Güntekin')
        assert u'아흐메드 하심' == self.hangulize(u'Ahmed Hâşim')
        assert u'나즘 히크메트' == self.hangulize(u'Nâzım Hikmet')
        assert u'니하트 카흐베지' == self.hangulize(u'Nihat Kahveci')
        assert u'야쿠프 카드리 카라오스마놀루' == \
               self.hangulize(u'Yakup Kadri Karaosmanoğlu')
        assert u'나므크 케말' == self.hangulize(u'Nâmık Kemal')
        assert u'야샤르 케말' == self.hangulize(u'Yaşar Kemal')
        assert u'파즐 퀴취크' == self.hangulize(u'Fazıl Küçük')
        assert u'일한 만스즈' == self.hangulize(u'İlhan Mansız')
        assert u'나카슈 오스만' == self.hangulize(u'Nakkaş Osman')
        assert u'오르한 파무크' == self.hangulize(u'Orhan Pamuk')
        assert u'오스만 함디 베이' == self.hangulize(u'Osman Hamdi Bey')
        assert u'피르 술탄 아브달' == self.hangulize(u'Pir Sultan Abdal')
        assert u'뤼슈튀 레치베르' == self.hangulize(u'Rüştü Reçber')
        assert u'지네트 살리' == self.hangulize(u'Ziynet Sali')
        assert u'외메르 세이페틴' == self.hangulize(u'Ömer Seyfettin')
        assert u'카누니 술탄 쉴레이만' == \
               self.hangulize(u'Kanuni Sultan Süleyman')
        assert u'툰자이 샨르' == self.hangulize(u'Tuncay Şanlı')
        assert u'아시으크 베이셀 샤트롤루' == \
               self.hangulize(u'Âşık Veysel Şatıroğlu')
        assert u'마흐주니 셰리프' == self.hangulize(u'Mahzuni Şerif')
        assert u'하칸 쉬퀴르' == self.hangulize(u'Hakan Şükür')
        assert u'타키위딘 이븐 마느프' == \
               self.hangulize(u'Takiyüddin ibn Manıf')
        assert u'타르칸 테베톨루' == self.hangulize(u'Tarkan Tevetoğlu')
        assert u'아르다 투란' == self.hangulize(u'Arda Turan')
        assert u'할리트 지야 우샤클르길' == \
               self.hangulize(u'Halit Ziya Uşaklıgil')

    def test_places(self):
        assert u'아다나' == self.hangulize(u'Adana')
        assert u'아르' == self.hangulize(u'Ağrı')
        assert u'앙카라' == self.hangulize(u'Ankara')
        assert u'안타키아' == self.hangulize(u'Antakya')
        assert u'안탈리아' == self.hangulize(u'Antalya')
        assert u'아리칸다' == self.hangulize(u'Arykanda')
        assert u'베식타슈' == self.hangulize(u'Beşiktaş')
        assert u'부르사' == self.hangulize(u'Bursa')
        assert u'차나칼레' == self.hangulize(u'Çanakkale')
        assert u'차탈회위크' == self.hangulize(u'Çatalhöyük')
        assert u'데니즐리' == self.hangulize(u'Denizli')
        assert u'디브리이' == self.hangulize(u'Divriği')
        assert u'돌마바흐체' == self.hangulize(u'Dolmabahçe')
        assert u'가지안테프' == self.hangulize(u'Gaziantep')
        assert u'하투샤슈' == self.hangulize(u'Hattuşaş')
        assert u'이스탄불' == self.hangulize(u'İstanbul')
        assert u'이즈미르' == self.hangulize(u'İzmir')
        assert u'카파도키아' == self.hangulize(u'Kapadokya')
        assert u'카이세리' == self.hangulize(u'Kayseri')
        assert u'코니아' == self.hangulize(u'Konya')
        assert u'메르신' == self.hangulize(u'Mersin')
        assert u'파무칼레' == self.hangulize(u'Pamukkale')
        assert u'파타라' == self.hangulize(u'Patara')
        assert u'사프란볼루' == self.hangulize(u'Safranbolu')
        assert u'셀추크' == self.hangulize(u'Selçuk')
        assert u'톱카프' == self.hangulize(u'Topkapı')
        assert u'트라브존' == self.hangulize(u'Trabzon')
        assert u'튀르키예' == self.hangulize(u'Türkiye')

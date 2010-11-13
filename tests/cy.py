# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.cy import Welsh


class WelshTestCase(HangulizeTestCase):

    lang = Welsh()

    def test_examples_of_iceager(self):
        assert u'컴리' == self.hangulize(u'Cymru')
        assert u'컴라이그' == self.hangulize(u'Cymraeg')
        assert u'카이르나르본' == self.hangulize(u'Caernarfon')
        assert u'케레디기온' == self.hangulize(u'Ceredigion')
        assert u'아베러스투이스' == self.hangulize(u'Aberystwyth')
        assert u'브런마우르' == self.hangulize(u'Brynmawr')
        assert u'흘란고흘렌' == self.hangulize(u'Llangollen')
        assert u'흘라네흘리' == self.hangulize(u'Llanelli')
        assert u'귀네드' == self.hangulize(u'Gwynedd')
        assert u'어스트라드건라이스' == self.hangulize(u'Ystradgynlais')
        assert u'타웨' == self.hangulize(u'Tawe')
        assert u'포위스' == self.hangulize(u'Powys')
        assert u'메레디스' == self.hangulize(u'Meredith')
        assert u'글런두르' == self.hangulize(u'Glyndŵr')
        assert u'흐리스' == self.hangulize(u'Rhys')
        assert u'이반스' == self.hangulize(u'Ifans')
        assert u'엠리스' == self.hangulize(u'Emrys')
        assert u'허웰' == self.hangulize(u'Hywel')
        assert u'귈림' == self.hangulize(u'Gwilym')
        assert u'흘리노르' == self.hangulize(u'Llinor')
        assert u'예이안' == self.hangulize(u'Ieuan')
        assert u'케리스' == self.hangulize(u'Cerys')
        assert u'다비드' == self.hangulize(u'Dafydd')
        assert u'이완' == self.hangulize(u'Iwan')
        assert u'히우' == self.hangulize(u'Huw')
        assert u'키아란' == self.hangulize(u'Ciaran')
        assert u'머바누이' == self.hangulize(u'Myfanwy')
        assert u'흘러웰린' == self.hangulize(u'Llywelyn')
        assert u'칼레니그' == self.hangulize(u'Calennig')
        assert u'크나판' == self.hangulize(u'cnapan')
        assert u'쿰' == self.hangulize(u'cwm')

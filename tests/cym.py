# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.cym import Welsh


class WelshTestCase(HangulizeTestCase):

    lang = Welsh()

    def test_examples_of_iceager(self):
        self.assert_examples({
            u'Cymru': u'컴리',
            u'Cymraeg': u'컴라이그',
            u'Caernarfon': u'카이르나르본',
            u'Ceredigion': u'케레디기온',
            u'Aberystwyth': u'아베러스투이스',
            u'Brynmawr': u'브런마우르',
            u'Llangollen': u'흘란고흘렌',
            u'Llanelli': u'흘라네흘리',
            u'Gwynedd': u'귀네드',
            u'Ystradgynlais': u'어스트라드건라이스',
            u'Tawe': u'타웨',
            u'Powys': u'포위스',
            u'Meredith': u'메레디스',
            u'Glyndŵr': u'글런두르',
            u'Rhys': u'흐리스',
            u'Ifans': u'이반스',
            u'Emrys': u'엠리스',
            u'Hywel': u'허웰',
            u'Gwilym': u'귈림',
            u'Llinor': u'흘리노르',
            u'Ieuan': u'예이안',
            u'Cerys': u'케리스',
            u'Dafydd': u'다비드',
            u'Iwan': u'이완',
            u'Huw': u'히우',
            u'Ciaran': u'키아란',
            u'Myfanwy': u'머바누이',
            u'Llywelyn': u'흘러웰린',
            u'Calennig': u'칼레니그',
            u'cnapan': u'크나판',
            u'cwm': u'쿰',
            u'fy ngwely': u'벙 웰리',
            u'fy nhadau': u'번 하다이',
            u"Banc Ty'nddôl": u'방크 턴돌',
        })
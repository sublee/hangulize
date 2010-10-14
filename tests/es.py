# -*- coding: utf-8 -*-
from . import HangulizeTestCase


class SpanishTestCase(HangulizeTestCase):

    def setUp(self):
        from hangulize.langs.es import Spanish
        self.lang = Spanish()

    def test_hangulize(self):
        assert u'뇨녜스' == self.hangulize(u'ñoñez')
        assert u'궤레로' == self.hangulize(u'güerrero')
        assert u'귀초' == self.hangulize(u'Güicho')
        assert u'가미뇨' == self.hangulize(u'Gamiño')
        assert u'앙헬레스' == self.hangulize(u'Ángeles')
        assert u'호세 오르테가 이 가세트' == \
               self.hangulize(u'José Ortega y Gasset')


# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.wlm import MiddleWelsh


class MiddleWelshTestCase(HangulizeTestCase):

    lang = MiddleWelsh()

    def test_examples_of_iceager(self):
        assert u'마비노기온' == self.hangulize(u'Mabinogion')
        assert u'퀼후흐' == self.hangulize(u'Culhwch')
        assert u'올웬' == self.hangulize(u'Olwen')
        assert u'탈리에신' == self.hangulize(u'Taliesin')
        assert u'페레뒤르' == self.hangulize(u'Peredur')
        assert u'게라인트' == self.hangulize(u'Geraint')
        assert u'흐로나부이' == self.hangulize(u'Rhonabwy')
        assert u'흐리아논' == self.hangulize(u'Rhiannon')
        assert u'아눈' == self.hangulize(u'Annwn')
        assert u'프러데리' == self.hangulize(u'Pryderi')
        assert u'브란웬' == self.hangulize(u'Brânwen')
        assert u'흘리르' == self.hangulize(u'Llŷr')
        assert u'과울' == self.hangulize(u'Gwawl')
        assert u'벨리 마우르' == self.hangulize(u'Beli Mawr')
        assert u'고바논' == self.hangulize(u'Gofannon')
        assert u'귀네드' == self.hangulize(u'Gwynedd')
        assert u'아리안흐로드' == self.hangulize(u'Arianrhod')
        assert u'마나위단' == self.hangulize(u'Manawydan')
        assert u'궨후이바르' == self.hangulize(u'Gwenhwyfar')

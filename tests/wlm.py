# -*- coding: utf-8 -*-
from tests import HangulizeTestCase
from hangulize.langs.wlm import MiddleWelsh


class MiddleWelshTestCase(HangulizeTestCase):

    lang = MiddleWelsh()

    def test_examples_of_iceager(self):
        self.assert_examples({
            u'Mabinogion': u'마비노기온',
            u'Culhwch': u'퀼후흐',
            u'Olwen': u'올웬',
            u'Taliesin': u'탈리에신',
            u'Peredur': u'페레뒤르',
            u'Geraint': u'게라인트',
            u'Rhonabwy': u'흐로나부이',
            u'Rhiannon': u'흐리아논',
            u'Annwn': u'아눈',
            u'Pryderi': u'프러데리',
            u'Brânwen': u'브란웬',
            u'Llŷr': u'흘리르',
            u'Gwawl': u'과울',
            u'Beli Mawr': u'벨리 마우르',
            u'Gofannon': u'고바논',
            u'Gwynedd': u'귀네드',
            u'Arianrhod': u'아리안흐로드',
            u'Manawydan': u'마나위단',
            u'Gwenhwyfar': u'궨후이바르',
            u'Aneirin': u'아네이린',
            u'Myrddin': u'머르딘',
            u'Llywarch': u'흘러와르흐',
            u'Cad Godeu': u'카드 고데이',
            u'Lleu Llaw Gyffes': u'흘레이 흘라우 거페스',
            u'tynged': u'텅에드',
            u'Chwedlau Odo': u'훼들라이 오도',
            u'Culhwch ac Olwen': u'퀼후흐 악 올웬',
            u'Math fab Mathonwy': u'마스 바브 마소누이',
            u'Pwyll Pendefig Dyfed': u'푸이흘 펜데비그 더베드',
        })
# -*- coding: utf-8 -*-
import unittest
from hangulize import *


class APITestCase(unittest.TestCase):

    def test_all_languages(self):
        from hangulize.langs import *
        assert isinstance(ja, type(unittest))
        assert isinstance(it, type(unittest))
        assert isinstance(es, type(unittest))


class PatternTestCase(unittest.TestCase):

    def setUp(self):
        import logging
        logger = logging.getLogger('test')
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler())
        class TestLang(Language):
            vowels = 'a', 'i', 'u', 'e', 'o'
            voiced = 'b', 'd', 'g'
            voiceless = 'ptk'
            notation = Notation(
                ('zu', Choseong(J), Jungseong(EU)),
                ('ju', (Choseong(J), Jungseong(YU))),
                ('(sh|xh|z)', 'S'),
                ('(<voiceless>|x){@}', 'X'),
                ('X', Choseong(GG)),
                ('S', Choseong(SS)),
                ('p', Choseong(P)),
                ('t', Choseong(T)),
                ('k', Choseong(K)),
                ('b', (Choseong(B),)),
                ('d', (Choseong(D),)),
                ('g', (Choseong(G),)),
                ('a', (Jungseong(A),)),
                ('i', (Jungseong(I),)),
                ('u', (Jungseong(U),)),
            )
        self.lang = TestLang()

    def test_separator(self):
        lang = self.lang
        assert u'싸씨쑤' == hangulize(u'shazixhu', lang=lang)

    def test_variable(self):
        lang = self.lang
        assert u'꾸까끼꾸' == hangulize(u'xupatiku', lang=lang)
        assert u'프끼꾸' == hangulize(u'ptiku', lang=lang)

    def test_phonemes(self):
        lang = self.lang
        assert u'즈쥬' == hangulize(u'zuju', lang=lang)


class AlgorithmTestCase(unittest.TestCase):

    def test_phunctuation(self):
        """이슈5: 문장부호에 맞붙은 글자가 시작 글자 또는 끝 글자로 인식 안 됨
        http://github.com/sublee/hangulize/issues#issue/5
        """
        assert hangulize(u'nad', 'pl') == hangulize(u'nad,', 'pl')
        assert hangulize(u'jak', 'pl') == hangulize(u'.jak', 'pl')
        assert u'나트 나트 야크 야크' == hangulize(u'nad, nad jak .jak', 'pl')

    def test_wide_letter(self):
        assert u'과괌' == hangulize(u'guaguam', 'es')


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

    def test_variable(self):
        class TestLang(Language):
            vowels = 'a', 'i', 'u'
            voiced = 'b', 'd', 'g'
            voiceless = 'p', 't', 'k'
            notation = Notation(
                ('<voiceless>{@}', 'X'),
                ('X', (Choseong(GG),)),
                ('p', (Choseong(P),)),
                ('t', (Choseong(T),)),
                ('k', (Choseong(K),)),
                ('b', (Choseong(B),)),
                ('d', (Choseong(D),)),
                ('g', (Choseong(G),)),
                ('a', (Jungseong(A),)),
                ('i', (Jungseong(I),)),
                ('u', (Jungseong(U),)),
            )
        lang = TestLang()
        assert u'까끼꾸' == hangulize(u'patiku', lang=lang)
        assert u'프끼꾸' == hangulize(u'ptiku', lang=lang)


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


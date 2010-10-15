# -*- coding: utf-8 -*-
import unittest
from hangulize import hangulize


class APITestCase(unittest.TestCase):

    def test_all_languages(self):
        from hangulize.langs import *
        assert isinstance(ja, type(unittest))
        assert isinstance(it, type(unittest))
        assert isinstance(es, type(unittest))


class AlgorithmTestCase(unittest.TestCase):

    def test_phunctuation(self):
        """이슈5: 문장부호에 맞붙은 글자가 시작 글자 또는 끝 글자로 인식 안 됨
        http://github.com/sublee/hangulize/issues#issue/5
        """
        assert hangulize(u'nad', 'pl') == hangulize(u'nad,', 'pl')
        assert hangulize(u'jak', 'pl') == hangulize(u'.jak', 'pl')
        assert u'나트 나트 야크 야크' == hangulize(u'nad, nad jak .jak', 'pl')


# -*- coding: utf-8 -*-
import unittest
from hangulize import *
from tests import HangulizeTestCase


class APITestCase(unittest.TestCase):

    def test_all_languages(self):
        from hangulize.langs import *
        assert isinstance(ja, type(unittest))
        assert isinstance(it, type(unittest))
        assert isinstance(es, type(unittest))


class PatternTestCase(HangulizeTestCase):

    def setUp(self):
        import logging
        logger = logging.getLogger('test')
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler())
        class TestLang(Language):
            vowels = 'a', 'i', 'u', 'e', 'o'
            voiced = 'b', 'd', 'g'
            voiceless = 'ptk'
            longvowels = 'AIUEO'
            cons = 'bcdfghjklmnpqrstvwxyz'
            notation = Notation(
                ('^^l', Choseong(L)),
                ('^l', Choseong(N)),
                ('l', Jongseong(L), Choseong(L)),
                ('q$$', split_phonemes(u'쿸')),
                ('q$', Jongseong(K)),
                ('zu', Choseong(J), Jungseong(EU)),
                ('ju', (Choseong(J), Jungseong(YU))),
                ('(sh|xh|z)', 'S'),
                ('(<voiceless>|x){@}', 'X'),
                ('^^{a}b', Choseong(BB)),
                ('^{a}b', Jongseong(P)),
                ('b{o}$', Choseong(P)),
                ('{a}(<voiceless>)', '<voiced>e'),
                ('{<cons>}<vowels>{gh}', '<longvowels>'),
                ("d'i", 'di'),
                ("d_i", 'di'),
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
                ('e', (Jungseong(E),)),
                ('o', (Jungseong(O),)),
                ('c', (Choseong(C),)),
                ('O', (Jungseong(O), Jungseong(U))),
                ('h$', (Jongseong(H))),
            )
        self.lang = TestLang()

    def test_separator(self):
        assert u'싸씨쑤' == self.hangulize(u'shazixhu')

    def test_variable(self):
        assert u'꾸까끼꾸' == self.hangulize(u'xupatiku')
        assert u'프끼꾸' == self.hangulize(u'ptiku')

    def test_phonemes(self):
        assert u'즈쥬' == self.hangulize(u'zuju')

    def test_caret_before_curly_bracket(self):
        assert u'라 앞바' == self.hangulize(u'la abba')

    def test_dollar_after_curly_bracket(self):
        assert u'브포' == self.hangulize(u'bbo')

    def test_variable_replacement(self):
        assert u'가베' == self.hangulize(u'gap')
        assert u'바게크' == self.hangulize(u'bakk')
        assert u'까데까게' == self.hangulize(u'tatkak')
        assert u'초우긓' == self.hangulize(u'cogh')

    def test_start_of_string(self):
        assert u'랄랄라' == self.hangulize(u'lalala')

    def test_start_of_word(self):
        assert u'랄라 날랄라' == self.hangulize(u'lala lalala')
        assert u'아쁘바' == self.hangulize(u'abba')

    def test_end_of_string(self):
        assert u'바베쿸' == self.hangulize(u'babeq')
        assert u'바벸 꾸' == self.hangulize(u'babeq ku')

    def test_special_character(self):
        assert u'디' == self.hangulize(u"d'i")

    def test_space(self):
        assert u'디' == self.hangulize(u"d i")


class AlgorithmTestCase(unittest.TestCase):

    def test_phunctuation(self):
        """이슈5: 문장부호에 맞붙은 글자가 시작 글자 또는 끝 글자로 인식 안 됨
        http://github.com/sublee/hangulize/issues#issue/5
        """
        assert hangulize(u'nad', 'pl') + ',' == hangulize(u'nad,', 'pl')
        assert '.' + hangulize(u'jak', 'pl') == hangulize(u'.jak', 'pl')
        assert u'나트, 나트 야크 .야크' == hangulize(u'nad, nad jak .jak', 'pl')

    def test_wide_letter(self):
        assert u'과괌' == hangulize(u'guaguam', 'es')

    def test_empty_sequence(self):
        """아무 규칙에도 매치되지 않아 빈 시퀀스가 반환될 때 다음 에러가 발생:

            TypeError: reduce() of empty sequence with no initial value
        """
        assert u'' == hangulize(u'h', 'it')

    def test_special_chars(self):
        assert u'레이르트,' == hangulize(u'leert,', 'nl')

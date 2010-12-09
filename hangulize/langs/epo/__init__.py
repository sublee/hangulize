# -*- coding: utf-8 -*-
from hangulize import *


class Esperanto(Language):
    """For transcribing Esperanto."""

    __iso639__ = {1: 'eo', 2: 'epo', 3: 'epo'}

    vowels = 'a', 'e', 'i', 'o', 'u'
    notation = Notation([
    	('cx',	u'ĉ'),
    	('gx',	u'ĝ'),
        ('hx',	u'ĥ'),
    	('jx',	u'ĵ'),
    	('sx',	u'ŝ'),
    	('ux',	u'ŭ'),
    	('qu',	u'kŭ'),
    	('w',	u'ŭ'),
    	('x',	'ks'),
    	('y',	'i'),
    	(u'ĉ',	'C'),
    	(u'ĝ',	'G'),
        (u'ĥ',	'H'),
    	(u'ĵ',	'J'),
    	(u'ŝ',	'S'),
    	(u'ŭ',	'U'),
    	(u'C',	'Zj'),
    	(u'J',	u'ĝj'),
    	(u'S',	'sj'),
    	('b',	(Choseong(B))),
    	('c',	(Choseong(JJ))),
    	('Z',	(Choseong(C))),
        ('d',	(Choseong(D))),
        ('f',	(Choseong(P))),
        ('g',	(Choseong(G))),
        ('G',	(Choseong(J))),
        ('h',	(Choseong(H))),
        ('H',	(Choseong(H))),
        ('k',	(Choseong(K))),
    	('^l{@}',(Choseong(L))),
        ('{.}l{@}',(Jongseong(L), Choseong(L))),
    	('l{@}',(Choseong(L))),
        ('l',	(Jongseong(L))),
        ('m{@}',(Choseong(M))),
        ('m',   (Jongseong(M))),
        ('n{@}',(Choseong(N))),
        ('n',	(Jongseong(N))),
    	('p',	(Choseong(P))),
        ('r',	(Choseong(L))),
        ('s',	(Choseong(S))),
        ('t',	(Choseong(T))),
        ('v',	(Choseong(B))),
    	('z',	(Choseong(J))),
        ('ja',	(Jungseong(YA))),
        ('je',	(Jungseong(YE))),
        ('ji',	(Jungseong(I))),
        ('jo',	(Jungseong(YO))),
        ('ju',	(Jungseong(YU))),
    	('Ua',	(Jungseong(WA))),
    	('Ue',	(Jungseong(WE))),
    	('Ui',	(Jungseong(WI))),
    	('Uo',	(Jungseong(WEO))),
    	('Uu',	(Jungseong(U))),
        ('a',	(Jungseong(A))),
        ('e',	(Jungseong(E))),
        ('i',	(Jungseong(I))),
        ('o',	(Jungseong(O))),
        ('u',	(Jungseong(U))),
        ('j',	(Jungseong(I))),
    ])


    def normalize(self, string):
        return normalize_roman(string, {
            u'Ĉ': u'ĉ', u'Ĝ': u'ĝ', u'Ĥ': u'ĥ', u'Ĵ': u'ĵ', u'Ŝ': u'ŝ',
            u'Ŭ': u'ŭ'
        })


__lang__ = Esperanto

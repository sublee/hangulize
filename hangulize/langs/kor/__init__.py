# -*- coding: utf-8 -*-
from hangulize import *


class Korean(Language):
    """For transcribing Korean."""

    __iso639__ = {1: 'ko', 2: 'kor', 3: 'kor'}
    
    vowels = u'aeiouAOUyw'
    cons = u'gndrlmbsjchCktpGDBSJNx'
    notation = Notation([
        ('ae',            'A'),
        ('eo',            'O'),
        ('eu',            'U'),
        ('ch',            'C'),
        ('ng{@}',         (Jongseong(N), Choseong(G))),
        ('ng',            'N'),
        ('r',             'l'),
        ('x',             (Choseong(NG),)),
        ('b{@}',          (Choseong(B),)),
        ('b',             (Jongseong(B),)),
        ('C{@}',          (Choseong(C),)),
        ('C',             (Jongseong(C),)),
        ('d{@}',          (Choseong(D),)),
        ('d',             (Jongseong(D),)),
        ('g{@}',          (Choseong(G),)),
        ('g',             (Jongseong(G),)),
        ('j{@}',          (Choseong(J),)),
        ('j',             (Jongseong(J),)),
        ('k{@}',          (Choseong(K),)),
        ('k',             (Jongseong(K),)),
        ('l{@}',          (Choseong(L),)),
        ('l',             (Jongseong(L))),
        ('m{@}',          (Choseong(M),)),
        ('m',             (Jongseong(M),)),
        ('n{@}',          (Choseong(N),)),
        ('n',             (Jongseong(N),)),
        ('N',             (Jongseong(NG),)),
        ('h{@}',          (Choseong(H),)),
        ('h',             (Jongseong(H),)),
        ('p{@}',          (Choseong(P),)),
        ('p',             (Jongseong(P),)),
        ('s{@}',          (Choseong(S),)),
        ('s',             (Jongseong(S),)),
        ('t{@}',          (Choseong(T),)),
        ('t',             (Jongseong(T),)),
        ('ui',            (Jungseong(YI),)),
        ('wa',            (Jungseong(WA),)),
        ('we',            (Jungseong(WE),)),
        ('wA',            (Jungseong(WAE),)),
        ('wo',            (Jungseong(WEO),)),
        ('wu',            (Jungseong(U),)),
        ('wO',            (Jungseong(WEO),)),
        ('wi',            (Jungseong(WI),)),
        ('ya',            (Jungseong(YA),)),
        ('ye',            (Jungseong(YE),)),
        ('yA',            (Jungseong(YAE),)),
        ('yo',            (Jungseong(YO),)),
        ('yu',            (Jungseong(YU),)),
        ('yO',            (Jungseong(YEO),)),
        ('U',             (Jungseong(EU),)),
        ('a',             (Jungseong(A),)),
        ('e',             (Jungseong(E),)),
        ('E',             (Jungseong(E),)),
        ('i',             (Jungseong(I),)),
        ('o',             (Jungseong(O),)),
        ('u',             (Jungseong(U),)),
        ('A',             (Jungseong(AE),)),
        ('O',             (Jungseong(EO),)),
    ])

__lang__ = Korean

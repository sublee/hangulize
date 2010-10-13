# -*- coding: utf-8 -*-
from .. import *


class Spanish(Language):
    """For transcribing Spanish."""

    vowels = 'a', 'e', 'i', 'o', 'u', 'ü', 'y'
    notation = Notation(
        ('ññ',         'ñ'),
        ('ñ{@}',       'nY'),
        ('^y{@}',      'Y'),
        ('{@}y{@}',    'Y'),
        ('y',          'i'),
        ('aa',         'a'),
        ('ee',         'e'),
        ('ii',         'i'),
        ('oo',         'o'),
        ('uu',         'u'),
        ('hh',         'h'),
        ('k$',         'kX'), # X prevents conversion of preceding letter
                              # to jongseong
        ('{@}cc{ei}',  'ks'),
        ('ch{@}',      'C'),
        ('h',          None),
        ('ll',         'Y'),
        ('n{ckgqx}',   'N'),
        ('c{kqx}',     None),
        ('cc',         'c'),
        ('c{ei}',      's'),
        ('c',          'k'),
        ('g{ei}',      'j'),
        ('{gq}ü{aei}', 'W'),
        ('ü',          'u'),
        ('{gq}u{ei}',  None),
        ('{gq}ua',     'Wa'),
        ('q',          'k'),
        ('ww',         'w'),
        ('^w{@}',      'W'),
        ('{@}w{@}',    'W'),
        ('w',          'XW'), # X prevents W from joining with preceding letter
        ('xx',         'x'),
        ('^x{@}',      's'),
        ('{@}x',       'ks'),
        ('bb',         'b'),
        ('dd',         'd'),
        ('ff',         'f'),
        ('gg',         'g'),
        ('jj',         'j'),
        ('kk',         'k'),
        ('mm',         'm'),
        ('nn',         'n'),
        ('pp',         'p'),
        ('rr',         'r'),
        ('z',          's'),
        ('ss',         's'),
        ('tt',         't'),
        ('vv',         'v'),
        ('b',          (Choseong(B),)),
        ('C',          (Choseong(C),)),
        ('d',          (Choseong(D),)),
        ('f',          (Choseong(P),)),
        ('g',          (Choseong(G),)),
        ('j{@}',       (Choseong(H),)),
        ('j',          None),
        ('^k',         (Choseong(K),)),
        ('k{@lmnrX}',  (Choseong(K),)),
        ('{@}k',       (Jongseong(G),)),
        ('k',          (Choseong(K),)),
        ('^l',         (Choseong(L),)),
        ('l{@}',       (Jongseong(L), Choseong(L))),
        ('l',          (Jongseong(L),)),
        ('m{@}',       (Choseong(M),)),
        ('m',          (Jongseong(M),)),
        ('n{@Y}',      (Choseong(N),)),
        ('n',          (Jongseong(N),)),
        ('N',          (Jongseong(NG),)),
        ('p{@lmnrX}',  (Choseong(P),)),
        ('{@}p',       (Jongseong(B),)),
        ('p',          (Choseong(P),)),
        ('r',          (Choseong(L),)),
        ('s',          (Choseong(S),)),
        ('t',          (Choseong(T),)),
        ('v',          (Choseong(B),)),
        ('Ya',         (Jungseong(YA),)),
        ('Ye',         (Jungseong(YE),)),
        ('Yi',         (Jungseong(I),)),
        ('Yo',         (Jungseong(YO),)),
        ('Yu',         (Jungseong(YU),)),
        ('Wa',         (Jungseong(WA),)),
        ('We',         (Jungseong(WE),)),
        ('Wi',         (Jungseong(WI),)),
        ('a',          (Jungseong(A),)),
        ('e',          (Jungseong(E),)),
        ('i',          (Jungseong(I),)),
        ('o',          (Jungseong(O),)),
        ('u',          (Jungseong(U),)),
    )

    def normalize(self, string):
        def normalize_only_unsafe(string):
            map = {u'Ñ': u'ñ', u'Ǘ': u'ü', u'Ü': u'ü'}
            safe = map.keys() + map.values()
            for c in string:
                if c not in safe:
                    yield normalize_roman(c)
                else:
                    yield safe[safe.index(c) / 2 * 2]
        return ''.join(normalize_only_unsafe(string))


es = Spanish


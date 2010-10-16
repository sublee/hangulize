# -*- coding: utf-8 -*-
from hangulize import *


class Hungarian(Language):
    """For transcribing Hungarian."""

    vowels = 'a', 'A', 'e', 'i', 'o', 'O', 'u', 'U'
    notation = Notation(
        (u'á',            'A'),
        (u'ö',            'O'),
        (u'ü',            'U'),
        ('cc',            'c'),
        ('cs',            'C'),
        ('ch',            'C'), # archaic spelling
        ('cz',            'c'), # archaic spelling
        ('dd',            'd'),
        ('dzs',           'D'),
        ('gg',            'g'),
        ('gy',            'D'),
        ('ny{@}',         'nJ'),
        ('ny',            'ni'),
        ('xx',            'x'),
        ('x',             'kS'),
        ('ss',            's'),
        ('sz',            'S'),
        ('tt',            't'),
        ('th',            't'), # archaic spelling
        ('ts',            'C'), # archaic spelling
        ('ty',            'C'),
        ('zz',            'z'),
        ('zs',            'Z'),
        ('ll',            'l'),
        ('ly{@}',         'J'),
        ('ly',            'i'),
        ('j{@}',          'J'),
        ('j',             'i'),
        ('y{@}',          'J'),
        ('y',             'i'),
        ('^Je',           'Ye'),
        ('{@sS}Je',       'Ye'),
        ('Je',            'e'),
        ('Y',             'J'),
        ('aa',            'a'),
        ('bb',            'b'),
        ('ee',            'e'),
        ('eO',            'O'), # archaic spelling
        ('ew',            'O'), # archaic spelling
        ('ff',            'f'),
        ('hh',            'h'),
        ('ii',            'i'),
        ('kk',            'k'),
        ('{@}mm{@}',      (Jongseong(M), Choseong(M))),
        ('mm',            'm'),
        ('{@}nn{@J}',     (Jongseong(N), Choseong(N))),
        ('nn',            'n'),
        ('oo',            'o'),
        ('OO',            'O'),
        ('pp',            'p'),
        ('rr',            'r'),
        ('s{@}',          'SJ'),
        ('s$',            'Si'),
        ('s',             'SJu'),
        ('uu',            'u'),
        ('UU',            'U'),
        ('w',             'v'),
        ('vv',            'v'),
        ('^k',            (Choseong(K),)),
        ('{@}k{cCfhpSt}', (Jongseong(G),)),
        ('^p',            (Choseong(P),)),
        ('{@}p{cCfhkSt}', (Jongseong(B),)),
        ('k',             (Choseong(K),)),
        ('p',             (Choseong(P),)),
        ('b',             (Choseong(B),)),
        ('c',             (Choseong(C),)),
        ('C{@}',          (Choseong(C),)),
        ('C',             (Choseong(C), Jungseong(I))),
        ('d',             (Choseong(D),)),
        ('D{@}',          (Choseong(J),)),
        ('D',             (Choseong(J), Jungseong(I))),
        ('f',             (Choseong(P),)),
        ('g',             (Choseong(G),)),
        ('h',             (Choseong(H),)),
        ('^l',            (Choseong(L),)),
        ('l{@}',          (Jongseong(L), Choseong(L))),
        ('l',             (Jongseong(L),)),
        ('^m',            (Choseong(M),)),
        ('m{@}',          (Choseong(M),)),
        ('m',             (Jongseong(M),)),
        ('^n',            (Choseong(N),)),
        ('n{@J}',         (Choseong(N),)),
        ('n',             (Jongseong(N),)),
        ('r',             (Choseong(L),)),
        ('S',             (Choseong(S),)),
        ('t',             (Choseong(T),)),
        ('v',             (Choseong(B),)),
        ('z',             (Choseong(J),)),
        ('Z{@}',          (Choseong(J),)),
        ('Z',             (Choseong(J), Jungseong(U))),
        ('Ja',            (Jungseong(YEO),)),
        ('JA',            (Jungseong(YA),)),
        ('Je',            (Jungseong(YE),)),
        ('Ji',            (Jungseong(I),)),
        ('Jo',            (Jungseong(YO),)),
        ('JO',            (Jungseong(OE),)),
        ('Ju',            (Jungseong(YU),)),
        ('JU',            (Jungseong(WI),)),
        ('a',             (Jungseong(EO),)),
        ('A',             (Jungseong(A),)),
        ('e',             (Jungseong(E),)),
        ('i',             (Jungseong(I),)),
        ('o',             (Jungseong(O),)),
        ('O',             (Jungseong(OE),)),
        ('u',             (Jungseong(U),)),
        ('U',             (Jungseong(WI),)),
    )

    def normalize(self, string):
        def normalize_only_unsafe(string):
            map = {u'Á': u'á',
                   u'Ö': u'ö',
                   u'Ő': u'ö',
                   u'ő': u'ö',
                   u'Ü': u'ü',
                   u'Ű': u'ü',
                   u'ű': u'ü'}
            safe = map.keys() + map.values()
            for c in string:
                if c not in safe:
                    yield normalize_roman(c)
                elif c in map:
                    yield map[c]
                else:
                    yield c
        return ''.join(normalize_only_unsafe(string))


hu = Hungarian


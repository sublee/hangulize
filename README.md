Hangulize - 외래어 자동 한글 변환 모듈
======================================

[![Build Status](https://secure.travis-ci.org/sublee/hangulize.png?branch=master)](http://travis-ci.org/sublee/hangulize)

> 외국어의 한글 표기 체계가 제대로 서려면 일반인이 외국어를 한글로
> 표기하고 싶을 때 바로바로 쉽게 용례를 찾을 수 있어야 한다. 정기적으로
> 회의를 열어 용례를 정하는 것으로는 한계가 있다. 외래어 표기 심의 방식이
> 자동화되어 한글로 표기하고 싶은 외국어를 입력하자마자 한글 표기가
> 나와야 한다. 이미 용례가 정해진 것은 그것을 따르고 용례에 없는 것이라도
> 각 언어의 표기 규칙에 따라 권장 표기를 표시해야 한다. 프로그래머들과
> 언어학자들이 손잡고 연구한다면 이게 공상으로만 그치지 않을 것이다.
>
> by Brian Jongseong Park (<http://iceager.egloos.com/2610028>)

Hangulize는 외래어를 한글로 자동 변환해주는 Python 모듈입니다.

    >>> from hangulize import hangulize
    >>> print hangulize('Guido van Rossum', 'nld')
    히도 판로쉼

변환 가능한 언어들
------------------

1. 라틴어(`lat`)
1. 독일어(`deu`)
1. 러시아어(`rus`)
1. 현대 그리스어(`ell`)
1. 고대 그리스어(`grc`)
1. 이탈리아어(`ita`)
1. 스페인어(`spa`)
1. 일본어(`jpn`)
1. 폴란드어(`pol`)
1. 체코어(`ces`)
1. 세르보크로아트어(`hbs`)
1. 루마니아어(`ron`)
1. 헝가리어(`hun`)
1. 베트남어(`vie`)
1. 스웨덴어(`swe`)
1. 네덜란드어(`nld`)
1. 포르투갈어(`por`)
1. 브라질 포르투갈어(`por.br`)
1. 웨일스어(`cym`)
1. 중세 웨일스어(`wlm`)
1. 불가리아어(`bul`)
1. 조지아어 간략전사(`kat`)
1. 조지아어 정밀전사(`kat.narrow`)
1. 핀란드어(`fin`)
1. 에스토니아어(`est`)
1. 라트비아어(`lav`)
1. 리투아니아어(`lit`)
1. 아이슬란드어(`isl`)
1. 카탈루냐어(`cat`)
1. 슬로바키아어(`slk`)
1. 슬로베니아어(`slv`)
1. 알바니아어(`sqi`)
1. 에스페란토(`epo`)
1. 우크라이나어(`ukr`)
1. 벨라루스어(`bel`)
1. 마케도니아어(`mkd`)
1. 터키어(`tur`)
1. 아제르바이잔어(`aze`)

설치
----

1. pip 이용:

    $ pip install hangulize

1. easy_install 이용:

    $ easy_install hangulize

1. pip로 개발버전 받기:

    $ pip install git+git://github.com/sublee/hangulize.git#egg=hangulize

1. 저장소 내려받아 설치하기:

    $ git clone git://github.com/sublee/hangulize.git
    $ cd hangulize
    $ python setup.py install

사용법
------

`hangulize` 함수를 사용해야합니다. 우선 모듈로부터 함수를 불러옵니다:

    >>> from hangulize import hangulize

`hangulize` 함수는 첫번째 인자로 변환할 단어를, 두번째 인자로 언어코드(ISO
639-3)를 입력받습니다. 이 함수는 표준 외래어표기법을 따른 한글 변환 결과를
반환할 것입니다:

    >>> print hangulize(u"Giro d'Italia", 'ita')
    지로 디탈리아
    >>> print hangulize(u'オオサカ', 'jpn')
    오사카
    >>> print hangulize(u'przyjaciół', 'pol')
    프시야치우
    >>> print hangulize(u'Алексеев', 'rus')
    알렉세예프
    >>> print hangulize(u'კახაბერ', 'kat.narrow')
    까하베르
    >>> print hangulize(u'Ἡρακλῆς', 'grc')
    헤라클레스

테스트
------

국립국어원 사이트에 있는 [외래어 표기법][1]을 토대로 작성한 테스트수트를
작동시킵니다:

    $ python setup.py test
    제1항: gl ... ok
    제2항: gn ... ok
    제3항: sc ... ok
    제4항 ... ok
    ...

이때 `HANGULIZE_TEST_LANG` 환경 변수를 설정할 경우, 해당 언어의 테스트만
할 수도 있습니다:

    $ HANGULIZE_TEST_LANG=jpn python setup.py test
    ...

또는 REPL 모드를 사용할 수 있습니다. REPL 모드에서는 단어의 변화 과정이
표준출력으로 나타납니다:

    $ python setup.py repl
    Select Locale: pol
    ==> łóżko
    -> 'łóżko'
    -> 'Xuóżko'
    -> 'Xuużko'
    -> 'Xuuszko'
    -> 'XuusJuko'
    -> 'XusJuko'
    -> 'usJuko'
    -> 'usJu o'
    -> 'u Ju o'
    -> 'u   o'
    -> 'u    '
    -> '     '
    우슈코

커뮤니티
--------

[메일링리스트][]를 운영하고 있습니다. Hangulize 개발자들이 주고받는 이야기를
보고싶거나 Hangulize에 제안할 좋은 아이디어가 있다면 이쪽으로 오시기 바랍니다.

만든이
------

- Brian Jongseong Park <<iceager@gmail.com>> - Linguistic Consultant
- Heungsub Lee <<sub@subl.ee>> - Developer

라이선스
--------

Hangulize에는 BSD 라이선스가 적용되어있습니다. 따라서 소스코드를 사용할
경우 라이선스 내용을 준수해주십시오. 라이선스 전문은 `LICENSE` 파일에서
확인하실 수 있습니다.

 [1]: http://www.korean.go.kr/front/page/pageView.do?page_id=P000105&mn_id=97

링크
----

- [웹사이트][]
- [메일링리스트][]
- [iOS 애플리케이션][] by Jeong YunWon
- [꽁치][](Hangulize IRC 봇) by Adrian Jung
- [읽어봐!][](또 다른 외래서 전사 프로그램) by 마늘아빠

 [웹사이트]: http://www.hangulize.org/
 [메일링리스트]: http://groups.google.com/group/hangulize
 [iOS 애플리케이션]: https://github.com/youknowone/hangulize-ios
 [꽁치]: https://github.com/kkung/kkongchi
 [읽어봐!]: http://socoop.net/ilgoba

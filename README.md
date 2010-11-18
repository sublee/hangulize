Hangulize - 외래어 자동 한글 변환 모듈
======================================

Hangulize는 자동으로 외래어를 한글로 변환해주는 Python 모듈입니다. 만든이 중
한 명인 Brian이 자신의 블로그에 작성한 다음 문단으로부터 프로젝트가
시작되었습니다.

> 외국어의 한글 표기 체계가 제대로 서려면 일반인이 외국어를 한글로
> 표기하고 싶을 때 바로바로 쉽게 용례를 찾을 수 있어야 한다. 정기적으로
> 회의를 열어 용례를 정하는 것으로는 한계가 있다. 외래어 표기 심의 방식이
> 자동화되어 한글로 표기하고 싶은 외국어를 입력하자마자 한글 표기가
> 나와야 한다. 이미 용례가 정해진 것은 그것을 따르고 용례에 없는 것이라도
> 각 언어의 표기 규칙에 따라 권장 표기를 표시해야 한다. 프로그래머들과
> 언어학자들이 손잡고 연구한다면 이게 공상으로만 그치지 않을 것이다.
>
> (전문: <http://iceager.egloos.com/2610028>)

Hangulize는 위 아이디어를 실현하는 첫번째 프로젝트입니다.

변환 가능한 언어들
------------------

- 이탈리아어(`it`)
- 스페인어(`es`)
- 일본어(`ja`)
- 폴란드어(`pl`)
- 체코어(`cs`)
- 세르보크로아트어(`sh`)
- 루마니아어(`ro`)
- 헝가리어(`hu`)
- 베트남어(`vi`)
- 스웨덴어(`sv`)
- 네덜란드어(`nl`)
- 독일어(`de`)
- 포르투갈어(`pt`)
- 브라질 포르투갈어(`pt-BR`)
- 러시아어(`ru`)
- 웨일스어(`cy`)
- 중세 웨일스어(`wlm`)
- 불가리아어(`bg`)

설치
----

1. pip 이용:

       $ pip install hangulize

1. easy_install 이용:

       $ easy_install hangulize

1. 저장소 내려받기:

       $ git clone git://github.com/sublee/hangulize.git
       $ cd hangulize
       $ python setup.py install

사용법
------

`hangulize` 함수를 사용해야합니다. 우선 모듈로부터 함수를 불러옵니다:

    >>> from hangulize import hangulize

`hangulize` 함수는 첫번째 인자로 변환할 단어를, 두번째 인자로 로캘 코드를
입력받습니다. 이 함수는 표준 외래어표기법을 따른 한글 변환 결과를 반환할
것입니다:

    >>> print hangulize(u"Giro d'Italia", 'it')
    지로 디탈리아
    >>> print hangulize(u'Gamiño', 'es')
    가미뇨
    >>> print hangulize(u'オオサカ', 'ja')
    오사카
    >>> print hangulize(u'przyjaciół', 'pl')
    프시야치우

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

또는 REPL 모드를 사용할 수 있습니다. REPL 모드에서는 단어의 변화 과정이
표준출력으로 나타납니다:

    $ python setup.py repl
    Select Locale: pl
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

Hangulize는 [메일링리스트][]와 IRC
채널(irc://irc.ozinger.org/hangulize)을 운영하고 있습니다. Hangulize 개발자들이
주고받는 이야기를 보고싶거나 Hangulize에 제안할 좋은 아이디어가 있다면 이쪽으로
와주시기 바랍니다.

만든이
------

- Brian Jongseong Park <<iceager@gmail.com>> - Linguistic Consultant
- Heungsub Lee <<heung@sublee.kr>> - Developer

라이선스
--------

Hangulize에는 BSD 라이선스가 적용되어있습니다. 따라서 소스코드를 사용할
경우 라이선스 내용을 준수해주십시오. 라이선스 전문은 `LICENSE` 파일에
쓰여있습니다.

 [1]: http://korean.go.kr/09_new/dic/rule/rule_foreign_index.jsp

링크
----

- [웹사이트][]
- [메일링리스트][]
- [꽁치][] - Hangulize IRC 봇

 [웹사이트]: http://www.hangulize.org/
 [메일링리스트]: http://groups.google.com/group/hangulize
 [꽁치]: https://github.com/kkung/kkongchi

# -*- coding: utf-8 -*-
"""
Hangulize
~~~~~~~~~

Hangulize transcribes a loanword to Hangul(the Korean alphabet).

>>> print hangulize(u"Giro d'Italia", 'it')
지로 디탈리아
>>> print hangulize(u'Gamiño', 'es')
가미뇨
>>> print hangulize(u'オオサカ', 'ja')
오사카
>>> print hangulize(u'przyjaciół', 'pl')
프시야치우

Links
`````

* `GitHub repository <http://github.com/sublee/hangulize>`_
* `development version
  <http://github.com/sublee/hangulize/zipball/master#egg=hangulize-dev>`_

"""
from setuptools import setup
from cmds import cmdclass


def run_tests():
    from tests import suite
    return suite()


setup(
    name='hangulize',
    version='0.0.1',
    license='BSD',
    author='Lee Heung-sub',
    author_email='heung@sublee.kr',
    description='Korean Alphabet Transcription',
    long_description=__doc__,
    zip_safe=False,
    test_suite="__main__.run_tests",
    platforms='any',
    packages=['hangulize'],
    package_data={'hangulize': ['langs/*']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Korean',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic'
    ],
    cmdclass=cmdclass
)


# -*- coding: utf-8 -*-
"""
Hangulize
~~~~~~~~~

Hangulize transcribes a loanword to Hangul(the Korean alphabet).

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

Links
`````

* `Try Online <http://www.hangulize.org/>`_
* `GitHub repository <http://github.com/sublee/hangulize>`_
* `development version
  <http://github.com/sublee/hangulize/zipball/master#egg=hangulize-dev>`_

"""
import re
from setuptools import setup, find_packages

from cmds import cmdclass


# detect the current version.
with open('hangulize/__init__.py') as f:
    version = re.search(r'__version__\s*=\s*\'(.+?)\'', f.read()).group(1)
assert version


setup(
    name='hangulize',
    version=version,
    license='BSD',
    author='Heungsub',
    author_email=re.sub('((sub).)(.*)', r'\2@\1.\3', 'sublee'),
    url='http://hangulize.org/',
    description='Korean Alphabet Transcription',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    packages=find_packages(),
    package_dir={'hangulize': 'hangulize'},
    py_modules=['cmds'],
    test_suite='tests.suite_for_setup',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Korean',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic'
    ],
    cmdclass=cmdclass()
)

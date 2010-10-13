# -*- coding: utf-8 -*-
"""
Hangulize
~~~~~~~~~

Hangulize transcribes a loanword to Hangul(the Korean alphabet).

>>> print hangulize(u'Italia', 'it')
이탈리아
>>> print hangulize(u"Giro d'Italia", 'it')
지로 디탈리아
>>> print hangulize(u'オオサカ', 'ja')
오사카

Links
`````

* `GitHub repository <http://github.com/sublee/hangulize>`_
* `development version
  <http://github.com/sublee/hangulize/zipball/master#egg=hangulize-dev>`_

"""
from setuptools import setup
from distutils.cmd import Command


class repl(Command):
    """Read-eval-print loop for Hangulize

        $ python setup.py repl
        Select Locale: it
        ==> gloria
        -> 'gloria'
        -> ' loria'
        -> '  oria'
        -> '  o ia'
        -> '  o i '
        -> '  o   '
        -> '      '
        글로리아
    """

    user_options = [('locale=', 'l', 'the locale')]

    def initialize_options(self):
        self.locale = None

    def finalize_options(self):
        pass

    def run(self):
        import logging
        from hangulize import hangulize
        logger = logging.getLogger('Hangulize REPL')
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler())
        def _repl():
            locale = self.locale or raw_input('Select Locale: ')
            while True:
                string = raw_input('==> ')
                if not string:
                    break
                yield hangulize(string.decode('utf-8'),
                                locale, logger=logger).encode('utf-8')
        for hangul in _repl():
            print hangul


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
    cmdclass={'repl': repl}
)


# -*- coding: utf-8 -*-
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
        import sys
        import logging
        from hangulize import hangulize
        logger = logging.getLogger('Hangulize REPL')
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler())
        encoding = sys.stdout.encoding
        def _repl():
            locale = self.locale or raw_input('Select Locale: ')
            while True:
                string = raw_input('==> ')
                if not string:
                    break
                yield hangulize(string.decode(encoding),
                                locale, logger=logger).encode(encoding)
        for hangul in _repl():
            print hangul


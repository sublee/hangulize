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

    user_options = [('code=', 'l', 'the language code(ISO 639-3)')]

    def initialize_options(self):
        self.code = None

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import logging
        from hangulize import hangulize, get_lang, LanguageError
        logger = logging.getLogger('Hangulize REPL')
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler())
        encoding = sys.stdout.encoding
        def _repl():
            while True:
                code = self.code or raw_input(color('Lang: ', 'magenta'))
                try:
                    lang = get_lang(code, logger=logger)
                    logger.info('** ' + color(type(lang).__name__, 'green') + \
                                ' is selected')
                    break
                except LanguageError as e:
                    logger.error(color(e, 'red'))
            while True:
                string = raw_input(color('==> ', 'cyan'))
                if not string:
                    logger.info('** ' + color('end', 'green'))
                    break
                yield hangulize(string.decode(encoding), lang=lang)
        for hangul in _repl():
            logger.info(color(hangul, 'yellow').encode(encoding))


def color(msg, color):
    colors = dict(BLACK=30, RED=31, GREEN=32, YELLOW=33, BLUE=34,
                  MAGENTA=35, CYAN=36, WHITE=37)
    code = colors[color.upper()]
    return '\033[1;%dm%s\033[0m' % (code, msg)

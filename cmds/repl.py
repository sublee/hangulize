# -*- coding: utf-8 -*-
from distutils.cmd import Command
import re
import logging


class REPLHandler(logging.StreamHandler):

    color_map = {'hangulize': 'cyan', 'rewrite': 'green', 'remove': 'red'}

    def handle(self, record):
        msg = record.msg
        # keywords
        maxlen = max([len(x) for x in self.color_map.keys()])
        def deco(color_name):
            def replace(m):
                pad = ' ' * (maxlen - len(m.group(1)))
                return color(m.group(1), color_name) + pad
            return replace
        for keyword, color_name in self.color_map.items():
            msg = re.sub(r'(?<=\t)(%s)' % keyword, deco(color_name), msg)
        # result
        msg = re.sub(r'(?<=^\=\>)(.*)$', color(r'\1', 'yellow'), msg)
        # step
        msg = re.sub(r'^(>>|\.\.)', color(r'\1', 'blue'), msg)
        msg = re.sub(r'^(=>)', color(r'\1', 'magenta'), msg)
        # arrow
        msg = re.sub(r'(->)(?= [^ ]+$)', color(r'\1', 'black'), msg)
        record.msg = msg
        return logging.StreamHandler.handle(self, record)


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
        from hangulize import hangulize, get_lang, LanguageError
        logger = logging.getLogger('Hangulize REPL')
        logger.setLevel(logging.INFO)
        logger.addHandler(REPLHandler())
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
            pass


def color(msg, color):
    colors = dict(BLACK=30, RED=31, GREEN=32, YELLOW=33, BLUE=34,
                  MAGENTA=35, CYAN=36, WHITE=37)
    code = colors[color.upper()]
    return '\033[1;%dm%s\033[0m' % (code, msg)

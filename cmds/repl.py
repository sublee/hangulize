# -*- coding: utf-8 -*-
import re
import logging
from distutils.cmd import Command
from cmds.helper import color
from hangulize import hangulize, get_lang, DONE, SPECIAL, BLANK, ZWSP


class REPLHandler(logging.StreamHandler):

    color_map = {'hangulize': 'cyan', 'rewrite': 'green', 'remove': 'red'}

    @staticmethod
    def readably(string):
        string = string.replace(DONE, '.')
        string = string.replace(SPECIAL, '#')
        string = re.sub('^' + BLANK + '|' + BLANK + '$', '', string)
        string = re.sub(ZWSP, '\r', string)
        string = re.sub(BLANK, ' ', string)
        string = re.sub('\r', ZWSP, string)
        return string

    def handle(self, record):
        msg = self.readably(record.msg)
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

    user_options = [('lang=', 'l', 'the language code(ISO 639-3)')]

    def initialize_options(self):
        self.lang = None

    def finalize_options(self):
        pass

    def run(self):
        import sys
        logger = make_logger()
        encoding = sys.stdout.encoding
        def _repl():
            while True:
                lang = self.lang or raw_input(color('Lang: ', 'magenta'))
                try:
                    lang = get_lang(lang)
                    logger.info('** ' + color(type(lang).__name__, 'green') + \
                                ' is selected')
                    break
                except Exception, e:
                    logger.error(color(e, 'red'))
                    self.lang = None
            while True:
                string = raw_input(color('==> ', 'cyan'))
                if not string:
                    logger.info('** ' + color('End', 'green'))
                    break
                yield lang.hangulize(string.decode(encoding), logger=logger)
        for hangul in _repl():
            pass


def make_logger(name='Hangulize REPL'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(REPLHandler())
    return logger

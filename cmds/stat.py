from distutils.cmd import Command

from six import print_

import hangulize.langs
from cmds.helper import color


class stat(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        langs = hangulize.langs.get_list()
        examples = []
        for lang in (x.replace('.', '_') for x in langs):
            mod = getattr(__import__('tests.%s' % lang), lang)
            case = [x for x in dir(mod) if x.endswith('TestCase') and \
                                           not x.startswith('Hangulize')][0]
            examples += getattr(mod, case).get_examples().keys()
        print_('Supported languages:', end=' ')
        print_(color(len(langs), 'cyan'))
        print_('Prepared examples:', end=' ')
        print_(color(len(examples), 'cyan'))

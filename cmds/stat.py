from distutils.cmd import Command
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
        print 'Supported languages:',
        print color(len(langs), 'cyan')
        print 'Prepared examples:',
        print color(len(examples), 'cyan')

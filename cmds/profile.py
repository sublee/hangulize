try:
    from cProfile import run as run_profile
except ImportError:
    from profile import run as run_profile
from distutils.cmd import Command


class profile(Command):

    user_options = [('lang=', 'l', 'the language code(ISO 639-3)')]

    def initialize_options(self):
        self.lang = None

    def finalize_options(self):
        pass

    def run(self):
        code = '' \
'''
import unittest
import tests
suite = tests.suite(%r)
unittest.TextTestRunner(verbosity=1).run(suite)
try:
    from guppy import hpy
    print '============= memory usage ============='
    print hpy().heap()
    print '----------------------------------------'
except ImportError:
    pass
''' \
        '' % self.lang
        run_profile(code)

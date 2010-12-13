from distutils.cmd import Command


class test(Command):

    user_options = [('code=', 'l', 'the specified language code(ISO 639-3) '
                                   'for test')]

    def initialize_options(self):
        self.code = None

    def finalize_options(self):
        pass

    def run(self):
        import unittest
        import tests
        suite = tests.suite(self.code)
        unittest.TextTestRunner(verbosity=2).run(suite)

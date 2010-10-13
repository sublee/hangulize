import unittest


class LanguagesTestCase(unittest.TestCase):

    def test_import_all(self):
        from hangulize.langs import *
        assert isinstance(ja, type(unittest))
        assert isinstance(it, type(unittest))
        assert isinstance(es, type(unittest))


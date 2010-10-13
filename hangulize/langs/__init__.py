from os import listdir
from os.path import splitext, dirname

__all__ = [splitext(f)[0] for f in listdir(dirname(__file__)) \
                          if splitext(f)[1] == '.py' and f != '__init__.py']


import re
from .phoneme import Impurity


SPACE = Impurity(' ')
SPACE_PATTERN = re.compile(' ')


class Notation(object):

    def __init__(self, *rule):
        self.rule = list(rule)

    def items(self, lang=None):
        """Yields each notation rules as regex."""
        for pattern, val in self.rule:
            yield self.regexify(pattern, lang), val
        yield SPACE_PATTERN, (SPACE,)

    def regexify(self, pattern, lang=None):
        """Compiles a regular expression from the notation pattern."""
        regex = pattern
        if lang:
            vowels = ''.join([re.escape(v) for v in lang.vowels])
            regex = re.sub('@', vowels, regex)
        regex = re.sub('^{([^}]+?)}', r'(?<=[\1])', regex)
        regex = re.sub('{([^}]+?)}$', r'(?=[\1])', regex)
        return re.compile(regex)


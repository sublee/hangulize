import re


class Notation(object):

    vowels = ()
    rule = []

    def items(self):
        """Yields each notation rules as regex."""
        for pattern, val in self.rule:
            yield self.regexify(pattern), val

    def regexify(self, pattern):
        """Compiles a regular expression from the notation pattern."""
        vowels = ''.join([re.escape(v) for v in self.vowels])
        regex = re.sub('@', vowels, pattern)
        regex = re.sub('^{([^}]+?)}', r'(?<=[\1])', regex)
        regex = re.sub('{([^}]+?)}$', r'(?=[\1])', regex)
        return re.compile(regex)


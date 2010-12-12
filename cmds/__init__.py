from cmds.repl import repl
from cmds.gentest import gen_test
from cmds.test import test


cmdclass = {'test': test, 'repl': repl, 'gen_test': gen_test}

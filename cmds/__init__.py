from cmds.test import test
from cmds.repl import repl
from cmds.gentest import gen_test


cmdclass = dict(test=test, repl=repl, gen_test=gen_test)

import cmds.test
import cmds.repl
import cmds.gentest


cmdclass = dict(test=cmds.test.test,
                repl=cmds.repl.repl,
                gen_test=cmds.gentest.gen_test)

def cmdclass():
    import cmds.test
    import cmds.repl
    import cmds.gentest
    import cmds.stat
    import cmds.profile
    return dict(test=cmds.test.test,
                repl=cmds.repl.repl,
                gen_test=cmds.gentest.gen_test,
                stat=cmds.stat.stat,
                profile=cmds.profile.profile)

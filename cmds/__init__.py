def cmdclass():
    import cmds.repl
    import cmds.gentest
    import cmds.stat
    import cmds.profile
    return dict(repl=cmds.repl.repl,
                gen_test=cmds.gentest.gen_test,
                stat=cmds.stat.stat,
                profile=cmds.profile.profile)

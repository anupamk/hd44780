def debug_print(do_dump, fmt_arg, *fmt_argv):
    if do_dump:
        dbg_str = str(fmt_arg) % fmt_argv
        print dbg_str
    return


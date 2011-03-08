# return the char equivalent of a 5bit array
def five_bits_to_char(b4, b3, b2, b1, b0):
    return ((b4 << 4) |
            (b3 << 3) |
            (b2 << 2) |
            (b1 << 1) |
            (b0))

# this function is called to convert an 8bit array to an equivalen
# char. index-0 is MSB, index-7 is LSB
def eight_bits_to_char(bit_array):
    return ((bit_array[0] << 7) |
            (bit_array[1] << 6) |
            (bit_array[2] << 5) |
            (bit_array[3] << 4) |
            (bit_array[4] << 3) |
            (bit_array[5] << 2) |
            (bit_array[6] << 1) |
            (bit_array[7] << 0))

# dump some debug info
def debug_print(do_dump, fmt_arg, *fmt_argv):
    if do_dump:
        dbg_str = str(fmt_arg) % fmt_argv
        print dbg_str
    return


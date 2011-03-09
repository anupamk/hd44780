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


# initialize the lcd matrix. fill it up with spaces...
def initialize_matrix(init_char, mat, dim):
    row, col = dim[0], dim[1]

    for i in range(row):
        mat_row = []
        for j in range(col):
            mat_row.append(init_char)
        mat.append(mat_row)
    return

# print a properly formatted string on the display, returns the new
# cursor-x-y-position, and the number of bytes actually dmumped.
#
# if the string would overflow the display, 
def matrix_printf(lcd_matrix, r, c, fmt_args, *fmt_argv):
    num_bytes = 0
    R, C      = r, c
    
    # args ok ?
    if printf_args_ok(lcd_matrix, r, c, fmt_args):
        return (num_bytes, C, R)

    # display params
    M, mat_cols = (lcd_matrix[0], lcd_matrix[2])

    # message properties
    full_msg  = str(fmt_args) % fmt_argv                 # what we have to show
    spc_avail = get_available_space(lcd_matrix, r, c)  # total space available
    disp_msg  = full_msg[:min(spc_avail, len(full_msg))] # what we can-show

    # write byte-by-byte
    for ch in disp_msg:
        M[R][C] = ch

        C = C + 1
        
        # next row
        if (C >= mat_cols):
            C = 1
            R = R + 1

    return (len(disp_msg), R, C)

# args are ok ?
def printf_args_ok(lcd_matrix, r, c, fmt_args):
    max_rows, max_cols = lcd_matrix[1], lcd_matrix[2]

    # basic usage failure
    if ((fmt_args == None) or
        (r < 0 or r >= max_rows) or
        (c < 0 or c >= max_cols)):
        return True                                      # usage-error

    return False                                         # all-is-well

# returns the total available space in the matrix from the given
# position.  
def get_available_space(lcd_matrix, r, c):
    num_rows, num_cols = lcd_matrix[1], lcd_matrix[2]

    total_space = (num_rows - r - 1) * num_cols + (num_cols - c)
    return total_space

    

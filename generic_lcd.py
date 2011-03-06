# 
# this file provides a generic abstraction to lcd module. it comprises
# the following:
#    - ddram-matrix : emulates the entire lcd-display-matrix
#    - cgram-vector : custom characters are stored here
#    - cursor-xpos  : column position in the ddram-matrix
#    - cursor-ypos  : row position in the ddram-matrix
# 
class generic_lcd(object):
    def __init__(self, ddram_row, ddram_col, cgram_row, cgram_col):
        # dimensions
        self.ddram_rows_ = ddram_row
        self.ddram_cols_ = ddram_col
        self.cgram_rows_ = cgram_row
        self.cgram_cols_ = cgram_col

        # position cursor at top-left corner of the display
        self.c_row_ = 0
        self.c_col_ = 0

        # initialize display
        self.ddram_matrix_ = []
        self.cgram_vector_ = []

        __initialize_matrix__(' ',  self.ddram_matrix_, (self.ddram_rows_, self.ddram_cols_))
        __initialize_matrix__(0x20, self.cgram_vector_, (self.cgram_rows_, self.cgram_cols_))
        
        return

    # puts a properly formatted string at a given position on the
    # display. text 'wraps' around. returns the number of bytes
    # actually dumped.
    def put_string(self, row, col, fmt_str, *fmt_argv):
        r, c = row, col
        
        if (r < 0 or c < 0):
            r = self.c_row_
            c = self.c_col_

        # write to display
        lcd_matrix = (self.ddram_matrix_, self.ddram_rows_, self.ddram_cols_)
        (bytes_written, new_row, new_col) = __do_matrix_printf__(lcd_matrix,
                                                                 r,
                                                                 c,
                                                                 fmt_str,
                                                                 *fmt_argv)

        # update cursor position
        self.__update_xycursor(new_col, new_row)
        
        return bytes_written

    # put a string in the center of a row
    def put_center_string(self, row, display_str):
        center_str = display_str.center(self.ddram_cols_, " ")
        
        return self.put_string(row, 0, "%s", center_str)

    # display a string in the center of the row
    def display_center_string(self, row, display_str):
        bytes_written = self.put_center_string(row, display_str)
        self.flush_row(row)

        return bytes_written

    # display a string
    def display_string(self, row, col, fmt_str, *fmt_argv):
        bytes_written = self.put_string(row, col, fmt_str, fmt_argv)
        self.flush_row(row)

        return bytes_written
        

    # puts the address of a custom shape in cgram on the
    # display. returns the number of bytes actually dumped.
    def put_shape(self, row, col, cgram_row):
        r, c = row, col
        
        if (r < 0 or c < 0):
            r = self.c_row_
            c = self.c_col_
        
        self.ddram_matrix_[r][c] = cgram_row
        self.__update_xycursor(c+1, r)
        return 1

    # copy a custom shape into the cgram_vector
    def cp_shape(self, row, byte_seq):
        shape_sz = len(byte_seq)

        # invalid shape
        if ((shape_sz <= 0) or (shape_sz > self.cgram_rows_)):
            return
        
        self.cgram_vector_[row] = byte_seq
        return

    # initialize the lcd, just the cursor position, and the actual
    # stuff that was displayed. 
    def initialize(self):
        self.c_row_ = 0
        self.c_col_ = 0

        __initialize_matrix__(' ', self.ddram_matrix_, (self.ddram_rows_, self.ddram_cols_))
        return

    # initialize a row
    def init_row(self, row):
        for i in range(self.ddram_cols_):
            self.ddram_matrix_[row][i] = ' '
        return

    # dump the contents of the matrix on the display
    def flush(self):
        self.debug_dump_ddram()
        return

    # dump the contents of a given row
    def flush_row(self, row):
        print "row: %d, value: %s" % (row, self.ddram_matrix_[row])
        return

    # debugging routines

    # dump the contents of the ddram on the console
    def debug_dump_ddram(self):
        print "---DDRAM---"
        for i in range(self.ddram_rows_):
            print "row: %d, value: %s" % (i, self.ddram_matrix_[i])
        return

    # dump the contents of the cgram on the console
    def debug_dump_cgram(self):
        print "---CGRAM---"
        for i in range(self.cgram_rows_):
            print "row: %d, value: %s" % (i, self.cgram_vector_[i])
        return

    # dump everythang
    def debug_dump_all(self):
        print "---MATRIX-STATE---"
        
        # basic stuff
        print "DDRAM      [rows: %d, cols: %d]" % (self.ddram_rows_, self.ddram_cols_)
        print "CGRAM      [rows: %d, cols: %d]" % (self.cgram_rows_, self.cgram_cols_)
        print "CURSOR-POS [ row: %d,  col: %d]" % (self.c_col_, self.c_row_)

        # matrix contents
        self.debug_dump_ddram()
        self.debug_dump_cgram()

        return
    
    # private stuff
    def __update_xycursor(self, newx, newy):
        self.c_row_ = newx
        self.c_col_ = newy

        # next row
        if (self.c_row_ > self.ddram_cols_):
            self.c_row_ = 1
            self.c_col_ = self.c_col_ + 1

        # maybe check invariants too...
        return

# initialize the lcd matrix. fill it up with spaces...
def __initialize_matrix__(init_char, mat, dim):
    row, col = dim[0], dim[1]

    for i in range(row):
        mat_row = []
        for j in range(col):
            mat_row.append(init_char)
        mat.append(mat_row)
    return

# args are ok ?
def __printf_args_bad(lcd_matrix, r, c, fmt_args):
    max_rows, max_cols = lcd_matrix[1], lcd_matrix[2]

    # basic usage failure
    if ((fmt_args == None) or
        (r < 0 or r >= max_rows) or
        (c < 0 or c >= max_cols)):
        return True                                      # usage-error

    return False                                         # all-is-well

# returns the total available space in the matrix from the given
# position.  
def __get_available_space(lcd_matrix, r, c):
    num_rows, num_cols = lcd_matrix[1], lcd_matrix[2]

    total_space = (num_rows - r - 1) * num_cols + (num_cols - c)
    return total_space

# print a properly formatted string on the display, returns the new
# cursor-x-y-position, and the number of bytes actually dmumped.
#
# if the string would overflow the display, 
def __do_matrix_printf__(lcd_matrix, r, c, fmt_args, *fmt_argv):
    num_bytes = 0
    R, C      = r, c
    
    # args ok ?
    if __printf_args_bad(lcd_matrix, r, c, fmt_args):
        return (num_bytes, C, R)

    # display params
    M, mat_cols = (lcd_matrix[0], lcd_matrix[2])

    # message properties
    full_msg  = str(fmt_args) % fmt_argv                 # what we have to show
    spc_avail = __get_available_space(lcd_matrix, r, c)  # total space available
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
    

import utils

# ----------------------------------------------------------------
# this file provides a generic abstraction to lcd module. it comprises
# the following:
#    - ddram-matrix : emulates the entire lcd-display-matrix
#    - cursor-xpos  : column position in the ddram-matrix
#    - cursor-ypos  : row position in the ddram-matrix
# ----------------------------------------------------------------
class generic_lcd(object):
    def __init__(self, ddram_row, ddram_col):
        self.do_init((ddram_row, ddram_col))
        return

    # initialize the lcd
    def do_init(self, lcd_dim):
        self.ddram_matrix_  = []
        self.c_row_         = 0         # cursor-positioned at the top-left
        self.c_col_         = 0         # corner of the display
        self.ddram_rows_    = lcd_dim[0]
        self.ddram_cols_    = lcd_dim[1]

        utils.initialize_matrix(' ', self.ddram_matrix_, (self.ddram_rows_, self.ddram_cols_))

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
        (bytes_written, new_row, new_col) = utils.matrix_printf(lcd_matrix,
                                                                r, c,
                                                                fmt_str, *fmt_argv)
        # update cursor position
        self.update_xycursor(new_col, new_row)
        
        return bytes_written

    # display a string
    def display_string(self, row, col, fmt_str, *fmt_argv):
        bytes_written = self.put_string(row, col, fmt_str, fmt_argv)
        self.flush_row(row)

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

    # puts the address of a custom shape in cgram on the
    # display. returns the number of bytes actually dumped.
    def put_shape(self, row, col, cgram_row):
        r, c = row, col
        
        if (r < 0 or c < 0):
            r = self.c_row_
            c = self.c_col_

        self.ddram_matrix_[r][c] = cgram_row
        self.update_xycursor(c+1, r)
        return 1

    # initialize a row
    def init_row(self, row):
        for i in range(self.ddram_cols_):
            self.ddram_matrix_[row][i] = ' '
        return

    # private stuff
    def update_xycursor(self, newx, newy):
        self.c_row_ = newx
        self.c_col_ = newy

        # next row
        if (self.c_row_ > self.ddram_cols_):
            self.c_row_ = 1
            self.c_col_ = self.c_col_ + 1

        # maybe check invariants too...
        return


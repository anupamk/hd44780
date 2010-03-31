# this function is called to initialize a matrix 'M' with 'R' rows,
# and 'C' columns 
def initialize_matrix(M, R, C):
    for i in range(R):
        mat_row = []
        for j in range(C):
            mat_row.append(0)
        M.append(mat_row)
    return

# a simple class for abstracting a generic lcd display. multiple
# instances can now represent 'pages' of information, which can be
# flushed as and when required. 
class lcd_generic:
    def __init__(self, ddram_rows, ddram_cols, cgram_rows = 5, cgram_cols = 5):
        self.ddram_rows             = ddram_rows
        self.ddram_cols             = ddram_cols
        self.max_displayable_string = ddram_rows * ddram_cols

        # initialize the ddram and cgram matrix
        self.__ddram_matrix = []
        self.__cgram_vector = []

        initialize_matrix(self.__ddram_matrix, ddram_rows, ddram_cols)
        initialize_matrix(self.__cgram_vector, cgram_rows, cgram_cols)

        return

    def write_lcd_matrix(self, R, C, byte):
        self.__ddram_matrix[R][C] = byte

    def read_lcd_matrix(self, R, C):
        return self.__ddram_matrix[R][C]

    def write_cgram_vector(self, R, byte_seq):
        self.__cgram_vector[R] = byte_seq

    def read_cgram_vector(self, R):
        return self.__cgram_vector[R]
    
    # a printf like interface for dumping characters on the
    # ddram-matrix. returns the number of characters actually dumped. 
    #
    # first-row, first-col == (1, 1)
    def str_printf(self, R, C, fmt_args, *fmt_argv):
        str_idx  = 0
        
        # bad arguments.
        if self.__lcd_printf_bad_args(R, C, fmt_args) == True:
            return str_idx

        # what-to-show
        lcd_output = str(fmt_args) % fmt_argv

        # dump the first row
        nc      = self.__safe_str_write(R, C, lcd_output[str_idx:])
        str_idx = nc

        if self.__continue_dumping(str_idx, lcd_output) == False:
            return str_idx
    
        # and the subsequent rows...
        for i in range(R+1, self.ddram_rows+1):
            nc = self.__safe_str_write(i, 1, lcd_output[str_idx:])

            # update
            str_idx  = str_idx + nc
            disp_col = 1

            if self.__continue_dumping(str_idx, lcd_output) == False:
                break

        return str_idx

    # print the contents of the matrix to the terminal
    def print_lcd_matrix(self):
        print "[Rows: %d, Cols = %d]" % (len(self.__ddram_matrix), len(self.__ddram_matrix[0]))
        for i in range(len(self.__ddram_matrix)):
            print "row: %d, value: %s" % (i, self.__ddram_matrix[i])
        return

    # dump matrix contents to lcd-display
    def flush_lcd_matrix(self):
        return

    # load custom shapes
    def flush_cgram_vector(self):
        print self.__cgram_vector                       # just-testing
        return


    # display a given string, returns the number of bytes actually
    # written. just 'write' the string on the lcd-matrix. 
    def __safe_str_write(self, R, C, disp_str):
        num_chars_to_show = min(self.__get_max_displayable_chars_in_row(C),
                                len(disp_str))
        lcd_row_str = disp_str[:num_chars_to_show]
        self.__unsafe_str_write(R - 1, C - 1, lcd_row_str)
        
        return len(lcd_row_str)
    
    # write a string to the matrix. no checks are made for
    # 'correctness' of passed parameters
    def __unsafe_str_write(self, R, C, dump_str):
        for ch in dump_str:
            self.write_lcd_matrix(R, C, ch)
            C = C+1

    # this function returns 'True' if the arguments to lcd-printf are bad,
    # and 'False' otherwise
    def __lcd_printf_bad_args(self, R, C, fmt_args):

        # basic usage failure
        if ((fmt_args == None) or
            (R < 1 or R > self.ddram_rows) or                      
            (C < 1 or C > self.ddram_cols)):
            return True                                         # yes

        # overflowing display limits ?
        blank_cols = (C-1) + (R-1) * self.ddram_cols
        if blank_cols >= self.max_displayable_string:             
            return True                                         # yes

        # all is well...
        return False                                            # nope

    # this function returns the maximum number of displayable-characters
    # in the current-row. both rows and columns start from '1'.
    def __get_max_displayable_chars_in_row(self, col_offset = 1):
        return self.ddram_cols - (col_offset - 1)
    
    # can dumping continue ? call epa...
    def __continue_dumping(self, idx, lcd_output):
        if ((idx >= len(lcd_output)) or
            (idx >= self.max_displayable_string)):
            return False
        
        return True

        

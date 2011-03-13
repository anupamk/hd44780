class matrix_display(object):
    def __init__(self, dimension):
        self.mat  = []
        self.rows = dimension[0]                                # number of rows
        self.cols = dimension[1]                                # and columns in matrix
        self.rpos = 0                                           # cursor row and
        self.cpos = 0                                           # column position

        self.initialize(' ')
        return

    def initialize(self, init_char):
        """
        initialize the display matrix with a given character.
        """
        for i in range(self.rows):
            mat_row = []
            for j in range(self.cols):
                mat_row.append(init_char)
            self.mat.append(mat_row)

        return

    def do_printf(self, location, fmt_args, *fmt_val):
        """
        print stuff at a given location on the matrix. the number of
        bytes that have been written are retured
        """
        num_bytes = 0
        R, C      = location[0], location[1]

        if self.printf_args_not_ok(location, fmt_args):
            return num_bytes

        # message properties
        full_msg  = str(fmt_args) % fmt_val                     # what we have to show
        spc_avail = self.get_avail_space(location)              # total space available
        disp_msg  = full_msg[:min(spc_avail, len(full_msg))]    # what we can-show

        for ch in disp_msg:
            self.mat[R][C] = ch
            C = C+1

            # goto next row
            if (C >= self.cols):
                C = 1
                R = R+1

        return (len(disp_msg), R, C)

    def update_cursor_pos(self, new_col, new_row):
        """
        this function is called to update the cursor row and column
        position.
        """
        self.cpos = new_col
        self.rpos = new_row

        # next-row
        if (self.cpos > self.cols):
            self.cpos = 1
            self.rpos = self.rpos + 1

        return

    def printf_args_not_ok(self, location, fmt_args):
        """
        return 'True' if printf arguments are not ok. 'False'
        otherwise.
        """
        r, c = location[0], location[1]
        
        if ((fmt_args == None) or
            (r < 0 or r >= self.rows) or
            (c < 0 or c >= self.cols)):
            return True                                         # usage-error

        return False                                            # all-is-well

    def get_avail_space(self, location):
        """
        returns the total space available from the given location
        (row, col).
        """
        r, c = location[0], location[1]
        total_space = (self.rows - r - 1) * self.cols + (self.cols - c)

        return total_space

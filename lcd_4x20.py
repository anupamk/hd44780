import hd44780_driver as lcd_drv
import generic_lcd    as lcd

# stuff specific to a 4x20 HD44780 compatible display

# lcd dimensions
LCD_NUM_ROWS                   = 4
LCD_NUM_COLS                   = 20
LCD_CGRAM_MAX_SHAPES           = 8
LCD_CGRAM_MAX_BYTES_PER_SHAPE  = 5        # max-bytes-per-custom-shape

# store start (row, col) ddram-address. other columns, are just a
# linear offset away from start
LCD_DDRAM_ADDRESS_TABLE = [
    [1, 0x00],                  
    [2, 0x40],
    [3, 0x14],
    [4, 0x54]
]

# 
# some notes about custom-characters:
#    1. all pre-defined characters are available in the CGROM
#    2. a ram area, called CGRAM, of 64 bytes is available for custom
#       characters. since each custom-character consumes 8 bytes,
#       there are 8 such characters that can be defined at a time.
#    3. CGRAM address starts from 0x40. Thus, we have the following
#       custom-char-num -> cgram-start-address map:
#           -- custom-char-0 : 0x40
#           -- custom-char-1 : 0x48
#           -- custom-char-2 : 0x50
#           -- custom-char-3 : 0x58
#       etc.
#    4. Displaying custom characters is pretty straightforward. We
#       just write to the DDRAM the ADDRESS of CGRAM location as
#       defined in (3) above.
#
#       Which basically brings an un-intended consequence to the whole
#       thing. If a CGRAM address is updated with a new shape, then
#       the older entries referring to it are also updated...
LCD_CUSTOMCHAR_ADDRESS_MAP = [
    [1, 0x40],
    [2, 0x48],
    [3, 0x50],
    [4, 0x58],
    [5, 0x60],
    [6, 0x68],
    [7, 0x70],
    [8, 0x78]
]

class lcd_4x20(lcd.generic_lcd):
    def __init__(self):
        super(lcd_4x20, self).__init__(LCD_NUM_ROWS, LCD_NUM_COLS,
                                       LCD_CGRAM_MAX_SHAPES,
                                       LCD_CGRAM_MAX_BYTES_PER_SHAPE)
        self.initialize()
        return

    def reset(self):
        lcd_drv.reset()
        return

    def initialize(self):
        super(lcd_4x20, self).initialize()
        lcd_drv.initialize()

        # extra stuff for us...
        lcd_drv.exec_named_cmdseq(['DISPLAY_ON_CURSOR_ON_BLINK_OFF',
                                   'DISPLAY_ON_CURSOR_OFF'])

        return

    # flush entire matrix. a matrix is a bunch of rows...
    def flush(self):
        for row in range(self.ddram_rows_):
            self.flush_row(row)
        return

    # flush a given character in the matrix
    def flush_row(self, row):
        self.__position_cursor_at_row(row)
        row_val = self.ddram_matrix_[row]

        # dump all the values in current row
        for ch in row_val:
            if ((ch >= 0) and (ch < self.cgram_rows_)):
                # dump a custom character
                lcd_drv.display_custom_char(ch)
            else:
                lcd_drv.write_char_data(ch)
        
        return

    # load cgram into the display
    def load_shapes(self):
        for row in range(self.cgram_rows_):
            cgram_addr   = LCD_CUSTOMCHAR_ADDRESS_MAP[row][1]
            custom_shape = self.cgram_vector_[row]
            lcd_drv.create_custom_charset(cgram_addr, custom_shape)
            
        return

    # private functions
    def __position_cursor_at_row(self, row):
        row_addr = LCD_DDRAM_ADDRESS_TABLE[row][1]
        lcd_drv.position_cursor(row_addr)
        return
    
    
    

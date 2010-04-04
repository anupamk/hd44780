import hd44780_driver as lcd_drv
import lcd_generic    as lcd

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

class lcd_4x20(lcd.lcd_generic):
    def __init__(self):
        super(lcd_4x20, self).__init__(LCD_NUM_ROWS, LCD_NUM_COLS, LCD_CGRAM_MAX_SHAPES, LCD_CGRAM_MAX_BYTES_PER_SHAPE)
        self.initialize()
        return

    def reset(self):
        lcd_drv.reset()
        return

    def initialize(self):
        lcd_drv.initialize()
        return

    # flush the contents of the matrix to the display
    def flush(self):
        for row in range(self.ddram_rows):
            rowcol_addr = LCD_DDRAM_ADDRESS_TABLE[row][1] + 0
            row_val     = self.read_lcd_row(row)

            lcd_drv.position_cursor(rowcol_addr)
            self.__flush_lcd_row(row_val)
        return

    # load cgram into the display
    def load_shapes(self):
        lcd_drv.exec_named_cmdseq(['DISPLAY_ON_CURSOR_ON_BLINK_OFF',
                                   'DISPLAY_ON_CURSOR_OFF'])
        
        for row in range(self.cgram_rows):
            cgram_addr   = LCD_CUSTOMCHAR_ADDRESS_MAP[row][1]
            custom_shape = self.read_cgram_vector(row)
            lcd_drv.create_custom_charset(cgram_addr, custom_shape)
            
        return

    # private functions
    def __flush_lcd_row(self, col_val):
        for c in range(self.ddram_cols):
            val = col_val[c]
            if (val == 0):
                val = ' '
                
            self.__flush_lcd_rowcol_val(val)

    # write a row+col value. if the value cannot be written as
    # char-data, it is treated as a cgram address...
    def __flush_lcd_rowcol_val(self, val):
        try:
            lcd_drv.write_char_data(val)
        except TypeError:
            lcd_drv.display_custom_char(val)

        return
    
    

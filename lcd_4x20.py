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

# return ddram address for a given (row, col)
def lcd_get_ddram_address(row, col):
    return LCD_DDRAM_ADDRESS_TABLE[row - 1][1] + (col - 1)

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
#       just write to the DDRAM the contents of a custom-char-location
#       as defined in (3) above.
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


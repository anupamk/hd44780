# lcd-wide control related imports
from hd44780_driver import reset_lcd as reset
from hd44780_driver import initialize_lcd as initialize

# display related imports
from hd44780_driver import write_string_at
from hd44780_driver import write_custom_character_at

# lcd dimensions
LCD_NUM_ROWS               = 4
LCD_NUM_COLS               = 20
LCD_MAX_DISPLAYABLE_STRING = LCD_NUM_COLS * LCD_NUM_ROWS

# printf like interface for displaying stuff on to the
# lcd. custom-characters are not supported...
def printf(row, col, wrap_ok = True, fmt_args = None, *fmt_argv):
    # basic checks first
    if ((fmt_args == None) or
        (row < 1 or row > LCD_NUM_ROWS) or                      
        (col < 1 or col > LCD_NUM_COLS)):
        return

    # can we even fit the string in the available space ?
    blank_cols = col + (row-1) * LCD_NUM_COLS
    if blank_cols >= LCD_MAX_DISPLAYABLE_STRING:             
        return                                       # nope
    
    # all-that-we-can-show VS what-we-actually-can-show
    temp_lcd_output = str(fmt_args) % fmt_argv
    lcd_output      = temp_lcd_output[:(LCD_MAX_DISPLAYABLE_STRING - blank_cols + 1)]
    
    # start dumping strings...
    write_string_at(row, col, lcd_output[:LCD_NUM_COLS - col + 1])

    # truncated dump
    if wrap_ok == False: return

    # wrap the whole thing around...
    i = row + 1
    j = LCD_NUM_COLS - col
    while i <= LCD_NUM_ROWS:
        write_string_at(i, 1, lcd_output[j:LCD_NUM_COLS + 1])
        
        i = i + 1
        j = j + LCD_NUM_COLS


# lcd-wide control related imports
import hd44780_driver as lcd_driver
import hd44780_custom_chars as lcd_cc

# lcd dimensions
LCD_NUM_ROWS               = 4
LCD_NUM_COLS               = 20
LCD_MAX_DISPLAYABLE_STRING = LCD_NUM_COLS * LCD_NUM_ROWS

# this function returns the maximum number of displayable-characters
# in the current-row. both rows and columns start from '1'.
def get_max_displayable_chars_in_row(col_offset = 1):
    max_chars = LCD_NUM_COLS

    return max_chars - (col_offset - 1)

# display a given string, returns the number of bytes actually written
def display_string(row, col, disp_str):
    num_chars_to_show = min(get_max_displayable_chars_in_row(col), len(disp_str))
    lcd_row_str = disp_str[:num_chars_to_show]

    lcd_driver.write_string_at(row, col, lcd_row_str)

    return len(lcd_row_str)

# this function returns 'True' if the arguments to lcd-printf are bad,
# and 'False' otherwise
def lcd_printf_bad_args(row, col, fmt_args):
    if ((fmt_args == None) or
        (row < 1 or row > LCD_NUM_ROWS) or                      
        (col < 1 or col > LCD_NUM_COLS)):
        return True

    # overflowing display limits ?
    blank_cols = (col-1) + (row-1) * LCD_NUM_COLS
    if blank_cols >= LCD_MAX_DISPLAYABLE_STRING:             
        return True                                             # yes

    return False

# can dumping continue ? call epa...
def continue_dumping(idx, lcd_output):
    if ((idx >= len(lcd_output)) or
        (idx >= LCD_MAX_DISPLAYABLE_STRING)):
        return False

    return True

# 
# this function implements a 'printf' like interface for displaying
# stuff on the lcd. it returns the number of characters actually
# dumped.
#
# first-row, first-col is defined as (1,1)
def lcd_printf(row, col, fmt_args, *fmt_argv):
    str_idx  = 0
    
    # bad arguments.
    if lcd_printf_bad_args(row, col, fmt_args) == True:
        return str_idx

    lcd_output = str(fmt_args) % fmt_argv               # what-to-show

    # dump the first row
    nc      = display_string(row, col, lcd_output[str_idx:])
    str_idx = nc

    if continue_dumping(str_idx, lcd_output) == False:
        return str_idx
    
    # and the subsequent rows...
    for i in range(row+1, LCD_NUM_ROWS+1):
        nc = display_string(i, 1, lcd_output[str_idx:])

        # update
        str_idx  = str_idx + nc
        disp_col = 1

        if continue_dumping(str_idx, lcd_output) == False:
            break

    return str_idx
     

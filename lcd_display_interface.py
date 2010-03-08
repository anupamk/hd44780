# lcd-wide control related imports
from hd44780_driver import reset_lcd as reset
from hd44780_driver import initialize_lcd as initialize

# display related imports
from hd44780_driver import write_string
from hd44780_driver import write_custom_character

# this module provdies a high-level interface to the functionality
# offered by the hd44780_driver.

LCD_PRINTF_FUNCTION_TABLE = {
    '%s' : write_string,
    '%B' : write_custom_character
}

# execute the functions defined above with the argument
def apply_lcd_printf(arg_val):
    LCD_PRINTF_FUNCTION_TABLE[arg_val[0]](arg_val[1])

# a simple printf like interface for displaying stuff on the lcd
# module. 
def printf(fmt_args, *fmt_argv):
    fmt_split_args = fmt_args.split()
    fmt_arg_values = []

    for v in fmt_argv:
        fmt_arg_values.append(v)

    # now, we have both arguments and values, in separate
    # lists. combine them into one neat package
    printf_arg_values = zip(fmt_split_args, fmt_arg_values)

    # display each value
    map(apply_lcd_printf, printf_arg_values)
    

from hd44780_driver import write_string
from hd44780_driver import write_custom_charset

# this module provdies a high-level interface to the functionality
# offered by the hd44780_driver.

LCD_PRINTF_FUNCTION_TABLE = {
    '%s' : write_string,
    '%B' : write_custom_charset
}

# execute the functions defined above with the argument
def apply_lcd_printf(arg_val):
    LCD_PRINTF_FUNCTION_TABLE[arg_val[0]](arg_val[1])

# a simple printf like interface for displaying stuff on the lcd
# module. 
def do_printf(args, *argv):
    fmt_args   = args.split()
    arg_values = []

    for v in argv:
        arg_values.append(v)

    # now, we have both arguments and values, in separate
    # lists. combine them into one neat package
    printf_arg_values = zip(fmt_args. arg_values)

    # display each value
    map(apply_lcd_printf, printf_arg_values)
    

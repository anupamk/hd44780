#!/usr/bin/env python

import lcd_display_interface as lcd_disp


# demo of custom-characters
CUSTOM_CHAR_MAP = {
    # CC-NAME    : [ DB0,  DB1,  DB2,  DB3,  DB4,  DB5,  DB6,  DB7] 
    'BETTER-BAR' : [0x00, 0x00, 0x1f, 0x1f, 0x1f, 0x1f, 0x00, 0x00],
    'BELL'       : [0x04, 0x0e, 0x0e, 0x0e, 0x1f, 0x00, 0x04, 0x00]
}

# display something:
def display_something():
    lcd_disp.do_printf("%s", "hello world")

    for shape_name, shape_val in CUSTOM_CHAR_MAP.iteritems():
        lcd_disp.do_printf("%s %B", shape_name, shape_val)



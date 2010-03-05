#!/usr/bin/env python

import parallel
import time
import hd44780_driver as lcd_driver


# demo of custom-characters
CUSTOM_CHAR_MAP = {
    'BETTER-BAR' : [0x00, 0x00, 0x1f, 0x1f, 0x1f, 0x1f, 0x00],
    'CIRCLE-DOT' : [0x00, 0x0e, 0x11, 0x15, 0x11, 0x0e, 0x00],
    'BELL'       : [0x04, 0x0e, 0x0e, 0x0e, 0x1f, 0x04, 0x00],
}

# create custom characters from CUSTOM_CHAR_MAP
def create_some_custom_chars():
    cc_location = 1

    for cc_shape_name, cc_shape_val in CUSTOM_CHAR_MAP.iteritems():
        print "creating custom character '%s'" % (cc_shape_name)
        lcd_driver.create_custom_charset(cc_location, cc_shape_val)

        cc_location = cc_location + 1

# show some custom-characters
def display_all_cc():
    num_cc = len(CUSTOM_CHAR_MAP)

    lcd_driver.lcd_position_cursor(1,1)
    for i in range(num_cc):
        lcd_driver.display_custom_char(i+1)


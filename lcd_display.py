#!/usr/bin/env python

import time

# lcd specific
import lcd_interface as lcd

# demo of custom-characters
CUSTOM_CHAR_MAP = {
    # CC-NAME    : [ DB0,  DB1,  DB2,  DB3,  DB4,  DB5,  DB6,  DB7] 
    'BETTER-BAR' : [0x00, 0x00, 0x1f, 0x1f, 0x1f, 0x1f, 0x00, 0x00],
    'BELL'       : [0x04, 0x0e, 0x0e, 0x0e, 0x1f, 0x00, 0x04, 0x00]
}

# display something:
def display_something():
    lcd.printf(1, 1, "%s ", "hello world")
    lcd.printf(2, 2, "%s ", "hello world")
    lcd.printf(3, 3, "%s ", "hello world")
    lcd.printf(4, 4, "%s ", "hello world")




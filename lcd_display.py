#!/usr/bin/env python

import time

# lcd specific
import lcd_interface as lcd

# display something:
def display_something():
    lcd.printf(1, 1, "%s ", "hello world")                 # canonical
    lcd.cc_printf(2,1, 'BELL')
    
# initialize the lcd first
lcd.initialize()






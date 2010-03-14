#!/usr/bin/env python

import hd44780_driver        as lcd_driver             # low-level stuff
import lcd_interface         as lcd_ascii              # vanilla-ascii
import lcd_custom_characters as lcd_cc                 # custom-characters


# a rudimentary class
class CustomCharacter:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

# lets define some custom characters
#   - cgram_location == -1 below implies a value that will be assigned
#     to during creation of the shape
POPULAR_CUSTOM_CHARACTERS = [
    CustomCharacter(cgram_location = -1, byte_seq = [0x04, 0x0e, 0x0e, 0x0e, 0x1f, 0x00, 0x04, 0x00], name = 'BELL'),
    CustomCharacter(cgram_location = -1, byte_seq = [0x00, 0x00, 0x1f, 0x1f, 0x1f, 0x1f, 0x00, 0x00], name = 'BAR' )
]






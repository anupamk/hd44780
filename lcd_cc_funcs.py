#!/usr/bin/env python

import lcd_cc_if      as lcd_cc_if              # custom-characters
from custom_char_def  import CustomCharacter

# return the char equivalent of a 5bit array
def _5bits_to_char(b4, b3, b2, b1, b0):
    return ((b4 << 4) |
            (b3 << 3) |
            (b2 << 2) |
            (b1 << 1) |
            (b0))

# bunch of custom shapes
CUSTOM_BAR_SHAPES = [
    CustomCharacter(cgram_loc = 1,
                    number    = 1,
                    name      = '1',
                    byte_seq  = [_5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 0, 0, 0, 0),
                                 _5bits_to_char(1, 0, 0, 0, 0),
                                 _5bits_to_char(1, 0, 0, 0, 0),
                                 _5bits_to_char(1, 0, 0, 0, 0),
                                 _5bits_to_char(1, 0, 0, 0, 0),
                                 _5bits_to_char(1, 0, 0, 0, 0),
                                 _5bits_to_char(1, 1, 1, 1, 1)]
                    ),
    
    CustomCharacter(cgram_loc = 2,
                    number    = 2,
                    name      = '2',
                    byte_seq  = [_5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 0, 0, 0),
                                 _5bits_to_char(1, 1, 0, 0, 0),
                                 _5bits_to_char(1, 1, 0, 0, 0),
                                 _5bits_to_char(1, 1, 0, 0, 0),
                                 _5bits_to_char(1, 1, 0, 0, 0),
                                 _5bits_to_char(1, 1, 0, 0, 0),
                                 _5bits_to_char(1, 1, 1, 1, 1)]
                    ),

    CustomCharacter(cgram_loc = 3,
                    number    = 3,
                    name      = '3',
                    byte_seq  = [_5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 1, 0, 0),
                                 _5bits_to_char(1, 1, 1, 0, 0),
                                 _5bits_to_char(1, 1, 1, 0, 0),
                                 _5bits_to_char(1, 1, 1, 0, 0),
                                 _5bits_to_char(1, 1, 1, 0, 0),
                                 _5bits_to_char(1, 1, 1, 0, 0),
                                 _5bits_to_char(1, 1, 1, 1, 1)]
                    ),

    CustomCharacter(cgram_loc = 4,
                    number    = 4,
                    name      = '4',
                    byte_seq  = [_5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 1, 1, 0),
                                 _5bits_to_char(1, 1, 1, 1, 0),
                                 _5bits_to_char(1, 1, 1, 1, 0),
                                 _5bits_to_char(1, 1, 1, 1, 0),
                                 _5bits_to_char(1, 1, 1, 1, 0),
                                 _5bits_to_char(1, 1, 1, 1, 0),
                                 _5bits_to_char(1, 1, 1, 1, 1)]
                    ),
    
    CustomCharacter(cgram_loc = 5,
                    number    = 5,
                    name      = '5'
                    byte_seq  = [_5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 1, 1, 1, 1)]
                    )

    CustomCharacter(cgram_loc = 6,
                    number    = 6,
                    name      = '01'
                    byte_seq  = [_5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(0, 0, 0, 0, 1),
                                 _5bits_to_char(0, 0, 0, 0, 1),
                                 _5bits_to_char(0, 0, 0, 0, 1),
                                 _5bits_to_char(0, 0, 0, 0, 1),
                                 _5bits_to_char(0, 0, 0, 0, 1),
                                 _5bits_to_char(0, 0, 0, 0, 1),
                                 _5bits_to_char(1, 1, 1, 1, 1)]
                    )

    CustomCharacter(cgram_loc = 7,
                    number    = 7,
                    name      = '11',
                    byte_seq  = [_5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(1, 0, 0, 0, 1),
                                 _5bits_to_char(1, 0, 0, 0, 1),
                                 _5bits_to_char(1, 0, 0, 0, 1),
                                 _5bits_to_char(1, 0, 0, 0, 1),
                                 _5bits_to_char(1, 0, 0, 0, 1),
                                 _5bits_to_char(1, 0, 0, 0, 1),
                                 _5bits_to_char(1, 1, 1, 1, 1)]
                    )

    CustomCharacter(cgram_loc = 8,
                    number    = 8,
                    name      = '00',
                    byte_seq  = [_5bits_to_char(1, 1, 1, 1, 1),
                                 _5bits_to_char(0, 0, 0, 0, 0),
                                 _5bits_to_char(0, 0, 0, 0, 0),
                                 _5bits_to_char(0, 0, 0, 0, 0),
                                 _5bits_to_char(0, 0, 0, 0, 0),
                                 _5bits_to_char(0, 0, 0, 0, 0),
                                 _5bits_to_char(0, 0, 0, 0, 0),
                                 _5bits_to_char(1, 1, 1, 1, 1)]
                    )
    ]

# load all the custom shapes defined above
def load_all_custom_shapes():
    for shape in CUSTOM_BAR_SHAPES:
        lcd_cc_if.load_custom_character(shape, True)

# cgram is mapped one-to-one to number of lines. nothing fancy todo.
def cgram_shape_location(num_lines):
    if (num_lines < 1 or num_lines > 8):
        return None

    return num_lines
    

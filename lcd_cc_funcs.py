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
                    name      = '1LINE',
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
                    name      = '2LINE',
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
                    name      = '3LINE',
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
                    name      = '4LINE',
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
                    name      = '5LINE',
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
                    name      = '1ENDLINE',
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
                    name      = '11LINE',
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
                    name      = 'SPACE',
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


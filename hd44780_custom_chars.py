from hd44780_driver import create_custom_charset
from hd44780_driver import exec_named_cmd

# 
# interface for custom-characters. fundamentally, each
# custom-character has the following items:
#    - a name (referral purposes)
#    - CGRAM location
#    - byte-sequence describing the pattern
#
LCD_MAX_CUSTOM_SHAPES_AT_A_TIME = 8


# a rudimentary class
class CustomCharacter:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

# lets define some custom characters
#   - cgram_location == -1 below implies a value that will be assigned
#     to during creation of the shape
POPULAR_CUSTOM_CHARACTERS = {
    'BELL'          :      CustomCharacter(cgram_location = -1, byte_seq = [0x04, 0x0e, 0x0e, 0x0e, 0x1f, 0x00, 0x04, 0x00]),
    'BAR'           :      CustomCharacter(cgram_location = -1, byte_seq = [0x00, 0x00, 0x1f, 0x1f, 0x1f, 0x1f, 0x00, 0x00])
}

# create all the custom characters
def load_custom_chars_to_cgram():
    cgram_index = 0
    
    # prevent cursor from jumping around...
    exec_named_cmd('DISPLAY_ON_CURSOR_OFF')

    # the real thang
    for shape_name, shape_props in POPULAR_CUSTOM_CHARACTERS.iteritems():

        # stop adding more than max possible shapes.
        if cgram_index == LCD_MAX_CUSTOM_SHAPES_AT_A_TIME:
            break;
        
        shape_props.cgram_location = cgram_index 
        create_custom_charset(shape_props.cgram_location, shape_props.byte_seq)
        cgram_index = cgram_index + 1

    # restore the balance
    exec_named_cmd('DISPLAY_ON_CURSOR_ON_BLINK_ON')

# where is this shape in the CGRAM ?
def get_custom_char_cgram_location(shape_name):
    try:
        cc = POPULAR_CUSTOM_CHARACTERS[shape_name]
    except KeyError:
        print "Error: Unknown Shape : '%s'" % (shape_name)
        return None

    return cc.cgram_location
    
    

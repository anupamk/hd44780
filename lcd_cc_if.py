import hd44780_driver as lcd_cc_driver
from custom_char_def import CustomCharacter

# custom-character has the following items:
#    - a name (referral purposes)
#    - CGRAM location
#    - byte-sequence describing the pattern
#
LCD_MAX_CUSTOM_SHAPES_AT_A_TIME = 8

# custom-character-map
loaded_custom_characters = { }

# this function returns the location of a 'shape' in the set of
# custom-characters that are loaded. 
def get_custom_char_cgram_location(shape_name):
    try:
        cc = loaded_custom_characters[shape_name]
    except KeyError:
        print "Error: Unknown Shape: '%s'" % (shape_name)
        return None

    return cc.cgram_loc
        
# this function is called to load a custom character into the
# cgram. each character is identified by a 'name'.
#
# loaded_custom_characters contains all the available
# custom-characters. 
def load_custom_character(cc, force = False):
    num_cc = len(loaded_custom_characters)
    cc_loc = num_cc + 1

    # max-limit-reached do nothing    
    if ((force == False) and
        (num_cc == LCD_MAX_CUSTOM_SHAPES_AT_A_TIME)):
        return

    # bad 'force' 
    if ((force == True) and
        ((cc.cgram_loc < 0) or (cc.cgram_loc > 8))):
        return

    # does it exist ?
    if (force == True):
        cc_loc = cc.cgram_loc

    lcd_cc_driver.exec_named_cmd('DISPLAY_ON_CURSOR_OFF')

    # load it at 'cc_loc'
    cc.cgram_loc = cc_loc
    lcd_cc_driver.create_custom_charset(cc.cgram_loc, cc.byte_seq)
    loaded_custom_characters[cc.name] = cc
        
    lcd_cc_driver.exec_named_cmd('DISPLAY_ON_CURSOR_ON_BLINK_ON')
        
    return cc.cgram_loc

# show the shape. nothing fancy at all...
def cc_printf(row, col, shape_name = None):
    cc_loc = get_custom_char_cgram_location(shape_name)

    # can't do much
    if cc_loc == None:
        return
    
    lcd_cc_driver.write_custom_character_at(row, col, cc_loc)



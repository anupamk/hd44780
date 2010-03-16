import hd44780_driver as lcd_cc_driver

# custom-character has the following items:
#    - a name (referral purposes)
#    - CGRAM location
#    - byte-sequence describing the pattern
#
LCD_MAX_CUSTOM_SHAPES_AT_A_TIME = 8

# custom-character-map
loaded_custom_characters = { }

# a rudimentary class
class CustomCharacter:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

def get_custom_char_cgram_location(shape_name):
    try:
        cc = loaded_custom_characters[shape_name]
    except KeyError:
        print "Error: Unknown Shape: '%s'" % (shape_name)
        return None

    return cc.cgram_location
        
# this function is called to load a custom character into the
# cgram. each character is identified by a 'name'.
#
# loaded_custom_characters contains all the available
# custom-characters. 
def load_custom_character(custom_char, force = False):
    num_cc = len(loaded_custom_characters)

    # max-limit-reached do nothing    
    if ((force == False) and
        (num_cc == LCD_MAX_CUSTOM_SHAPES_AT_A_TIME)):
        return

    # does it exist ?
    cc_location = get_custom_char_cgram_location(custom_char.name)

    if (cc_location == None):
        lcd_cc_driver.exec_named_cmd('DISPLAY_ON_CURSOR_OFF')

        # create-it
        custom_char.cgram_location = num_cc + 1
        lcd_cc_driver.create_custom_charset(custom_char.cgram_location, custom_char.byte_seq)

        # add it to the available list
        loaded_custom_characters[custom_char.name] = custom_char
        
        lcd_cc_driver.exec_named_cmd('DISPLAY_ON_CURSOR_ON_BLINK_ON')
        
    return custom_char.cgram_location

# load all custom-characters into the cgram
def load_all_custom_characters(all_custom_char):
    for i in all_custom_char:
        load_custom_character(i)

# show the shape. nothing fancy at all...
def cc_printf(row, col, shape_name = None):
    cc_cgram_loc = get_custom_char_cgram_location(shape_name)

    # can't do much
    if cc_cgram_loc == None:
        return
    
    lcd_cc_driver.write_custom_character_at(row, col, cc_cgram_loc)



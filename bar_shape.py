from utils import *

# a struct defining custom-character. 
class custom_character:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

# bunch of custom shapes
bar_shape_list = [
    custom_character(cgram_loc =  1,
                     byte_seq  = [five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 0, 0, 0, 0),
                                  five_bits_to_char(1, 0, 0, 0, 0),
                                  five_bits_to_char(1, 0, 0, 0, 0),
                                  five_bits_to_char(1, 0, 0, 0, 0),
                                  five_bits_to_char(1, 0, 0, 0, 0),
                                  five_bits_to_char(1, 0, 0, 0, 0),
                                  five_bits_to_char(1, 1, 1, 1, 1)]
                     ),
    
    custom_character(cgram_loc =  2,
                     byte_seq  = [five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 0, 0, 0),
                                  five_bits_to_char(1, 1, 0, 0, 0),
                                  five_bits_to_char(1, 1, 0, 0, 0),
                                  five_bits_to_char(1, 1, 0, 0, 0),
                                  five_bits_to_char(1, 1, 0, 0, 0),
                                  five_bits_to_char(1, 1, 0, 0, 0),
                                  five_bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  3,
                     byte_seq  = [five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 1, 0, 0),
                                  five_bits_to_char(1, 1, 1, 0, 0),
                                  five_bits_to_char(1, 1, 1, 0, 0),
                                  five_bits_to_char(1, 1, 1, 0, 0),
                                  five_bits_to_char(1, 1, 1, 0, 0),
                                  five_bits_to_char(1, 1, 1, 0, 0),
                                  five_bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  4,
                     byte_seq  = [five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 1, 1, 0),
                                  five_bits_to_char(1, 1, 1, 1, 0),
                                  five_bits_to_char(1, 1, 1, 1, 0),
                                  five_bits_to_char(1, 1, 1, 1, 0),
                                  five_bits_to_char(1, 1, 1, 1, 0),
                                  five_bits_to_char(1, 1, 1, 1, 0),
                                  five_bits_to_char(1, 1, 1, 1, 1)]
                     ),
    
    custom_character(cgram_loc =  5,
                     byte_seq  = [five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  6,
                     byte_seq  = [five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(0, 0, 0, 0, 1),
                                  five_bits_to_char(0, 0, 0, 0, 1),
                                  five_bits_to_char(0, 0, 0, 0, 1),
                                  five_bits_to_char(0, 0, 0, 0, 1),
                                  five_bits_to_char(0, 0, 0, 0, 1),
                                  five_bits_to_char(0, 0, 0, 0, 1),
                                  five_bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  7,
                     byte_seq  = [five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(1, 0, 0, 0, 1),
                                  five_bits_to_char(1, 0, 0, 0, 1),
                                  five_bits_to_char(1, 0, 0, 0, 1),
                                  five_bits_to_char(1, 0, 0, 0, 1),
                                  five_bits_to_char(1, 0, 0, 0, 1),
                                  five_bits_to_char(1, 0, 0, 0, 1),
                                  five_bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  8,
                     byte_seq  = [five_bits_to_char(1, 1, 1, 1, 1),
                                  five_bits_to_char(0, 0, 0, 0, 0),
                                  five_bits_to_char(0, 0, 0, 0, 0),
                                  five_bits_to_char(0, 0, 0, 0, 0),
                                  five_bits_to_char(0, 0, 0, 0, 0),
                                  five_bits_to_char(0, 0, 0, 0, 0),
                                  five_bits_to_char(0, 0, 0, 0, 0),
                                  five_bits_to_char(1, 1, 1, 1, 1)]
                     ),
    ]

# put a bar at a given location on the lcd.
#   - 'max-size' is the maximum number of columns that will be
#     occupied by the bar
#
#   - 'value' is the current value to be displayed as a bar.
#
# no checks are made to see if the bar would actually 'fit' on the
# display. 
def show_usage_meter(lcd, row, col, bar_width, usage_val):
    lines_per_col = lcd.lines_per_col
    
    # compute how many full, and partial lines are required
    max_lines  = int(usage_val * (bar_width * lines_per_col) / 100)
    part_lines = max_lines % lines_per_col
    full_lines = (max_lines - part_lines)/lines_per_col

    # setup the border properly
    for i in range(bar_width):
        lcd.put_shape(row, col+i, 7)

    # write all full lines
    last_col = col
    for i in range(full_lines):
        lcd.put_shape(row, last_col, 4)
        last_col = last_col + 1

    # write custom shape for partial lines
    if (part_lines > 0):
        lcd.put_shape(row, last_col, part_lines-1)

    lcd.flush_row(row)
    return

import generic_lcd as lcd

# a struct defining custom-character. 
class custom_character:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

# return the char equivalent of a 5bit array
def __5bits_to_char(b4, b3, b2, b1, b0):
    return ((b4 << 4) |
            (b3 << 3) |
            (b2 << 2) |
            (b1 << 1) |
            (b0))

# shape specific
NUM_LINES_PER_COLUMN = 5

# bunch of custom shapes
CUSTOM_BAR_SHAPES = [
    custom_character(cgram_loc =  1,
                     number    =  1,
                     name      = '1',
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 0, 0, 0, 0),
                                  __5bits_to_char(1, 0, 0, 0, 0),
                                  __5bits_to_char(1, 0, 0, 0, 0),
                                  __5bits_to_char(1, 0, 0, 0, 0),
                                  __5bits_to_char(1, 0, 0, 0, 0),
                                  __5bits_to_char(1, 0, 0, 0, 0),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),
    
    custom_character(cgram_loc =  2,
                     number    =  2,
                     name      = '2',
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 0, 0, 0),
                                  __5bits_to_char(1, 1, 0, 0, 0),
                                  __5bits_to_char(1, 1, 0, 0, 0),
                                  __5bits_to_char(1, 1, 0, 0, 0),
                                  __5bits_to_char(1, 1, 0, 0, 0),
                                  __5bits_to_char(1, 1, 0, 0, 0),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  3,
                     number    =  3,
                     name      = '3',
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 0, 0),
                                  __5bits_to_char(1, 1, 1, 0, 0),
                                  __5bits_to_char(1, 1, 1, 0, 0),
                                  __5bits_to_char(1, 1, 1, 0, 0),
                                  __5bits_to_char(1, 1, 1, 0, 0),
                                  __5bits_to_char(1, 1, 1, 0, 0),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  4,
                     number    =  4,
                     name      = '4',
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 0),
                                  __5bits_to_char(1, 1, 1, 1, 0),
                                  __5bits_to_char(1, 1, 1, 1, 0),
                                  __5bits_to_char(1, 1, 1, 1, 0),
                                  __5bits_to_char(1, 1, 1, 1, 0),
                                  __5bits_to_char(1, 1, 1, 1, 0),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),
    
    custom_character(cgram_loc =  5,
                     number    =  5,
                     name      = '5',
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  6,
                     number    =  6,
                     name      = 'A',
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  7,
                     number    =  7,
                     name      = 'B',                           
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 0, 0, 0, 1),
                                  __5bits_to_char(1, 0, 0, 0, 1),
                                  __5bits_to_char(1, 0, 0, 0, 1),
                                  __5bits_to_char(1, 0, 0, 0, 1),
                                  __5bits_to_char(1, 0, 0, 0, 1),
                                  __5bits_to_char(1, 0, 0, 0, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc =  8,
                     number    =  8,
                     name      = 'C',
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(0, 0, 0, 0, 0),
                                  __5bits_to_char(0, 0, 0, 0, 0),
                                  __5bits_to_char(0, 0, 0, 0, 0),
                                  __5bits_to_char(0, 0, 0, 0, 0),
                                  __5bits_to_char(0, 0, 0, 0, 0),
                                  __5bits_to_char(0, 0, 0, 0, 0),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),
    ]

# load all custom shapes into the display
def load_cust_shapes(lcd):
    row = 0
    for shape in CUSTOM_BAR_SHAPES:
        lcd.cp_shape(row, shape.byte_seq)
        row = row + 1

    lcd.load_shapes()
    return

# return the cgram-location for the shape-name (1-to-1 mapping)
def get_shape_cgram_loc(shape_name):
    print "shape-name = '%s'" % (shape_name)
    return int(shape_name)

# put a bar at a given location on the lcd.
#   - 'max-size' is the maximum number of columns that will be
#     occupied by the bar
#
#   - 'value' is the current value to be displayed as a bar.
#
# no checks are made to see if the bar would actually 'fit' on the
# display. 
def show_usage_meter(lcd, row, col, bar_width, usage_val):
    # compute how many full, and partial lines are required
    max_lines  = int(usage_val * (bar_width * NUM_LINES_PER_COLUMN) / 100)
    part_lines = max_lines % NUM_LINES_PER_COLUMN
    full_lines = (max_lines - part_lines)/NUM_LINES_PER_COLUMN

    print "USAGE-METER: [usage: %.1f, max-lines: %d, full-lines: %d, partial-lines: %d]" %  (usage_val,
                                                                                             max_lines,
                                                                                             full_lines,
                                                                                             part_lines)

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
        lcd.put_shape(row,
                      last_col,
                      part_lines - 1)
        
    return
    


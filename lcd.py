import lcd_generic as lcd

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
    custom_character(cgram_loc = 1,
                     number    = 1,
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
    
    custom_character(cgram_loc = 2,
                     number    = 2,
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

    custom_character(cgram_loc = 3,
                     number    = 3,
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

    custom_character(cgram_loc = 4,
                     number    = 4,
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
    
    custom_character(cgram_loc = 5,
                     number    = 5,
                     name      = '5'
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc = 6,
                     number    = 6,
                     name      = 'A'
                     byte_seq  = [__5bits_to_char(1, 1, 1, 1, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(0, 0, 0, 0, 1),
                                  __5bits_to_char(1, 1, 1, 1, 1)]
                     ),

    custom_character(cgram_loc = 7,
                     number    = 7,
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

    custom_character(cgram_loc = 8,
                     number    = 8,
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
def load_all_custom_shapes(lcd):
    for shape in CUSTOM_BAR_SHAPES:
        lcd.write_cgram_vector(shape.cgram_loc, shape.byte_seq)

    # load all the shapes on the display
    lcd.load_shapes()
    return

# return the cgram-location for the shape-name (1-to-1 mapping)
def get_shape_cgram_loc(shape_name):
    return int(shape_name)

# put a bar at a given location on the lcd.
#   - 'max-size' is the maximum number of columns that will be
#     occupied by the bar
#
#   - 'value' is the current value to be displayed as a bar.
#
# no checks are made to see if the bar would actually 'fit' on the
# display. 
def show_usage_bar(lcd, row, col, bar_width, usage_val):
    start_col = col
    
    # compute how many full, and partial lines are required
    max_lines  = usage_val * (bar_width * NUM_LINES_PER_COLUMN) / 100
    part_lines = max_lines % NUM_LINES_PER_COLUMN
    full_lines = (max_lines - part_lines)/NUM_LINES_PER_COLUMN

    # write the full lines
    for i in range(full_lines):
        start_col = start_col + i
        lcd.write_lcd_matrix(row,
                             start_col,
                             get_shape_cgram_loc(str(NUM_LINES_PER_LOCATION)))

    # write partial lines
    lcd.write_lcd_matrix(row,
                         start_col + 1,
                         get_shape_cgram_loc(str(part_lines)))
    

    # show it
    lcd.flush()
    


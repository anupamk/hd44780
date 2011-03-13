from lcd_interface import *
from utils import printf

# a dummy lcd class which implements the lcd-interface.
class lcd_dummy(lcd_interface):
    def flush_row(self, row):
        printf("flush-row: %d", row)
        return

    def put_string(self, location, display_string):
        printf("put-string: location: [row: %d, col: %d], display-string: [fmt: %s, str: %s]",
               location[0], location[1],
               display_string[0], display_string[1])
        return

    def put_center_string(self, row, display_string):
        printf("put-center-string: [row: %d, display-string: %s]", row, display_string)
        return

    def put_shape(self, location, shape_vector):
        printf("put-shape: location: [row: %d, col: %d], shape: %s",
               location[0], location[1],
               shape_vector)
        return

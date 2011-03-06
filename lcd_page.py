import generic_lcd as lcd
from bar_shape import *

class lcd_page(object):
    def __init__(self, name, display_func, custom_shapes, disp_lcd):
        self.name          = name
        self.lcd_obj       = disp_lcd
        self.display_func  = display_func
        self.custom_shapes = custom_shapes

        return

    def display(self):
        self.display_func(self.lcd_obj)
        return

    def load_custom_shapes(self):
        row = 0
        if (self.custom_shapes == None):
            return
        
        # load custom shapes
        for shape in self.custom_shapes:
            self.lcd_obj.cp_shape(row, shape.byte_seq)
            row = row + 1
            
        self.lcd_obj.load_shapes()

        return

    def initialize(self):
        self.lcd_obj.initialize()
        self.load_custom_shapes()
        
        return
        
        


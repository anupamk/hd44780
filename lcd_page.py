import generic_lcd as lcd

# lcd_page provides a means of displaying different 'pages' of information one
# at a time. a 'page' contains it's own display function, and an associated set
# of custom shapes which can provide non-ascii display e.g. a cpu-usage meter
# etc. 
class lcd_page(object):
    def __init__(self, disp_lcd, name, total_duration, refresh_rate, display_func, custom_shapes):
        self.lcd_obj       = disp_lcd
        self.name          = name
        self.pg_disp_time  = total_duration
        self.refresh_rate  = refresh_rate
        self.display_func  = display_func
        self.custom_shapes = custom_shapes

        return

    def display(self):
        self.display_func(self)
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
        
        


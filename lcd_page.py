# lcd_page provides a means of displaying different 'pages' of information one
# at a time. a 'page' contains it's own display function, and an associated set
# of custom shapes which can provide non-ascii display e.g. a cpu-usage meter
# etc. 
class lcd_page(object):
    def __init__(self, disp_lcd, name, display_func, total_duration = 30.0, refresh_rate = 1.0):
        self.lcd_obj       = disp_lcd
        self.name          = name
        self.pg_disp_time  = total_duration
        self.display_func  = display_func

        # can't refresh faster than 1/sec
        if refresh_rate < 1.0:
            refresh_rate = 1.0
        self.refresh_rate  = refresh_rate

        return

    def show(self):
        self.lcd_obj.do_init()
        self.display_func(self)
        
        return
        

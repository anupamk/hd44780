# an abstract class describing the interface that is exported by
# different implementations of lcd.
class lcd_interface(object):
    def flush_row(self, row):
        """
        called to flush the contents of a given row onto the lcd
        """
        abstract()
        return
    
    def put_string(self, location, display_str):
        """
        called to put a string at a given location on the
        lcd. location is specified using a typical [row, col], and the
        string is specified using python specific 'format-string'

        the string is displayed on the device when explicitly
        flushed.
        """
        abstract()
        return
    
    def put_center_string(self, row, display_str):
        """
        places a string in the center of the current row.
        """
        abstract()
        return

    def put_shape(self, location, display_shape):
        """
        places a user-defined shape at a given location on the
        display.

        the shape needs to be flushed to display it on the lcd.
        """
        abstract()
        return

    def load_custom_shapes(self, shape_list):
        """
        loads a bunch of shapes into the display-ram
        """
        abstract()
        return
    
    def display_string(self, location, display_str):
        """
        a 'thin' wrapper over the 'put_string' function. flushes the
        string-to-be-displayed onto the device.
        """
        row = location[0]
        self.put_string(location, display_str)
        self.flush_row(row)

        return

    def display_center_string(self, row, display_str):
        """
        a 'thin' wrapper over the 'put_center_string'
        function. flushes teh string-to-be-displayed onto the device
        """
        self.put_center_string(row, display_str)
        self.flush_row(row)
        
        return

def abstract():
    """
    raise 'NotImplementedError' when invoked for pure-interface type
    classes. 
    """
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')


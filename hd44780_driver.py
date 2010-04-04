import pp_driver

# this module provides an interface to the functionality offered by
# the HD44780 Text LCD Display.


# following dictionary contains the set of available commands for the
# lcd module. this is not a comprehensive list anyways. it just
# contains the commands that we are currently interested in.
# 
# a function 'get_instruction_data' is defined which takes a
# command-name defined below, and returns the appropriate RS, R/W,
# DB7-DB0 values, which are then used.
LCD_INSTRUCTION_TABLE = {
    # COMMAND-NAME                                  : [  RS,  R/W,  DB7,  DB6,  DB5,  DB4,  DB3,  DB2,  DB1,  DB0]
    'DISPLAY_CLEAR'                                 : [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01],
    'RETURN_HOME'                                   : [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
    'DISPLAY_OFF'                                   : [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00],
    'DISPLAY_ON'                                    : [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x00, 0x00],
    'DISPLAY_ON_CURSOR_OFF'                         : [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x00, 0x00],
    'DISPLAY_ON_CURSOR_ON_BLINK_OFF'                : [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x01, 0x00],
    'DISPLAY_ON_CURSOR_ON_BLINK_ON'                 : [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x01, 0x01],
    'DISPLAY_PARAM_8BIT_2LINE_5x8DOTS'              : [0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x01, 0x01, 0x00, 0x00],
    'WRITE_CGRAM_ADDRESS'                           : [0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    'WRITE_DDRAM_ADDRESS'                           : [0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    'WRITE_DATA_TO_RAM'                             : [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
}

# this function is called to convert an 8bit array to an equivalen
# char. index-0 is MSB, index-7 is LSB
def _bits2char(bit_array):
    return ((bit_array[0] << 7) |
            (bit_array[1] << 6) |
            (bit_array[2] << 5) |
            (bit_array[3] << 4) |
            (bit_array[4] << 3) |
            (bit_array[5] << 2) |
            (bit_array[6] << 1) |
            (bit_array[7] << 0))

# this function is called to return rs, r/w, db0-db7 values for a
# given instruction. for write_XXX instructions, addr_val should be
# appropriately populated
def get_instruction_data(instruction_name, addr_val = 0):
    reg_select = 0x00
    read_write = 0x00
    instr_val  = 0x00

    # lookup the instruction, and return the value
    try:
        instr_tab  = LCD_INSTRUCTION_TABLE[instruction_name]
    except KeyError:
        print "Error: Unknown / Un-Implemented Command : '%s'" % (instruction_name)
        return None

    # instruction_name is ok
    reg_select = instr_tab[0]
    read_write = instr_tab[1]
    instr_val  = _bits2char(instr_tab[2:]) | addr_val

    return (reg_select, read_write, instr_val)

# this function is called to execute a named-command  (from the
# LCD_INSTRUCTION_TABLE)
def exec_named_cmdval(cmd_name, cmd_val):
    rs, rw, cmd_value = get_instruction_data(cmd_name, cmd_val)

    # nothing to do
    if (rs == None or rw == None or cmd_val == None):
        return
    
    # the real thang
    print "[cmd-name:'%32s', cmd-value: '%3d', reg-sel: '%2d']" % (cmd_name, cmd_value, rs)
    pp_driver.exec_command(rs, cmd_value)

# execute a named-command
def exec_named_cmd(cmd_name):
    exec_named_cmdval(cmd_name, 0)

# execute a sequence of commands
def exec_named_cmdseq(cmd_name_seq):
    for cmd_name in cmd_name_seq:
        exec_named_cmd(cmd_name)

# position the cursor to a specific location on the lcd
def position_cursor(rowcol_ddram_addr):
    exec_named_cmdval('WRITE_DDRAM_ADDRESS', rowcol_ddram_addr)

def write_data_byte(data):
    pp_driver.write_data_byte(data)
    
# write a ascii-character data
def write_char_data(char):
    write_data_byte(ord(char))

# this function is called to create a custom-character at a given
# location in the CGRAM
def create_custom_charset(cc_start_addr, shape_byte_seq):
    exec_named_cmdval('WRITE_CGRAM_ADDRESS', cc_start_addr)

    for i in shape_byte_seq:
        exec_named_cmdval('WRITE_DATA_TO_RAM', i)

# this function is called to display a custom-character at current
# DDRAM location
def display_custom_char(cgram_addr):
    write_data_byte(cgram_addr)

# reset the lcd to a sane state. everything is cleaned out
def reset():
    exec_named_cmdseq(['DISPLAY_CLEAR',
                       'DISPLAY_OFF',
                       'DISPLAY_ON_CURSOR_ON_BLINK_ON',
                       'DISPLAY_PARAM_8BIT_2LINE_5x8DOTS',
                       'RETURN_HOME'])

# initialize the lcd to 8bit mode, with a blinking-cursor at (0, 0)
def initialize():
    exec_named_cmdseq(['DISPLAY_ON_CURSOR_ON_BLINK_ON',
                       'DISPLAY_CLEAR',
                       'DISPLAY_PARAM_8BIT_2LINE_5x8DOTS',
                       'RETURN_HOME'])


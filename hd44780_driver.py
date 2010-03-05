#!/usr/bin/env python

import parallel
import time

# global-definitions
pp = parallel.Parallel()

# following dictionary contains the set of available commands for the
# lcd module. this is not a comprehensive list anyways. it just
# contains the commands that we are currently interested in.
# 
# a function 'lcd_get_instruction_data' is defined which takes a
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

# store start (row, col) ddram-address. other columns, are just a
# linear offset away from start
LCD_DDRAM_ADDRESS_TABLE = [
    [1, 0x00],                  
    [2, 0x40],
    [3, 0x14],
    [4, 0x54]
]

# 
# some notes about custom-characters:
#    1. all pre-defined characters are available in the CGROM
#    2. a ram area, called CGRAM, of 64 bytes is available for custom
#       characters. since each custom-character consumes 8 bytes,
#       there are 8 such characters that can be defined at a time.
#    3. CGRAM address starts from 0x40. Thus, we have the following
#       custom-char-num -> cgram-start-address map:
#           -- custom-char-0 : 0x40
#           -- custom-char-1 : 0x48
#           -- custom-char-2 : 0x50
#           -- custom-char-3 : 0x58
#       etc.
#    4. Displaying custom characters is pretty straightforward. We
#       just write to the DDRAM the contents of a custom-char-location
#       as defined in (3) above.
# 
LCD_CUSTOMCHAR_ADDRESS_MAP = [
    [1, 0x40],
    [2, 0x48],
    [3, 0x50],
    [4, 0x58],
    [5, 0x60],
    [6, 0x68],
    [7, 0x70],
    [8, 0x78]
]


# this function is called to convert an 8bit array to an equivalen
# char. index-0 is MSB, index-7 is LSB
def bits2char(bit_array):
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
def lcd_get_instruction_data(instruction_name, addr_val = 0):
    reg_select = 0x00
    read_write = 0x00
    instr_val  = 0x00

    # lookup the instruction, and return the value
    instr_tab  = LCD_INSTRUCTION_TABLE[instruction_name]
    
    if instr_tab == None:
        return reg_select, read_write, instr_val

    # instruction_name is ok
    reg_select = instr_tab[0]
    read_write = instr_tab[1]
    instr_val  = bits2char(instr_tab[2:]) | addr_val

    return (reg_select, read_write, instr_val)

# this function is called to get the DDRAM address for a corresponding
# (row, col) value
def lcd_get_ddram_address(row, col):
    return LCD_DDRAM_ADDRESS_TABLE[row - 1][1] + (col - 1)

# this function is called to get the CGRAM-START-ADDRESSS for a given
# custom-character 
def lcd_get_cc_cgram_start_addr(cc_loc):
    return LCD_CUSTOMCHAR_ADDRESS_MAP[cc_loc - 1][1]

# 
# || port         :  HD-44780
# D0 - D7         :  DB0 - DB7
# C0 (inv)        :  E
# C2 (non-inv)    :  RS
#

# 
# first we define top level functions that make the whole thing
# work. next we define abstractions on these building blocks
#

# this function is called to strobe the enable pin. data is only
# considered valid when it is high
def toggle_enable():
    pp.setDataStrobe(1)         # E == low
    time.sleep(0.0001)
    pp.setDataStrobe(0)         # E == high
    time.sleep(0.0001)

# send out some control command
def lcd_exec_command(reg_select, ctrl):
    pp.setInitOut(reg_select)
    pp.setData(ctrl)
    toggle_enable()

# this function is called to execute a named-command  (from the
# LCD_INSTRUCTION_TABLE)
def lcd_exec_named_cmdval(cmd_name, cmd_val):
    rs, _, cmd_value = lcd_get_instruction_data(cmd_name, cmd_val)
    
    print "[cmd-name:'%32s', cmd-value: '%3d', reg-sel: '%2d']" % (cmd_name, cmd_value, rs)
    lcd_exec_command(rs, cmd_value)
    
def lcd_exec_named_cmd(cmd_name):
    lcd_exec_named_cmdval(cmd_name, 0)

# execute a sequence of commands
def lcd_exec_named_cmdseq(cmd_name_seq):
    for cmd_name in cmd_name_seq:
        lcd_exec_named_cmd(cmd_name)

# position the cursor to a specific location on the lcd
def lcd_position_cursor(lcd_row, lcd_col):
    rowcol_ddram_addr = lcd_get_ddram_address(lcd_row, lcd_col)
    lcd_exec_named_cmdval('WRITE_DDRAM_ADDRESS', rowcol_ddram_addr)

# write some data
def lcd_write_data(data):
    pp.setInitOut(1)
    pp.setData(data)
    toggle_enable()

# position the cursor to a specific location on the lcd    
# write a ascii-character data
def lcd_write_char_data(char):
    lcd_write_data(ord(char))

# write a string onto the lcd
def lcd_write_string(msg_string):
    for ch in msg_string:
        lcd_write_char_data(ch)

    # don't show the cursor anymore
    lcd_exec_named_cmd('DISPLAY_ON_CURSOR_OFF')

# write string at a given location
def lcd_write_string_at(row, col, msg_string):
    lcd_position_cursor(row, col)
    lcd_write_string(msg_string)

    # don't show the cursor any-more
    lcd_exec_named_cmd('DISPLAY_ON_CURSOR_OFF')

# this function is called to create a custom-character at a given
# location in the CGRAM
def create_custom_charset(cc_loc, cc_byte_string):
    cc_start_addr = lcd_get_cc_cgram_start_addr(cc_loc)
    lcd_exec_named_cmdval('WRITE_CGRAM_ADDRESS', cc_start_addr)

    for i in cc_byte_string:
        lcd_exec_named_cmdval('WRITE_DATA_TO_RAM', i)

# this function is called to display a custom-character at current
# DDRAM location
def display_custom_char(cc_loc):
    lcd_write_data(cc_loc - 1)

def display_custom_char_at(lcd_row, lcd_col, cc_loc):
    lcd_position_cursor(lcd_row, lcd_col)
    display_custom_char(cc_loc)

# reset the lcd to a sane state. everything is cleaned out
def reset_lcd():
    lcd_exec_named_cmdseq(['DISPLAY_CLEAR',
                           'DISPLAY_OFF',
                           'DISPLAY_ON_CURSOR_ON_BLINK_ON',
                           'DISPLAY_PARAM_8BIT_2LINE_5x8DOTS',
                           'RETURN_HOME'])

# initialize the lcd to 8bit mode, with a blinking-cursor at (0, 0)
def initialize_lcd():
    lcd_exec_named_cmdseq(['DISPLAY_ON_CURSOR_ON_BLINK_ON',
                           'DISPLAY_CLEAR',
                           'DISPLAY_PARAM_8BIT_2LINE_5x8DOTS',
                           'RETURN_HOME'])


    

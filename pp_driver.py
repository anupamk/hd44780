import parallel
import time

# global-definitions
pp = parallel.Parallel()

# here is how we expect the pins to be wired up:
# 
# || port         :  HD-44780
# DB0 - DB7       :  DB0 - DB7
# C0 (inv)        :  E
# C2 (non-inv)    :  RS
#

# this function is called to strobe the enable pin. data is only
# considered valid when it is high.
def _toggle_enable():
    pp.setDataStrobe(1)         # E == low
    time.sleep(0.0001)
    pp.setDataStrobe(0)         # E == high
    time.sleep(0.0001)

# send out some control command
def exec_command(reg_select, ctrl):
    pp.setInitOut(reg_select)
    pp.setData(ctrl)
    _toggle_enable()

# write some data
def write_data_byte(data):
    pp.setInitOut(1)
    pp.setData(data)
    _toggle_enable()

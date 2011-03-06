import os
import time
import string

from utils import *
from bar_shape import *

# useful constants
MACHINE_INFO_MAX_DISPLAY_ITERATIONS = 30
MACHINE_INFO_NAME_DISPLAY_ROW       = 0
MACHINE_INFO_CPU_USAGE_ROW          = 2
MACHINE_INFO_SYSTEM_UPTIME_ROW      = 3

# no debugging is required
DO_DEBUG_PRINT = False

# interface into external world
def get_name():
    return "Machine Info"

def get_custom_shapes():
    return bar_shape_list

def get_display_func():
    return display_machine_info

# this displays static machine specific information on the lcd
def display_static_machine_info(lcd):
    hostname = string.upper(os.uname()[1])
    lcd.display_center_string(MACHINE_INFO_NAME_DISPLAY_ROW, hostname)
    
    return

# this function returns the system uptime in the following format
#    Up:022 days 21:03:56
# numbers are '0' padded to fit into appropriate width
def get_system_uptime():
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR   = 60 * SECONDS_PER_MINUTE
    SECONDS_PER_DAY    = 24 * SECONDS_PER_HOUR

    # get current uptime seconds
    with file("/proc/uptime", "r") as uptime_file:
        proc_uptime = uptime_file.readline().split()[:1]
    uptime_secs  = float(proc_uptime[0])

    # compute uptime values
    up_days      = int(uptime_secs  / SECONDS_PER_DAY)
    up_hours     = int((uptime_secs % SECONDS_PER_DAY)  / SECONDS_PER_HOUR)
    up_minutes   = int((uptime_secs % SECONDS_PER_HOUR) / SECONDS_PER_MINUTE)
    up_seconds   = int(uptime_secs  % SECONDS_PER_MINUTE)

    # uptime string
    up_str = "Uptime %03d %02d:%02d:%02d" % (up_days,
                                             up_hours,
                                             up_minutes,
                                             up_seconds)
    
    return up_str

# display the uptime
def display_uptime(lcd):
    uptime_str = get_system_uptime()
    lcd.display_center_string(MACHINE_INFO_SYSTEM_UPTIME_ROW, uptime_str)

    return

# percentage usage in an interval
def percent_usage(delta_use, delta_idle):
    delta_use   = 1.0 * abs(delta_use)
    delta_idle  = 1.0 * abs(delta_idle)
    percent_use = 100.00 * (delta_use)/(delta_use + delta_idle)

    return percent_use


# return the used/idle cpu-values
def get_cpu_usage_stats():
    with file("/proc/stat", "r") as stat_file:
        cpu_val = stat_file.readline().split()[1:5]
        for i in range(len(cpu_val)):
            cpu_val[i] = int(cpu_val[i])
    
    # c[0] == user, c[1] == nice, c[2] == system, c[3] == idle
    return (cpu_val[0]+cpu_val[1]+cpu_val[2], cpu_val[3])


# a genrator returning cpu-usage values...
def cpu_usage_gen():
    old_cpu_usage, old_cpu_idle = 0.0, 0.0
    new_cpu_usage, new_cpu_idle = 0.0, 0.0

    while True:
        new_cpu_usage, new_cpu_idle = get_cpu_usage_stats()
        
        # compute usage
        cpu_usage = percent_usage((new_cpu_usage - old_cpu_usage),
                                  (new_cpu_idle  - old_cpu_idle))
        yield cpu_usage

        # update the values
        old_cpu_usage = new_cpu_usage
        old_cpu_idle  = new_cpu_idle

    return                                               # not-reached


# this function is called to display cpu usage
def display_cpu_usage(lcd, cpu_gen):
    cpu_usage = cpu_gen.next()
    debug_print(DO_DEBUG_PRINT, "CPU-USAGE: %.1f", cpu_usage)
    
    # push some values to the display
    lcd.init_row(MACHINE_INFO_CPU_USAGE_ROW)
    lcd.put_string(MACHINE_INFO_CPU_USAGE_ROW, 0, "%s:%.1f", "CPU", cpu_usage)
    show_usage_meter(lcd, MACHINE_INFO_CPU_USAGE_ROW, 9, 11, cpu_usage)
    lcd.flush_row(MACHINE_INFO_CPU_USAGE_ROW)

    return


# this function is called to display machine specific information on
# the lcd display. 
def display_machine_info(lcd):
    current_iters = 0
    cpu_generator = cpu_usage_gen()

    display_static_machine_info(lcd)
    
    while (current_iters < MACHINE_INFO_MAX_DISPLAY_ITERATIONS):
        # dynamic information
        display_cpu_usage(lcd, cpu_generator)
        display_uptime(lcd)
        
        current_iters = current_iters + 1
        time.sleep(1.0)

    return

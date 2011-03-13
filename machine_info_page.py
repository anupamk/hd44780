import os
import time
import string

from bar_shape import *

def get_custom_shapes():
    return bar_shape_list

# this displays static machine specific information on the lcd
def display_static_machine_info(lcd):
    ROW_0 = 0
    hostname         = string.upper(os.uname()[1])
    base_linux_osver = os.uname()[2].split('-')[0]

    static_info = "%s (%s)" % (hostname, base_linux_osver)
    lcd.display_center_string(ROW_0, static_info)
    
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
    up_str = "Up %03d-%02d:%02d" % (up_days,
                                    up_hours,
                                    up_minutes)
    
    return up_str

# display the uptime
def display_uptime_cpu(lcd, cpu_gen):
    ROW_1, ROW_3      = 1, 3
    cpu_usage         = cpu_gen.next()
    cpu_str           = " CPU %-3d" % (cpu_usage)
    uptime_str        = get_system_uptime()
    USAGE_METER_WIDTH = 20
    
    lcd.display_center_string(ROW_1, uptime_str+cpu_str)
    show_usage_meter(lcd, ROW_3, 0, USAGE_METER_WIDTH, cpu_usage)

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

# this function is called to display machine specific information on
# the lcd display. 
def display_machine_info(lcd_page):
    max_disp_count    = lcd_page.pg_disp_time/lcd_page.refresh_rate
    cur_disp_count    = 0
    lcd_display       = lcd_page.lcd_obj

    # display static content and ...
    cpu_generator = cpu_usage_gen()
    display_static_machine_info(lcd_display)

    # dynamic content as well
    while (cur_disp_count < max_disp_count):
        display_uptime_cpu(lcd_display, cpu_generator)
        
        cur_disp_count = cur_disp_count + 1
        time.sleep(lcd_page.refresh_rate)

    return

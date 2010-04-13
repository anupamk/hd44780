import time
import lcd_func
import lcd_4x20 as display
import utils
import os

# no debugging output
DO_DEBUG_PRINT = False

# useful constants
NAME_DISPLAY_ROW  = 0
CPU_USAGE_ROW     = 2
SYSTEM_UPTIME_ROW = 3

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
    utils.debug_print(DO_DEBUG_PRINT, "CPU-USAGE: %.1f", cpu_usage)
    
    # push some values to the display
    lcd.init_row(CPU_USAGE_ROW)
    lcd.put_string(CPU_USAGE_ROW, 0, "%s:%.1f", "CPU", cpu_usage)
    lcd_func.show_usage_meter(lcd, CPU_USAGE_ROW, 9, 11, cpu_usage)
    lcd.flush_row(CPU_USAGE_ROW)

    return

# this function returns the system uptime in the following format
#    Ad(ays):Bh(ours):Cm(inutes):Ds(econds)
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
    up_str = "UP %3dd %2dh %2dm %2ds" % (up_days,
                                         up_hours,
                                         up_minutes,
                                         up_seconds)
    
    return up_str

# display the uptime
def display_uptime(lcd):
    uptime_str = get_system_uptime()

    # dump the text string
    lcd.init_row(SYSTEM_UPTIME_ROW)
    lcd.put_string(SYSTEM_UPTIME_ROW, 0, "%s", uptime_str)
    lcd.flush_row(SYSTEM_UPTIME_ROW)

    return

# self information
def display_self_info(my_lcd):
    my_lcd.put_string(NAME_DISPLAY_ROW,   0, "%s", "   ANUPAM KAPOOR   ")
    my_lcd.put_string(NAME_DISPLAY_ROW+1, 0, "%s", " STARENT NETWORKS  ")
    my_lcd.flush_row(NAME_DISPLAY_ROW)
    my_lcd.flush_row(NAME_DISPLAY_ROW+1)

    return
        
# reset the lcd display
def initialize_lcd(my_lcd):
    my_lcd.initialize()
    lcd_func.load_cust_shapes(my_lcd)

    return

# run it all
def run_main():
    cpu_gen = cpu_usage_gen()

    # setup the display
    my_lcd  = display.lcd_4x20()                        # current-lcd
    initialize_lcd(my_lcd)

    display_self_info(my_lcd)
    
    # deamonize this...
    while True:
        time.sleep(1.0)

        # display various stuff
        display_cpu_usage(my_lcd, cpu_gen)
        display_uptime(my_lcd)
        


import time
import lcd_func
import lcd_4x20 as display
import utils
import os

# no debugging output
DO_DEBUG_PRINT = False

# useful constants
NAME_DISPLAY_ROW   = 0
CPU_USGAGE_ROW     = 2
SYSTEM_UPTIME_ROW  = 3

# return the used/idle cpu-values
def get_cpu_usage_stats():
    with file("/proc/stat", "r") as stat_file:
        cpu_val = stat_file.readline().split()[1:5]
        for i in range(len(cpu_val)):
            cpu_val[i] = int(cpu_val[i])
    
    # c[0] == user, c[1] == nice, c[2] == system, c[3] == idle
    return (cpu_val[0]+cpu_val[1]+cpu_val[2], cpu_val[3])

# percentage usage in an interval
def compute_cpu_usage(old_cpu_usage, new_cpu_usage):
    delta_usage = 1.0 * abs(new_cpu_usage[0] - old_cpu_usage[0])
    delta_idle  = 1.0 * abs(new_cpu_usage[1] - old_cpu_usage[1])
    usage       = 100.00 * (delta_usage)/(delta_usage + delta_idle)

    return usage

# this function is called to display cpu usage
def display_cpu_usage(lcd, old_usage, new_usage):
    
    (new_usage[0], new_usage[1]) = get_cpu_usage_stats()
    cpu_usage = compute_cpu_usage(old_usage, new_usage)

    utils.debug_print(DO_DEBUG_PRINT, "CPU-USAGE: %.1f", cpu_usage)
    
    # push some values
    lcd.init_row(CPU_USGAGE_ROW)
    
    lcd.put_string(CPU_USGAGE_ROW, 0, "%s:%.1f", "CPU", cpu_usage)
    lcd_func.show_usage_meter(lcd, CPU_USGAGE_ROW, 9, 11, cpu_usage)
    
    lcd.flush_row(CPU_USGAGE_ROW)

    # update values
    (old_usage[0], old_usage[1]) = (new_usage[0], new_usage[1])

    return

# this function returns the system uptime in the following format
#    Ad(ays):Bh(ours):Cm(inutes)
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
    
        
# reset the lcd display
def reset_lcd(my_lcd):
    my_lcd.initialize()
    lcd_func.load_cust_shapes(my_lcd)
    my_lcd.put_string(NAME_DISPLAY_ROW, 0, "%s", "   ANUPAM KAPOOR   ")
    my_lcd.put_string(NAME_DISPLAY_ROW+1, 0, "%s", " STARENT NETWORKS  ")
    my_lcd.flush_row(NAME_DISPLAY_ROW)
    my_lcd.flush_row(NAME_DISPLAY_ROW+1)

    return

# run it all
def run_main():
    num_itr = 0
    old_cpu = [0.0, 0.0]                                # [used, idle]
    new_cpu = [0.0, 0.0]                                # [used, idle]

    # setup the display
    my_lcd  = display.lcd_4x20()                        # current-lcd
    reset_lcd(my_lcd)

    # collect old values
    (old_cpu[0], old_cpu[1]) = get_cpu_usage_stats()
    
    # deamonize this...
    while True:
        num_itr = num_itr + 1
        time.sleep(1.0)

        # display various stuff
        display_cpu_usage(my_lcd, old_cpu, new_cpu)
        display_uptime(my_lcd)
        


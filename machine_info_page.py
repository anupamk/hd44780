import os
import time
import string

import slim_bar_shape as slim_bar

def get_custom_shapes():
    return slim_bar.shape_list

# this displays static machine specific information on the lcd
def display_static_machine_info(lcd):
    os_info = os.uname()
    
    osname  = os_info[0]
    osver   = os_info[2].split('-')[0]

    static_info = "%s (%s)" % (osname, osver)
    lcd.display_center_string(row = 0, display_str = static_info)
    
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
    up_str = "Uptime %03d:%02d:%02d:%02d" % (up_days,
                                             up_hours,
                                             up_minutes,
                                             up_seconds)
    
    return up_str

# this function returns the current system load
def get_percent_cpu_load():
    cpu_current_load = os.getloadavg()[0]

    # cap it at a maximum
    if cpu_current_load >= 1.0:
        cpu_current_load = 1.0
    
    return 100.00 * cpu_current_load

def get_current_procs():
    all_pids = [int(x) for x in os.listdir('/proc') if x.isdigit()]

    # kernel process
    all_pids.insert(0, 0)
    
    return len(all_pids)

# display the uptime
def display_uptime_cpu(lcd):
    cpu_usage           = get_percent_cpu_load()
    cpu_str             = "CPU %4.2f" % (cpu_usage)
    uptime_str          = get_system_uptime()
    lcd_rows, lcd_cols  = lcd.dimensions()
    num_processes       = get_current_procs()
    num_processes_str   = " Proc:%3d" % (num_processes)

    if cpu_usage >= 100.0:
        cpu_str = " CPU %4.0f" % (cpu_usage)
    if cpu_usage >= 10.0:
        cpu_str = " CPU %4.1f" % (cpu_usage)

    # cpu-usage + processes
    cpu_str = cpu_str + num_processes_str

    # display the lot
    lcd.display_center_string(row = 1, display_str = uptime_str)
    lcd.display_center_string(row = 2, display_str = cpu_str)
    slim_bar.show_usage_meter(lcd, row = 3, col = 0, bar_width = lcd_cols, usage_val = cpu_usage)

    return

# this function is called to display machine specific information on
# the lcd display. 
def display_machine_info(lcd_page):
    max_disp_count    = lcd_page.pg_disp_time/lcd_page.refresh_rate
    cur_disp_count    = 0
    lcd_display       = lcd_page.lcd_obj

    # load the custom shapes required for this page
    lcd_display.load_custom_shapes(get_custom_shapes())
    
    # display static content and ...
    display_static_machine_info(lcd_display)

    # dynamic content as well
    while (cur_disp_count < max_disp_count):
        display_uptime_cpu(lcd_display)
        
        cur_disp_count = cur_disp_count + 1
        time.sleep(lcd_page.refresh_rate)

    return

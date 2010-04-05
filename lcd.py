import time
import lcd_func
import lcd_4x20 as display

# useful constants
NAME_DISPLAY_ROW = 1
CPU_USGAGE_ROW   = 2

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

    lcd.str_printf(CPU_USGAGE_ROW,5, "%s:%.1f", "CPU", cpu_usage)
    lcd.flush()

    # update values
    (old_usage[0], old_usage[1]) = (new_usage[0], new_usage[1])

    return

# initialize lcd device
def init_lcd_dev(my_lcd):
    my_lcd.initialize()
    lcd_func.load_custom_shapes(my_lcd)

    return

# run it all
def run_main():
    old_cpu = [0.0, 0.0]                                # [used, idle]
    new_cpu = [0.0, 0.0]                                # [used, idle]
    my_lcd  = display.lcd_4x20()                        # current-lcd

    init_lcd_dev(my_lcd)

    # collect old values
    (old_cpu[0], old_cpu[1]) = get_cpu_usage_stats()

    my_lcd.str_printf(NAME_DISPLAY_ROW, 1, "%s", "ANUPAM KAPOOR !")
    my_lcd.flush()
    
    # # deamonize this...
    while True:
        time.sleep(2)
        display_cpu_usage(my_lcd, old_cpu, new_cpu)

        
        

        

    

import time

# this displays static machine specific information on the lcd
def show_personal_info(lcd):
    lcd.display_center_string(0, "Anupam Kapoor")
    lcd.display_center_string(1, "Cisco Systems")
    lcd.display_center_string(2, "akapoor@cisco.com")
    lcd.display_center_string(3, "966-501-7891")
    
    return

# this function is called to display personal information on the lcd display.
def display_personal_info(lcd_page):
    max_disp_count = lcd_page.pg_disp_time/lcd_page.refresh_rate
    cur_disp_count = 0

    # static information
    show_personal_info(lcd_page.lcd_obj)

    while (cur_disp_count < max_disp_count):
        show_personal_info(lcd_page.lcd_obj)
        
        cur_disp_count = cur_disp_count + 1
        time.sleep(lcd_page.refresh_rate)
    
    return
    

import time

from utils import *
from bar_shape import *

PERSONAL_INFO_MAX_DISPLAY_ITERATIONS = 30
PERSONAL_INFO_NAME_DISPLAY_ROW       = 0
PERSONAL_INFO_COMP_DISPLAY_ROW       = 1
PERSONAL_INFO_EMAIL_DISPLAY_ROW      = 2
PERSONAL_INFO_PHONE_DISPLAY_ROW      = 3

# interface into external world
def get_name():
    return "Personal Info"

def get_custom_shapes():
    return None

def get_display_func():
    return display_personal_info

# this displays static machine specific information on the lcd
def show_personal_info(lcd):
    lcd.display_center_string(PERSONAL_INFO_NAME_DISPLAY_ROW,  "Anupam Kapoor")
    lcd.display_center_string(PERSONAL_INFO_COMP_DISPLAY_ROW,  "Cisco Systems")
    lcd.display_center_string(PERSONAL_INFO_EMAIL_DISPLAY_ROW, "akapoor@cisco.com")
    lcd.display_center_string(PERSONAL_INFO_PHONE_DISPLAY_ROW, "966-501-7891")
    
    return

def display_personal_info(lcd):
    current_iters = 0

    show_personal_info(lcd)

    while (current_iters < PERSONAL_INFO_MAX_DISPLAY_ITERATIONS):
        current_iters = current_iters + 1
        time.sleep(1)
        show_personal_info(lcd)

    return
    

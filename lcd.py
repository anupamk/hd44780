import lcd_4x20 as display
from lcd_page import *
import machine_info_page as machine_info
import personal_info_page as personal_info

# setup a bunch of pages to display on the lcd
def setup_lcd_pages(lcd):
    pages = []

    # create a bunch of pages
    page_1 = lcd_page(machine_info.get_name(),
                      machine_info.get_display_func(),
                      machine_info.get_custom_shapes(),
                      lcd)

    page_2 = lcd_page(personal_info.get_name(),
                      personal_info.get_display_func(),
                      personal_info.get_custom_shapes(),
                      lcd)

    # add them to the page-list to be displayed
    pages.append(page_1)
    pages.append(page_2)

    return pages

# the main thing
def run_main():
    this_lcd  = display.lcd_4x20()
    lcd_pages = setup_lcd_pages(this_lcd)

    while True:
        for pg in lcd_pages:
            pg.initialize()
            pg.display()

    return

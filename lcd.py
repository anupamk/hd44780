import lcd_4x20 as display
from lcd_page import *
import machine_info_page as machine_info
import personal_info_page as personal_info

# setup a bunch of pages to display on the lcd
def setup_lcd_pages(lcd):
    pages = []

    # create a bunch of pages
    page_1 = lcd_page(lcd,
                      "Machine Info",                           # page-name
                      machine_info.display_machine_info)        # display-function

    page_2 = lcd_page(lcd,
                      "Personal Info",                          # page-name
                      personal_info.display_personal_info)      # display-function

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
            pg.show()

    return

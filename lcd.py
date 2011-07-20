import lcd_4x20 as display
from lcd_page import *

# page-display specific functions
import machine_info_page as machine_info
import personal_info_page as personal_info
import stock_info_page as stock_info

# setup a bunch of pages to display on the lcd
def setup_lcd_pages(lcd):
    pages = []

    # create a bunch of pages
    page_1 = lcd_page(lcd,
                      "Machine Info",                           # page-name
                      machine_info.display_machine_info)        # display-function

    page_2 = lcd_page(lcd,
                      "Personal Info",                          # page-name
                      personal_info.display_personal_info,      # display-function
                      total_duration = 15.0)

    page_3 = lcd_page(lcd,
                      "Stock Info",                             # page-name
                      stock_info.display_stock_info,            # display-function
                      total_duration = 15.0,                    # show for 15 seconds total
                      refresh_rate   = 3.0)                     # and update every 3 seconds


    # add them to the page-list to be displayed
    pages.append(page_1)
    pages.append(page_2)
    pages.append(page_3)

    return pages

# the main thing
def run_main():
    this_lcd  = display.lcd_4x20()
    lcd_pages = setup_lcd_pages(this_lcd)

    while True:
        for pg in lcd_pages:
            print "now showing: '%s'" % (pg.name)
            pg.show()

    return

if __name__ == '__main__':
    run_main()

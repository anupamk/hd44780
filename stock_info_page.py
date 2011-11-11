import time
from stock_ticker import *

# list of stocks that we are interested in monitoring
stock_tickers = []

def init_stock_list(stock_names):
    for stk_sym in stock_names:
        stock_tickers.append(stock_ticker(stk_sym))

    return

# update the ticker with latest information
def update_stock_tickers():
    for s in stock_tickers:
        s.get_price()

    return

# 
# return a list of strings with latest ticker price in the following format:
#     <stock-symbol-name> : <price>
# 
def get_ticker_info():
    ticker_info = []
    for s in stock_tickers:
        s_info = "%s : %4.2f" % (s.name, s.last_value)
        ticker_info.append(s_info)

    return ticker_info
        

# 
# finally show this on the display
#
def show_stock_info(lcd):
    row_num = 2
    update_stock_tickers()                                      # fetch latest info
    price_list = get_ticker_info()

    for p in price_list:
        lcd.display_center_string(row_num, p)
        row_num = row_num + 1

    return

def setup_stock_info_pg(lcd):
    lcd.display_center_string(row = 0, display_str = "Stock Quotes")
    lcd.display_center_string(row = 1, display_str = "")
    lcd.display_center_string(row = 2, display_str = "")
    lcd.display_center_string(row = 3, display_str = "")

    return

# periodically display stock information
def display_stock_info(lcd_page):
    lcd_display      = lcd_page.lcd_obj
    monitored_stocks = ["CSCO", "JNPR"]

    num_displays = lcd_page.pg_disp_time/lcd_page.refresh_rate
    i = 0

    if len(stock_tickers) == 0:
        init_stock_list(monitored_stocks)
        
    setup_stock_info_pg(lcd_display)
    
    while (i < num_displays):
        show_stock_info(lcd_display)

        i = i+1
        time.sleep(lcd_page.refresh_rate)

    return

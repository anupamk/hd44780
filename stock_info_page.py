import time
import yahoo_stock_quote as stock_quote

# this function is called to return the price of
# stock-symbol
def get_stock_price(stock_sym):
    price = stock_quote.request_quote(stock_sym, ["PRICE"])
    stock_price_str = "%s : %s" % (stock_sym, price[0][1])

    return stock_price_str

# this function is called to periodically display current
# stock price of a bunch of companies
def show_stock_info(lcd):
    csco_price = get_stock_price("CSCO")
    jnpr_price = get_stock_price("JNPR")

    lcd.display_string([2, 0], ("%s", csco_price))
    lcd.display_string([3, 0], ("%s", jnpr_price))

    return

def display_static_stock_info(lcd):
    lcd.display_center_string(row = 0, display_str = "Stock Quotes")
    lcd.display_center_string(row = 1, display_str = "")
    lcd.display_center_string(row = 2, display_str = "")
    lcd.display_center_string(row = 3, display_str = "")

    return

# periodically display stock information
def display_stock_info(lcd_page):
    max_disp_count = lcd_page.pg_disp_time/lcd_page.refresh_rate
    cur_disp_count = 0
    lcd_display    = lcd_page.lcd_obj

    display_static_stock_info(lcd_display)
    
    while (cur_disp_count < max_disp_count):
        show_stock_info(lcd_display)
        
        cur_disp_count = cur_disp_count + 1
        time.sleep(lcd_page.refresh_rate)

    return

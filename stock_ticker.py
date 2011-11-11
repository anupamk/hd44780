import yahoo_stock_quote as stock_quote

# a trivial class abstracting stock-ticker madness.
class stock_ticker(object):
    def __init__(self, name):
        self.name       = name
        self.last_value = 0.0
        
        return

    # return the price of the ticker. on failure, return last known good
    # value. i think, it be better to return 'last-value' when markets are
    # closed as well...
    def get_price(self):
        try:
            price_attr_val  = stock_quote.request_quote(self.name, ["PRICE"])
            price           = float(price_attr_val[0][1])
            self.last_value = price
        except:
            price = self.last_value

        return price


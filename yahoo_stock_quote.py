import urllib
import time

YAHOO_STOCK_QUERY_URL_STRING = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s"


# this table provides a mapping between information what we are requesting
# e.g. AVG_DAILY_VOL and actual suffix that needs to be
# provided as part of the query-string to finance.yahoo.com
# 
# For example, for getting the current 'PRICE' of a symbol e.g. 'CSCO' we need
# to have this:
#                 http://finance.yahoo.com/d/quotes.csv?s='CSCO'&f='l1'
INFONAME_TO_CSV_TABLE = {
    'PRICE'                   : 'l1',
    'CHANGE'                  : 'c1',
    'VOLUME'                  : 'v' ,
    'AVG_DAILY_VOL'           : 'a2',
    'STOCK_EXCHANGE'          : 'x' ,
    'MARKET_CAP'              : 'j1',
    'BOOK_VALUE'              : 'b4',
    'EBITDA'                  : 'j4',
    'DIVIDEND_PER_SHARE'      : 'd' ,
    'DIVIDEND_YIELD'          : 'y' ,
    'EARNINGS_PER_SHARE'      : 'e' ,
    '52_WEEK_HIGH'            : 'k' ,
    '50_DAY_MOVING_AVERAGE'   : 'm3',
    '200_DAY_MOVING_AVERAGE'  : 'm4',
    'PRICE_EARNINGS_RATIO'    : 'r' ,
    'PRICE_EARNINGS_GROWTH'   : 'r5',
    'PRICE_SALES_RATIO'       : 'p5',
    'PRICE_BOOK_RATION'       : 'p6', 
    'SHORT_RATIO'             : 's7',
    }

# return 'csv' string-list from a list of requested infoname
# items. 
def get_query_string_from_info_list(info_list):
    query_str = ""
    
    for info in info_list:
        try:
            csv = INFONAME_TO_CSV_TABLE[info]
            query_str = query_str + csv
        except KeyError:
            print "Requesting unknown INFONAME: '%s'" % (info)

    return query_str

# return a tuple of ('info-name', value) corresponding to a 
# stock-symbol.
def request_quote(stock_sym, info_list):
    query_str = get_query_string_from_info_list(info_list)
    
    url = YAHOO_STOCK_QUERY_URL_STRING % (stock_sym, query_str)
    val = urllib.urlopen(url).read().strip().strip('"').split(',')

    stock_info = zip(info_list, val)
    
    return stock_info

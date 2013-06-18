import urllib
import re
import time

def get_smartquote(symbol):
    base_url = 'http://markets.smartstocks.com/smartstocks./quote?Symbol='
    content = urllib.urlopen(base_url + symbol).read()
    m = re.search('id="quotenav1_field_price">(.*?)<', content)
    if m:
        quote = m.group(1)
    else:
        quote = 'no quote available for: ' + symbol
    return quote
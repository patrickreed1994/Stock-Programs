import urllib
import re
import time

def get_percent(symbol):
	base_url = 'http://www.google.com/finance?q='
	content = urllib.urlopen(base_url + symbol).read()
	m = re.search('id="ref_.*?_cp".*?>(.*?)<', content)
	if m:
		quote = m.group(1)
		quote = quote.strip('(')
		quote = quote.strip(')')
		quote = quote.strip('%')
		if '-' in quote:
			quote = quote.strip('-')
			quote = 0 - float(quote)
	else:
		quote = 'stock: ' + symbol + " doesn't appear"
	return quote
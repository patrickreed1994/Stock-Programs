import urllib
import re
import time

def get_smartprcnt(symbol):
	base_url = 'http://markets.smartstocks.com/smartstocks/quote/detailedquote?Symbol='
	content = urllib.urlopen(base_url + symbol).read()
	m = re.search('tive">' + ('+' or '-') + '(.*?)' + '%', content)
	if m:
		quote = m.group(1)
		if '+' in quote:
			quote = quote.strip('+')
		if '-' in quote:
			quote = quote.strip('-')
			quote = 0 - float(quote)
		quote = float(quote)
	else:
		quote = 'No quote available for: ' + symbol
	return quote
from get_googlestock import get_quote
from get_googlepercent import get_percent
from get_smartstock import get_smartquote
from get_smartpercent import get_smartprcnt
from get_topfive import get_topfive
import urllib
import time
import re

def calc_leverage(a):
	google_percent = float(get_percent(a))
	smart_percent = float(get_smartprcnt(a))
	leverage = google_percent - smart_percent
	if leverage > 3:
		return (a, leverage, 'DO IT. NOW.')
	if 2.99 > leverage > 2:
		return (a, leverage, 'Definite Must')
	if 1.99 > leverage > 1:
		return (a, leverage, 'Go for it')
	if 0 > leverage > .99:
		return (a, leverage, 'Pass')
	if leverage == 0:
		return (a, leverage, 'Nothing there')
	if leverage < 0:
		return (a, leverage, 'Sell')
		
print calc_leverage('cmkm')
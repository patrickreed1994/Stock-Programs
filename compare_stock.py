from get_stock import get_quote
import urllib
import re
import time

def compare_stock(a,b):
	stock_a = get_quote(a)
	stock_b = get_quote(b)
	diff = float(stock_a) - float(stock_b)
	return (a + "(" + stock_a + ")" + " is " + str(diff) + " a share against " + b + "(" + stock_b + ")")

from recommendation import rec
import urllib
import time
import re

def update(total, a):
	for iter in range(total):
		for number in range(len(a)):
			print time.strftime("%H:%M:%S"), iter, rec(a[number])
		time.sleep(10)
	
print update(10, ['aapl', 'adbe', 'driv', 'gff', 'goog', 'ibm', 'ioc', 'ixc', 'mstr', 'nls', 'ogzpy', 'sbr'])
from recommendation import rec
import urllib
import time
import re

def update(total, a):
	for iter in range(total):
		for number in range(len(a)):
			print time.strftime("%H:%M:%S"), iter, rec(a[number])
		time.sleep(10)

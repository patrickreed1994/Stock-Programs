import urllib
import re
import time

def get_topfive():
	basic_url = 'http://www.google.com/finance?hl=en&tab=ee'
	content = urllib.urlopen(basic_url).read()
	m = re.findall('title=' + '"' + '(.*?)' + '"' + ' >', content)
	topfive = []
	if m:
		totallist = m
		for i in range(5):
			topfive.append(totallist[i])
	else:
		topfive = 'Done fucked up'
	return topfive
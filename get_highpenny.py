import urllib
import re
import time

def get_highpenny():
	base_url = 'http://www.advfn.com/pinksheets'
	content = urllib.urlopen(base_url).read()
	m = re.findall("pid=qkquote&symbol=NO%5E(.*?)'",content)
	highpennies = []
	others = []
	if m:
		for i in range(len(m)):
			if i <= 23:
				others.append(m[i])
			if 36 > i > 23:
				highpennies.append(m[i])
	return highpennies

def update():
	for i in range(20):
		time.sleep(30)
		stocktime = time.strftime("%H:%M:%S +0000", time.localtime())
		print stocktime, get_highpenny()
	
print update()
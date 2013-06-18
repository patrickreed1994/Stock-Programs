import urllib
import re
import time

def get_highest():
	base_url = 'http://www.marketwatch.com/tools/stockresearch/screener/afterhours.asp?count=25&skip=0&sort=53&sortd=0'
	content = urllib.urlopen(base_url).read()
	m = re.findall('class="lk01">' + '(.*?)' + '</a></td>', content)
	highestlist = []
	if m:
		for i in range(len(m)):
			if len(m[i]) < 6:
				highestlist.append(m[i])
	return highestlist
	
print get_highest()
import urllib
import urllib.request
import http.cookiejar
import re

req = urllib.request.Request("https://www.hulu.com/browse/movies", headers={'User Agent' : "Magic Browser"})
html = str(urllib.request.urlopen(req).read())

results = re.findall(r'<a href[^<]*?\(this\);">(.*?)</a>',html)

for result in results:
	print (result)
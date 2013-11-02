import urllib
import http.cookiejar
import re

jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

search = 'the+office'
html = str(opener.open('https://signup.netflix.com/Search?v1='+search).read())

results = re.findall(r'<section class="movie-result agMovie">.*?</section>',html)

for result in results:

	title = re.search(r'alt="(.*?)"',result).group(1)
	print ('Title:',title)

	movieID = re.search(r'data-movieid="(.*?)"',result).group(1)
	print ('Movie ID:',movieID)

	link = re.search(r'href="(.*?)"',result).group(1)
	print ('Link:',link)

	image = re.search(r'src="(.*?)"',result).group(1)
	print ('Image:',image)

	time = re.search(r'<time class="mdp-date">(.*?)</time>',result).group(1)
	print ('Time:',time)

	span = re.search(r'<span class="mdp-season">(.*?)</span>',result)
	if (span is not None):
		print ('Span:',span.group(1))

	print()
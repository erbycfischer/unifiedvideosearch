import urllib.request
import http.cookiejar
import re

class NetflixParser(Parser):

	def search(self, movie):
		jar = http.cookiejar.CookieJar()
		opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

		html = str(opener.open('https://signup.netflix.com/Search?v1='+movie).read())

		results = re.findall(r'<section class="movie-result agMovie">.*?</section>',html)

		videos = []
		for result in results:
			title = re.search(r'alt="(.*?)"',result).group(1)
			movieID = re.search(r'data-movieid="(.*?)"',result).group(1)
			link = re.search(r'href="(.*?)"',result).group(1)
			image = re.search(r'src="(.*?)"',result).group(1)
			time = re.search(r'<time class="mdp-date">(.*?)</time>',result).group(1)
			span = re.search(r'<span class="mdp-season">(.*?)</span>',result)

			videos.append({title: [movieID, link, image, time, span.group(1)]})

		return videos

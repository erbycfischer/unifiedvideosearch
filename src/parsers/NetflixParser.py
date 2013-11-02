import Parser
import urllib
import http.cookiejar
from lxml import html

class NetflixParser(Parser):

	def search(self, movie):

		movie =  movie.strip()
		movie = movie.replace(" ", "+")

		jar = http.cookiejar.CookieJar()
		opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

		source = opener.open('https://signup.netflix.com/Search?v1='+movie).read()

		doc = html.fromstring(source)

		videos = []
		for el in doc.get_element_by_id("search-resultlist"):
			tag = el.find_class("mdpLink")[1]
			title = tag.text
			movieID = tag.get("data-movieid")
			link = tag.get("href")
			time = el.find_class("mdp-date")[0].text
			spantag = el.find_class("mdp-season")
			span = None
			if len(spantag):
				span = spantag[0].text

			videos.append({title: [movieID, link, time, span]})

		return videos

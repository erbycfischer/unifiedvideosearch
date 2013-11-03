from Parser import *

import urllib
import http.cookiejar
from lxml import html

class HitBlissParser(Parser):

	def __init__(self):
		pass

	def search(self, query):

		query =  query.strip()
		query = query.replace(" ", "%20")

		req = urllib.request.Request('http://www.hitbliss.com/search?srch='+query, headers={'User Agent' : "Magic Browser"})
		source = urllib.request.urlopen(req).read()

		doc = html.fromstring(source)

		videos = []
		catalog = doc.find_class("catalog")
		if len(catalog):
			for item in catalog[0].iterfind(".//li"):
				tag = item.find("a")
				title = tag.get("title")
				link = "http://www.hitbliss.com"+tag.get("href")
				image = item.find(".//img").get("src")
				videos.append((title, [link, image]))

		return videos
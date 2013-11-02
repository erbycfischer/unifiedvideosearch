from Parser import *

import urllib
import http.cookiejar
from lxml import etree

class CrackleParser(Parser):

	def search(self, query):

		results = []

		query =  query.strip()
		query = query.replace(" ", "%20")


		jar = http.cookiejar.CookieJar()
		opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

		source = opener.open("http://api.crackle.com/Service.svc/search/all/"+query+"/US?format=xml").read()

		root = etree.XML(source)
		tree = etree.ElementTree(root)
		for item in root.iterfind(".//CrackleItem"):
			if item.find("ClipsOnly").text == "false":
				title = item.find("Title").text
				description = item.find("Description").text
				genre = item.find("Genre").text
				rating = item.find("Rating").text
				duration = item.find("Duration").text
				link = "http://www.crackle.com/c/"+title.strip().replace(" ","-")

				results.append((title, [description, link, genre, rating, duration, link]))
		
		return results
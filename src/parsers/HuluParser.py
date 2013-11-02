from Parser import *

import urllib
import http.cookiejar
from lxml import html
import re

class HuluParser(Parser):

	videos = []


	def get_videos(self):

		self.videos = []

		req = urllib.request.Request("https://www.hulu.com/browse/tv", headers={'User Agent' : "Magic Browser"})
		source = urllib.request.urlopen(req).read()

		doc = html.fromstring(source)

		for el in doc.get_element_by_id("show_list_hiden"):
			tag = el.find_class("beaconid")[0]
			title = tag.text
			link = tag.get("href")
			movieID = tag.get("beaconid")

			self.videos.append((title, [movieID, link, "tv"]))

		req = urllib.request.Request("https://www.hulu.com/browse/movies", headers={'User Agent' : "Magic Browser"})
		source = urllib.request.urlopen(req).read()

		doc = html.fromstring(source)

		for el in doc.get_element_by_id("show_list_hiden"):
			tag = el.find_class("beaconid")[0]
			title = tag.text
			link = tag.get("href")
			movieID = tag.get("beaconid")

			self.videos.append((title, [movieID, link, "movie"]))


	def search(self, query):
		results = []

		for video in self.videos:
			if (re.search(query, video[0], re.IGNORECASE)):
				results.append(video)
		return results

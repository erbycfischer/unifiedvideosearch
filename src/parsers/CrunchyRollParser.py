from Parser import *

import urllib
import http.cookiejar
from lxml import html
import re

class CrunchyRollParser(Parser):

	def __init__(self):
		self.videos = []

	def get_videos(self):

		req = urllib.request.Request('http://www.crunchyroll.com/videos/anime/alpha?group=all', headers={'User Agent' : "Magic Browser"})
		source = urllib.request.urlopen(req).read()
		doc = html.fromstring(source)

		for item in doc.find_class("hover-bubble group-item"):
			tag = item.find("a")
			title = tag.text.strip()
			link = "http://www.crunchyroll.com"+tag.get("href")
			self.videos.append((title, link))

	def search(self, query):
		results = []

		for video in self.videos:
			if (re.search(query, video[0], re.IGNORECASE)):
				results.append(video)
		return results
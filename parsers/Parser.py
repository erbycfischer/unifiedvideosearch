class Parser(object):

def get_videos(self):
	pass

def search(self, video):
	pass

def add_to_redis(self, redis_instance):
	videos = get_videos()
	for movie in videos.keys():
		redis_instance.set(movie, {self.__class__.__name__, videos[movie]})


		

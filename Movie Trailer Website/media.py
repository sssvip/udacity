# coding:utf-8
' the center of media class'
__author__ = 'David West : admin@dxscx.com'

#define the abstract class video
class Video:
	def __init__(self,title):
		self.title=title

#define the child class Movie
class Movie(Video):
	def __init__(self,title,poster_image_url,trailer_youtube_url):
		Video.__init__(self,title)
		self.poster_image_url=poster_image_url #movie image url
		self.trailer_youtube_url=trailer_youtube_url #movie youtube url
	#using test inherit
	def show_info(self):
		print(self.title)


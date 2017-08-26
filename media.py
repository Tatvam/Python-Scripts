#!/usr/bin/python -tt
import webbrowser

class Movie():
	def __init__( self, movie_title, storyline, image, turl):
		self.title=movie_title
		self.storyline=storyline
		self.poster_image_url=image
		self.trailer_youtube_url=turl
	def trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class Movie:
	""" Movie class docstring

	This class is used to create an object to store movie related information

	Attributes:
		title - String to store movie title.
		movie_description - String to store movie description.
		poster_image_url - String to store URL of movie's poster.
		trailer_youtube_url - String to store youtube URL of movie's trailer.
		
	"""
	def __init__(self, title, movie_description, poster_image_url, trailer_youtube_url):
		self.title = title
		self.movie_description = movie_description
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
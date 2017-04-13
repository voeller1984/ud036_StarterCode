class Movie():
        """this class allows storing information about my favourite movies"""
        def __init__(self, movie_title, movie_picture, movie_video):
                '''assign variables in the constructor function'''
                self.title = movie_title
                self.poster_image_url = movie_picture
                self.trailer_youtube_url = movie_video

""" Defines the Movie class that contains the details of a movie."""
import webbrowser
import turtle

class Movie ():
    """This class provides a way to save and store movies trailers

Attributes:
        title: A string to store the title of movies.
        storyline: A string to store the basic plot of movies.
        poster: A string to store the URL images
        trailer: string to store the URL movie links"""
    

    def __init__ (self, movie_title, movie_storyline, \
                  poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline 
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

""" reatings: show ratings"""
VALID_RATINGS = ["G",
                        "PG",
                        "PG-13",
                        "R"]


def show_trailer (self):
    webbrowser.open(self.trailer_youtube_url)
    """ plays the movie trailer in the web browser."""


def draw_square ():
    window.exitonclick ()
    """ shows box line in the web browser."""

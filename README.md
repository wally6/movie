Project : Movie Trailer Website

What it is and does:
Python script to run and store a list of your favorite movies, including box art, movie trailer URL, & generates webpage for showing movie 
info and trailers.

Class Movie: param1 function with E501 
inputs: self.title = movie_title
        self.storyline = movie_storyline 
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

VALID_RATINGS = ["G",
                "PG",
                "PG-13",
                "R"]

def show_trailer (self):
    webbrowser.open(self.trailer_youtube_url)

def draw_square ():
    window.exitonclick ()


File List
media.py module

contains class Movie definition used for creating instances of movies.

Prjoect contents:
movie.py File code

contains intances of class Movie used in website.

fresh_tomatoes.py (File Code

contains script for genrating webpage using instances of movies.

fresh_tomatoes.open_movies_page(movies)

where movies is list of instances of class Movie.

How to Run Project

Download the project zip file to you computer and unzip the file. Or clone this repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal window in Linux, the command prompt in Windows).

Navigate to the project directory and type in the following command:

python entertainment_center.py

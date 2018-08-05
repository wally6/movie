import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

wreck_it_ralph_2 = media.Movie("Wreck it Ralph",
                               "A story of acrade game player breaking the internet",
                               "https://en.wikipedia.org/wiki/Ralph_Breaks_the_Internet#/media/File:Ralph_Breaks_the_Internet_poster.jpg",
                               "https://www.youtube.com/watch?v=KHQhp2cGZtE")

movies = [toy_story, acatar, wreck_it_ralph_2]
fresh_tomatoes.open_movies_page (movies)

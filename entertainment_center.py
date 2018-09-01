import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")


venom = media.Movie("Venom",
                    "Reporter Eddie Brock develops superpowers after becoming a host to an alien parasite.",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcT1wbV7jcFXm3f8sKbZx_bruPB_w75w0FwBDLEA52DcbI2hRr3k",
                    "https://www.youtube.com/watch?v=zX81KEqzy_M")



movies = [toy_story, avatar, venom]
fresh_tomatoes.open_movies_page (movies)

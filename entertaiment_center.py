import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life.",
                        "https://images-na.ssl-images-amazon.com/images/I/71iSIVGZQUL._AC_SL1024_.jpg",
                        "https://www.youtube.com/watch?v=CxwTLktovTU")

# print(toy_story.storyline)
# toy_story.show_trailer()

avatar = media.Movie( "Avatar",
                       "A marine on an alien planet.",
                       "https://danhairfield.files.wordpress.com/2011/02/avatar-movie-poster.jpg",
                       "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)

batman = media.Movie("Batman Begins",
                        "A man that flies at night. ",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Batman_Begins_Poster.jpg/220px-Batman_Begins_Poster.jpg",
                        "https://www.youtube.com/watch?v=qHhHIbNuok8")

# print(batman.storyline)
# batman.show_trailer()                   
#
school_of_rock = media.Movie("School of Rock",
                            "A man with a group of children that rocks.",
                            "http://www.impawards.com/2003/posters/school_of_rock_verdvd.jpg",
                            "https://www.youtube.com/watch?v=TExoc0MG4I4")    

wall_e = media.Movie("WALL•E",
                    "A robot that falls in love",
                    "https://animatedkid.files.wordpress.com/2016/10/wall-eposter.jpg",
                    "https://www.youtube.com/watch?v=alIq_wG9FNk")

raging_bull = media.Movie("Raging Bull",
                        "A man that boxing",
                        "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQFyUVhNLyO8Nq1n3humvYykzsKYEVWlhU8zOHDWo61wwk_Z3XN",
                        "https://www.youtube.com/watch?v=yUp6d79WRVI")

movies = [toy_story, avatar, batman, school_of_rock,wall_e, raging_bull]

fresh_tomatoes.open_movies_page(movies)

# print(avatar.VALID_RATINGS)
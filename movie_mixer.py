import mediatek
import fresh_tomatoes

shawshank_redemption=mediatek.Movie("the Shawshank Redemption",
                                    "http://pics.filmaffinity.com/the_shawshank_redemption-576140557-large.jpg",
                                    "https://www.youtube.com/watch?v=6hB3S9bIaco")

godfather_2 = mediatek.Movie("The Godfather: Part II",
                             "http://static.rogerebert.com/uploads/movie/movie_poster/the-godfather-part-ii-1974/large_tHbMIIF51rguMNSastqoQwR0sBs.jpg",
                             "https://www.youtube.com/watch?v=qJr92K_hKl0")

twelve_angry_men= mediatek.Movie("12 Angry mMen",
                                 "http://4.bp.blogspot.com/-qr5hN-DsX4w/Vley1RMQk0I/AAAAAAAAFbs/Dd4t3CXZVvA/s400/12angrymen.gif",
                                 "https://www.youtube.com/watch?v=Z4Ym5vBfk50")

pulp_fiction= mediatek.Movie("Pulp Fiction",
                             "http://www.parkcircus.fr/assets/0009/5511/affiche_A3_PULP_FICTION.jpg",
                             "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
                             
good_bad_ugly = mediatek.Movie("The Good, Tha Bad and the Ugly",
                               "https://i.jeded.com/i/the-good-the-bad-and-the-ugly-il-buono-il-brutto-il-cattivo.9123.jpg",
                               "https://www.youtube.com/watch?v=WCN5JJY_wiA")

lord_of_rings_1 = mediatek.Movie("The Lord of the Rings: The Fellowship of the Ring",
                                 "http://static.rogerebert.com/uploads/movie/movie_poster/lord-of-the-rings-the-fellowship-of-the-ring-2001/large_9HG6pINW1KoFTAKY3LdybkoOKAm.jpg",
                                 "https://www.youtube.com/watch?v=V75dMMIW2B4")

                                 

movies=[shawshank_redemption, godfather_2, twelve_angry_men, pulp_fiction, good_bad_ugly, lord_of_rings_1]
fresh_tomatoes.open_movies_page(movies)

print ("Class doc: " + mediatek.Movie.__doc__ +
       "\nClass Name: " + mediatek.Movie.__name__ +
       "\nClass Module: " + mediatek.Movie.__module__)


                                    

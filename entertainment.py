import media
import fresh_tomatoes

Sing=media.Movie("Sing",
                 "Dapper Koala Buster Moon presides over a once-grand theater that has fallen on hard times. An eternal optimist, and a bit of a scoundrel, he loves his theater above all and will do anything to preserve it. Facing the crumbling of his life's ambition, he takes one final chance to restore his fading j…",
                 "http://t2.gstatic.com/images?q=tbn:ANd9GcQeTMzh3aGw46IVUdS6N2tToanuLOc9dO7f6CgWVQlq1laJjuXa",
                 "https://www.youtube.com/watch?v=m37yG_7UXRM")

#The_Lego_Batman_Movie.show_trailer()

Rock_Dog=media.Movie("Rock_Dog",
                     "For the Tibetan mastiffs on Snow Mountain, a dog's life has a simple riff -- guard a peaceful village of sheep from the thuggish wolf Linnux and his rabid pack. To avoid distractions, mastiff leader Khampa forbids all music. ",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcR8DNLN51ENNrtcztMZ7Z1BYOYEAV1mdTjUiw14685fsxMdVk9I",
                     "https://www.youtube.com/watch?v=AZhssZV75vY")
#Rock_Dog.show_trailer()


A_Dog_Purpose=media.Movie("A_Dog_Purpose",
                          "A devoted dog (Josh Gad) discovers the meaning of its own existence through the lives of the humans it teaches to laugh and love. Reincarnated as multiple canines over the course of five decades, the lovable pooch develops an unbreakable bond with a kindred spirit named Ethan (Bryce Gheisar).",
                          "https://i.ytimg.com/vi/1jLOOCADTGs/maxresdefault.jpg",
                          "https://www.youtube.com/watch?v=WBvftTVGnGI")

#A_Dog_Purpose.show_trailer()




Hidden_Figures=media.Movie("Hidden_Figures",
                           "The incredible untold story of Katherine G. Johnson, Dorothy Vaughan and Mary Jackson - brilliant African-American women working at NASA, who served as the brains behind one of the greatest operations in history: the launch of astronaut John Glenn into orbit, a stunning achievement that restored the…",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRqU2FbN7Zp0ELl-sX4lO8XO0pTjpmdJcpos_fnP9wM9DQHYgFq",
                           "https://www.youtube.com/watch?v=WnZRw8juTsQ")

Moonlight=media.Movie("Moonlight",
                      "A look at three defining chapters in the life of Chiron, a young black man growing up in Miami. His epic journey to manhood is guided by the kindness, support and love of the community that helps raise him.",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcT53B_Wizqekgv5U9fetXZc_7FmMFzp5MpeEodcyTOiugrjV7iP",
                      "https://www.youtube.com/watch?v=2gCc6kGpXdw")

The_Lego_Batman_Movie=media.Movie("The_Lego_Batman_Movie",
                                  "There are big changes brewing in Gotham, but if Batman (Will Arnett) wants to save the city from the Joker's (Zach Galifianakis) hostile takeover, he may have to drop the lone vigilante thing, try to work with others and maybe, just maybe, learn to lighten up. Maybe his superhero sidekick Robin (Michael Cera) and loyal butler Alfred (Ralph Fiennes) can show him a thing or two.",
                                  "http://www.legobatman.com/assets/content/home/promo-instagram.jpg",
                                  "https://www.youtube.com/watch?v=_pc2-y8WJn8")

movies=[Sing,Moonlight,A_Dog_Purpose,Rock_Dog,Hidden_Figures,The_Lego_Batman_Movie]
fresh_tomatoes.open_movies_page(movies)
                      

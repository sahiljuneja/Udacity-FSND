import media
import fresh_tomatoes

'''
Movie - Up
Description Source - https://www.imdb.com/title/tt1049413/plotsummary, user: Jwelch5742
'''
up = media.Movie("Up",
                 "Carl Fredricksen, a 78-year-old balloon salesman, is about "
				 "to fulfill a lifelong dream. Tying thousands of balloons to"
				 "his house, he flies away to the South American wilderness. " 
				 "But curmudgeonly Carl's worst nightmare comes true when he "
				 "discovers a little boy named Russell is a stowaway aboard "
				 "the balloon-powered house.",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/"
                 "Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

'''
Movie - Inside Out
Description Source - https://www.imdb.com/title/tt2096673/plotsummary
'''
inside_out = media.Movie("Inside Out",
                  "When a young girl named Riley is uprooted from her Midwestern "
                  "lifestyle and moves to the busy and chaotic San Francisco, "
                  "her emotions; Anger, Sadness, Disgust, Fear, and (her most "
                  "important emotion) Joy, start to disagree on how to deal "
                  "with this dramatic change, which causes problems up in "
                  "Headquaters, the central living and working place for "
                  "the five emotions.",
                  "https://upload.wikimedia.org/wikipedia/en/0/0a/"
                  "Inside_Out_%282015_film%29_poster.jpg",
                  "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

'''
Movie - Megamind
Description Source - https://www.imdb.com/title/tt1001526/plotsummary, user: IMDB editors
'''
megamind = media.Movie("Megamind",
                  "After super-villain Megamind kills his good-guy nemesis, "
                  "Metro Man, he becomes bored since there is no one left "
                  "to fight. He creates a new foe, Tighten, who, instead "
                  "of using his powers for good, sets out to destroy the "
                  "world, positioning Megamind to save the day for the "
                  "first time in his life.",
                  "https://upload.wikimedia.org/wikipedia/en/8/89/"
                  "Megamind2010Poster.jpg",
                  "https://www.youtube.com/watch?v=Xu42-p6_5RE")

# Create movie list
movie_list = [up, inside_out, megamind]

# Build HTML file
fresh_tomatoes.open_movies_page(movie_list)

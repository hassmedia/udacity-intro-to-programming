import class_file
import website

'''
Lists with details for each movie.
'''

# star wars movie details
star_wars = class_file.Movie(
	"Star Wars Episode III",
	"As the Clone Wars near an end, the Sith Lord Darth Sidious steps out of the shadows, at which time Anakin succumbs to his emotions, becoming Darth Vader and putting his relationships with Obi-Wan and Padme at risk.",
	"https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
	"https://www.youtube.com/watch?v=5UnjrG_N8hU"
)

# avatar movie details
avatar = class_file.Movie(
	"Avatar",
	"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

# tron legacy movie details
tron_legacy = class_file.Movie(
	"TRON: Legacy",
	"The son of a virtual world designer goes looking for his father and ends up inside the digital world that his father designed. He meets his father's corrupted creation and a unique ally who was born inside the digital world.",
	"https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
	"https://www.youtube.com/watch?v=L9szn1QQfas"
)

# hunger games movie details
hunger_games = class_file.Movie(
	"Hunger Games",
	"Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised fight to the death in which two teenagers from each of the twelve Districts of Panem are chosen at random to compete.",
	"https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
	"https://www.youtube.com/watch?v=qoUT7q2iTbQ"
)

# lists with movies
movies = [star_wars, avatar, tron_legacy, hunger_games]

# initialise program
website.open_movies_page(movies)

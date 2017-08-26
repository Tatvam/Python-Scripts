import media
import fresh_tomatoes
toy_story = media.Movie( 'Toy Story' , 'Toys come to life' , 'https://upload.wikimedia.org/wikipedia/en/5/5c/Avatar_picture.jpg' , 'https://www.youtube.com/watch?v=KYz2wyBy3kc' )
#print(toy_story.storyline)
avatar = media.Movie( 'Avatar' , 'Story about capturing alien territory' , 'https://upload.wikimedia.org/wikipedia/en/5/5c/Avatar_picture.jpg' , 'https://www.youtube.com/watch?v=d1_JBMrrYw8' )
#print(avatar.storyline)
#avatar.trailer()
movies=[toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
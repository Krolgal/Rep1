import tmdbsimple as tmdb

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

# http get requesttel lekértünk adatokat, JSON-ben kaptuk vissza

search = tmdb.Search()
response = search.movie(query='Alien')['results']


import pprint
pprint.pprint(response[0], indent = 4)
movie = tmdb.Movies(response[0]['id'])
print(movie.credits()['cast'])

for item in movie.credits()['cast']:
    print(item)

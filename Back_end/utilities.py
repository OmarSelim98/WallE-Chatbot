from flask import jsonify, send_file
import math
import requests
import random
import json
def getGenres():
    api_key = 'e8045335406b33dd9f35b9ec6eb3c5ec'
    url = "https://api.themoviedb.org/3/genre/movie/list?api_key={}&language=en-USc".format(api_key)
    r = requests.get(url=url).json()
    genres = []
    for i in range(len(r['genres'])):
        genres.append('<button (onclick)="getNameBtn(\'{}\')" class="btn chat-btn" >{}</button><br>'.format(r['genres'][i]['id'],r['genres'][i]['name']))
    genres_text = " ".join(str(x) for x in genres)
    return genres_text

def getByGenre(args):
    genre_id = args[0]
    api_key = 'e8045335406b33dd9f35b9ec6eb3c5ec'
    rand = random.randrange(1, 100)
    url = 'https://api.themoviedb.org/3/discover/movie?api_key={}&with_genres={}&page={}'.format(api_key,genre_id,rand)
    res = requests.get(url=url).json()
    movies = []
    for i in range(0,3):
        movie = {}
        movie["title"] = res['results'][i]['title']
        movie["rating"] = res['results'][i]['vote_average']
        movie["release_date"] = res['results'][i]['release_date']
        movie["poster_path"] = "http://image.tmdb.org/t/p/w185{}".format(res['results'][i]['poster_path'])
        movies.append(movie)
    return json.dumps(movies)
def getTrending():
    api_key = 'e8045335406b33dd9f35b9ec6eb3c5ec'
    url = 'https://api.themoviedb.org/3/trending/movie/day?api_key={}'.format(api_key)
    res = requests.get(url=url).json()
    movies = []
    for i in range(0,3):
        movie = {}
        movie["title"] = res['results'][i]['title']
        movie["rating"] = res['results'][i]['vote_average']
        movie["release_date"] = res['results'][i]['release_date']
        movie["poster_path"] = "http://image.tmdb.org/t/p/w185{}".format(res['results'][i]['poster_path'])
        movies.append(movie)
    return json.dumps(movies)
def searchFor(args):
    api_key = 'e8045335406b33dd9f35b9ec6eb3c5ec'
    movie_name = args[0]
    url = 'https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query={}&page=1&include_adult=false'.format(api_key,movie_name)
    res = requests.get(url=url).json()
    movies = []
    for i in range(len(res['results'])):
        movie = {}
        movie["id"] = res['results'][i]['id']
        movie["title"] = res['results'][i]['title']
        movie["poster_path"] = "http://image.tmdb.org/t/p/w185{}".format(res['results'][i]['poster_path'])
        movies.append(movie)
    return "search ||| "+json.dumps(movies)
def getSimilar(args):
    movie_id= args[0]
    api_key = 'e8045335406b33dd9f35b9ec6eb3c5ec'
    url='https://api.themoviedb.org/3/movie/{}/similar?api_key={}&language=en-US&page=1'.format(movie_id,api_key)
    res = requests.get(url=url).json()
    movies = []
    for i in range(0,3):
        movie = {}
        movie["title"] = res['results'][i]['title']
        movie["rating"] = res['results'][i]['vote_average']
        movie["release_date"] = res['results'][i]['release_date']
        movie["poster_path"] = "http://image.tmdb.org/t/p/w185{}".format(res['results'][i]['poster_path'])
        movies.append(movie)
    return json.dumps(movies)
import datetime

from flask import Blueprint, jsonify
from src.IdlixScrapper import IdlixScrapper
from cache import Cache


genre = Blueprint('genre', __name__)

@genre.route('/')
@Cache.cached(timeout=300)
def getGenre():
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_genre(),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

@genre.route('/<genre>/<page>')
@Cache.cached(timeout=300)
def getMovieByGenre(genre, page):
    list_genre = IdlixScrapper().get_genre()
    list_genre = [i.lower() for i in list_genre]

    if genre not in list_genre:
        return jsonify(
            {
                'status': 'error',
                'message': 'genre is required'
            }
        )

    if not page.isdigit():
        return jsonify(
            {
                'status': 'error',
                'message': 'page is required'
            }
        )

    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_movie_in_genre(genre, page),
            'cache_time' : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

@genre.route('/netflix/')
@Cache.cached(timeout=300)
def getNetflix():
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_network_netflix(1),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

@genre.route('/netflix/<page>')
@Cache.cached(timeout=300)
def getNetflixByPage(page):
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_network_netflix(page),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
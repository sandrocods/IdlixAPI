import datetime
from flask import Blueprint, jsonify
from src.IdlixScrapper import IdlixScrapper
from cache import Cache

movie = Blueprint('movie', __name__)


##
# Index Movie Series
##
@movie.route('/')
@Cache.cached(timeout=300)
def getMovie():
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_movie_series(1),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })


##
# Movie Page
##
@movie.route('/<page>')
@Cache.cached(timeout=300)
def getMovies(page):
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_movie_series(page),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })


##
# Info Movie
##
@movie.route('/detail/<slug>')
@Cache.cached(timeout=300)
def getMovieBySlug(slug):
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_info_movie(slug),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

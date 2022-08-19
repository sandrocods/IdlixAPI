import datetime
from flask import Blueprint, jsonify
from src.IdlixScrapper import IdlixScrapper
from cache import Cache

trending = Blueprint('trending', __name__)


@trending.route('/movie')
@Cache.cached(timeout=300)
def getTrendingMovie():
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_movie_tranding(1),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })


@trending.route('/movies/<page>')
@Cache.cached(timeout=300)
def getTrendingMovies(page):
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_movie_tranding(page),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })


@trending.route('/tv')
@Cache.cached(timeout=300)
def getTrendingTvs():
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_tv_trending(1),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })


@trending.route('/tv/<page>')
@Cache.cached(timeout=300)
def getTrendingTv(page):
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_tv_trending(page),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

import datetime
from flask import Blueprint, jsonify
from src.IdlixScrapper import IdlixScrapper
from cache import Cache

tv = Blueprint('tv', __name__)


##
# Index TV Series
##
@tv.route('/')
@Cache.cached(timeout=300)
def getTv():
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_serial_tv(1),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })


##
# Tv page
#
@tv.route('/<page>')
@Cache.cached(timeout=300)
def getTvs(page):
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_serial_tv(page),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })


##
# Tv detail
#
@tv.route('/detail/<slug>')
@Cache.cached(timeout=300)
def getTvBySlug(slug):
    return jsonify(
        {
            'status': 'success',
            'data': IdlixScrapper().get_info_tv(slug),
            'cache_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

from flask import Flask, jsonify
from api.movie import movie
from api.genre import genre
from api.trending import trending
from api.tv import tv
from cache import Cache

app = Flask(__name__)

Cache.init_app(app=app, config={
    'DEBUG': False,
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 400
})

app.register_blueprint(tv, url_prefix='/tv')
app.register_blueprint(genre, url_prefix='/genre')
app.register_blueprint(movie, url_prefix='/movie')
app.register_blueprint(trending, url_prefix='/trending')


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'status': 'error',
        'message': 'API Route Not Found'
    }), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({
        'status': 'error',
        'message': 'Unable to process request'
    }), 500


@app.route('/')
def index():
    return jsonify({
        'status': 'success',
        'message': 'Idlix API'
    })


if __name__ == '__main__':
    print('🚀 Server is running ')
    app.run(port=5000, host='0.0.0.0', debug=False)

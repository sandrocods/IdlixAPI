import requests
from bs4 import BeautifulSoup


class IdlixScrapper:
    def __init__(self):
        self.API = 'https://94.103.82.88'

    def get_genre(self):
        """
        Get genre
        """
        r = requests.get(self.API + '/genre/')
        soup = BeautifulSoup(r.text, 'html.parser')
        genre = soup.find('div', class_='container').find_all('a')
        data_genre = []
        for i in genre:
            data_genre.append(i.get('title').replace(' Genre', ''))
        return data_genre

    def get_movie_in_genre(self, genre, page=1):
        """
        Get the movie in the genre
        """
        r = requests.get(self.API + '/genre/' + genre + '/page/' + str(page))
        soup = BeautifulSoup(r.text, 'html.parser')
        movie = soup.findAll('article', class_='item movies')
        data_movie = []
        for i in movie:
            data_movie.append({
                'img': i.find('div', class_='poster').find('img').get('src'),
                'title': i.find('div', class_='data').find('a').text,
                'rating': i.find('div', class_='rating').text,
                'quality': i.find('div', class_='mepo').find('span').text,
                'slug': i.find('div', class_='poster').find('a').get('href').split('/')[-2],
                'date': i.find('div', class_='data').find('span').text,
                'link': i.find('div', class_='data').find('a').get('href')
            })

        return data_movie

    def get_movie_tranding(self, page=1):
        """
        Get the movie tranding
        """
        r = requests.get(self.API + '/trending/page/' + str(page) + '/?get=movies')
        soup = BeautifulSoup(r.text, 'html.parser')
        movie = soup.findAll('article', class_='item movies')
        data_movie = []
        for i in movie:
            data_movie.append({
                'img': i.find('div', class_='poster').find('img').get('src'),
                'title': i.find('div', class_='data').find('a').text,
                'rating': i.find('div', class_='rating').text,
                'quality': i.find('div', class_='mepo').find('span').text,
                'slug': i.find('div', class_='poster').find('a').get('href').split('/')[-2],
                'date': i.find('div', class_='data').find('span').text,
                'link': i.find('div', class_='data').find('a').get('href')
            })

        return data_movie

    def get_info_movie(self, link):
        """
        Get info movie
        """
        r = requests.get(self.API + '/movie/' + link + '/')
        soup = BeautifulSoup(r.text, 'html.parser')

        # get tag movie
        tag_content = soup.find('div', class_='sgeneros')
        content_tag = []
        for i in tag_content:
            content_tag.append(
                i.findNext('a').text
            )

        if soup.find('span', class_='CR rated'):
            rating = soup.find('span', class_='CR rated').text
        else:
            rating = '-'

        if soup.find('span', class_='tagline'):
            tagline = soup.find('span', class_='tagline').text
        else:
            tagline = '-'
        return {
            'img': soup.find('div', class_='poster').find('img').get('src'),
            'title': soup.find('div', class_='data').find('h1').text,
            'description': soup.find('div', class_='wp-content').find('p').text,
            'tagline': tagline,
            'date': soup.find('span', class_='date').text,
            'country': soup.find('span', class_='country').text,
            'duration': soup.find('span', class_='runtime').text,
            'rating': rating,
            'tag': content_tag[:-1],
        }

    def get_tv_trending(self, page=1):
        """
        Get the tv tranding
        """
        r = requests.get(self.API + '/trending/page/' + str(page) + '/?get=tv')
        soup = BeautifulSoup(r.text, 'html.parser')
        movie = soup.findAll('article', class_='item tvshows')
        data_movie = []
        for i in movie:
            data_movie.append({
                'img': i.find('div', class_='poster').find('img').get('src'),
                'title': i.find('div', class_='data').find('a').text,
                'rating': i.find('div', class_='rating').text,
                'slug': i.find('div', class_='poster').find('a').get('href').split('/')[-2],
                'date': i.find('div', class_='data').find('span').text,
                'link': i.find('div', class_='data').find('a').get('href')
            })

        return data_movie

    def get_info_tv(self, link):
        """
        Get info tv
        """
        r = requests.get(self.API + '/tvseries/' + link + '/')
        soup = BeautifulSoup(r.text, 'html.parser')

        # get tag movie
        content_tag = []
        for i in soup.find('div', class_='sgeneros'):
            content_tag.append(
                i.findNext('a').text
            )

        # get info sessions
        data_sessions = []
        for i in soup.findAll('div', class_='se-c'):
            for j in i.find('ul', class_='episodios').findAll('li'):
                data_sessions.append({
                    'Session ' + i.find('span', class_='se-t').text: {
                        'title': j.find('a').text,
                        'date': j.find('span', class_='date').text,
                        'image': j.find('img').get('src'),
                        'link': j.find('a').get('href')
                    },
                })

        if soup.find('span', class_='CR rated'):
            rating = soup.find('span', class_='CR rated').text
        else:
            rating = '-'

        if soup.find('span', class_='tagline'):
            tagline = soup.find('span', class_='tagline').text
        else:
            tagline = '-'

        return {
            'image': soup.find('div', class_='poster').find('img').get('src'),
            'title': soup.find('div', class_='data').find('h1').text,
            'description': soup.find('div', class_='wp-content').find('p').text,
            'tagline': tagline,
            'date': soup.find('span', class_='date').text,
            'rating': rating,
            'tag': content_tag[:-1],
            'sessions': data_sessions,
            'total_movie': len(data_sessions)
        }

    def get_network_netflix(self, page=1):
        """
        Get netflix series
        """
        r = requests.get(self.API + '/network/netflix/page/' + str(page) + '/')
        soup = BeautifulSoup(r.text, 'html.parser')
        movie = soup.findAll('article', class_='item tvshows')
        data_movie = []
        for i in movie:
            data_movie.append({
                'img': i.find('div', class_='poster').find('img').get('src'),
                'title': i.find('div', class_='data').find('a').text,
                'rating': i.find('div', class_='rating').text,
                'slug': i.find('div', class_='poster').find('a').get('href').split('/')[-2],
                'date': i.find('div', class_='data').find('span').text,
                'link': i.find('div', class_='data').find('a').get('href')
            })
        return data_movie

    def get_serial_tv(self, page=1):
        """
        Get serial tv series
        """
        r = requests.get(self.API + '/tvseries/page/' + str(page) + '/')
        soup = BeautifulSoup(r.text, 'html.parser')
        movie = soup.findAll('article', class_='item tvshows')
        data_movie = []
        for i in movie:
            data_movie.append({
                'img': i.find('div', class_='poster').find('img').get('src'),
                'title': i.find('div', class_='data').find('a').text,
                'rating': i.find('div', class_='rating').text,
                'slug': i.find('div', class_='poster').find('a').get('href').split('/')[-2],
                'date': i.find('div', class_='data').find('span').text,
                'link': i.find('div', class_='data').find('a').get('href')
            })

        return data_movie

    def get_movie_series(self, page=1):
        """
        Get the movie series
        """
        r = requests.get(self.API + '/movie/page/' + str(page) + '/')
        soup = BeautifulSoup(r.text, 'html.parser')
        movie = soup.find('div', class_='animation-2 items full').findAll('article', class_='item movies')
        data_movie = []
        for i in movie:
            data_movie.append({
                'img': i.find('div', class_='poster').find('img').get('src'),
                'title': i.find('div', class_='data').find('a').text,
                'rating': i.find('div', class_='rating').text,
                'slug': i.find('div', class_='poster').find('a').get('href').split('/')[-2],
                'date': i.find('div', class_='data').find('span').text,
                'link': i.find('div', class_='data').find('a').get('href')
            })

        return data_movie

<p align="center">
<img src="https://github.com/sandrocods/IdlixAPI/blob/master/ss/IDLIX.png?raw=true" alt="Jupyter Notebook" style="width:200%;">

</p>

Program sederhana yang dibuat dengan bahasa pemrograman python3. menggunakan metode scrapping untuk mendapatkan
informasi web dan menampilkan kembali dalam bentuk API Json

## 📚 Dibuat Dengan

- [Python3](https://www.python.org/)
- [Requests](https://pypi.org/project/requests/)
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [Flask](https://pypi.org/project/Flask/)
- [Flask-Caching](https://pypi.org/project/Flask-Caching/)

## ✅ Fitur

- Menggunakan Caching dengan Flask Caching untuk mengurangi beban server dalam mengambil data langsung dari web IDLIX

## 🚀 Demo

- [idlixapi.sandroputraa.com](https://idlixapi.sandroputraa.com/)
- [idlix-api.vercel.app](https://idlix-api.vercel.app/)

## 📑 Cara Penggunaan

Lakukan Git pada repository ini

```bash
  git clone https://github.com/sandrocods/IdlixAPI
```

Masuk ke folder repository

```bash
  cd IdlixAPI
```

Install Requirements

```bash
  pip install -r ./requirements.txt
```

Menjalankan Program

```bash
  python3 main.py
```

Output :
![ss](https://github.com/sandrocods/IdlixAPI/blob/master/ss/ss.png?raw=true)

## 📝 Refrensi API

#### 1. Sub Genre

#### Menampilkan seluruh genre film

#### Request :

```http
  GET /genre/
```

#### Example : [https://idlix-api.vercel.app/genre/](https://idlix-api.vercel.app/genre/)

#### Result :

[response_genre.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_genre.json)

#### Menampilkan List Film berdasarkan Genre dan Page

#### Request :

```http
  GET /genre/<genre>/<page>
```

#### Example : [https://idlix-api.vercel.app/action/8](https://idlix-api.vercel.app/action/8)

| Parameter | Tipe     | Deskripsi                |
| :-------- | :------- | :------------------------- |
| `genre` | `string` | **Required**. Genre Film |
| `page` | `string` | **Required**. Nomor halaman |

#### Result :

[response_genre_page.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_genre_page.json)

#### Menampilkan List Film berdasarkan Genre Netflix

#### Request :

```http
  GET /genre/netflix/
```

#### Example : [https://idlix-api.vercel.app/netflix/](https://idlix-api.vercel.app/netflix/)

#### Result :

[response_genre_netflix.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_genre_netflix.json)

#### Menampilkan List Film Genre Netflix Berdsarkan Page

#### Request :

```http
  GET /genre/netflix/<page>
```

#### Example : [https://idlix-api.vercel.app/netflix/2](https://idlix-api.vercel.app/netflix/2)

| Parameter | Tipe     | Deskripsi                   |
| :-------- | :------- |:----------------------------|
| `genre` | `string` | **Required**. netflix       |
| `page` | `string` | **Required**. Nomor halaman |

#### Result :

[response_genre_netflix_page.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_genre_netflix_page.json)

#### 2. Sub Tv Series

#### Menampilkan List Tv Series

#### Request :

```http
  GET /tv/
```

#### Example : [https://idlix-api.vercel.app/tv/](https://idlix-api.vercel.app/tv/)

#### Result :

[response_tv.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_tv.json)

#### Menampilkan List Tv Series berdasarkan Page

#### Request :

```http
  GET /tv/<page>
```

#### Example : [https://idlix-api.vercel.app/tv/2](https://idlix-api.vercel.app/tv/2)

| Parameter | Tipe     | Deskripsi                   |
| :-------- | :------- |:----------------------------|
| `page` | `string` | **Required**. Nomor halaman |

#### Result :

[response_tv_page.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_tv_page.json)

#### Menampilkan Detail Tv Series

#### Request :

```http
  GET /tv/detail/<slug>
```

#### Example : [https://idlix-api.vercel.app/tv/detail/she-hulk-attorney-at-law-2022](https://idlix-api.vercel.app/tv/detail/she-hulk-attorney-at-law-2022)

| Parameter | Tipe     | Deskripsi                   |
| :-------- | :------- |:----------------------------|
| `slug` | `string` | **Required**. Slug Tv Series |

#### Result :

[response_tv_detail.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_tv_detail.json)

#### 3.Sub Movie

#### Menampilkan List Movie

#### Request :

```http
  GET /movie/
```

#### Example : [https://idlix-api.vercel.app/movie/](https://idlix-api.vercel.app/movie/)

#### Result :

[response_movie.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_movie.json)

#### Menampilkan List Movie berdasarkan Page

#### Request :

```http
  GET /movie/<page>
```

#### Example : [https://idlix-api.vercel.app/movie/2](https://idlix-api.vercel.app/movie/2)

| Parameter | Tipe     | Deskripsi                   |
| :-------- | :------- |:----------------------------|
| `page` | `string` | **Required**. Nomor halaman |

#### Result :

[response_movie_page.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_movie_page.json)

#### Menampilkan Detail Movie

#### Request :

```http
  GET /movie/detail/<slug>
```

#### Example : [https://idlix-api.vercel.app/movie/detail/the-godfather](https://idlix-api.vercel.app/movie/detail/the-godfather)

| Parameter | Tipe     | Deskripsi                   |
| :-------- | :------- |:----------------------------|
| `slug` | `string` | **Required**. Slug Movie |

#### Result :

[response_movie_detail.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_movie_detail.json)

#### 3.Sub Trending

#### Menampilkan List Movie Trending

#### Request :

```http
  GET /trending/movie
```

#### Example : [https://idlix-api.vercel.app/trending/movie](https://idlix-api.vercel.app/trending/movie)

#### Result :

[response_trending_movie.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_trending_movie.json)

#### Menampilkan List Movie Trending berdasarkan Page

#### Request :

```http
  GET /trending/movies/<page>
```

#### Example : [https://idlix-api.vercel.app/trending/movies/2](https://idlix-api.vercel.app/trending/movies/2)

| Parameter | Tipe     | Deskripsi                   |
| :-------- | :------- |:----------------------------|
| `page` | `string` | **Required**. Nomor halaman |

#### Result :

[response_trending_movie_page.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_tranding_movie_page.json)

#### Menampilkan List Tv Series Trending

#### Request :

```http
  GET /trending/tv
```

#### Example : [https://idlix-api.vercel.app/trending/tv](https://idlix-api.vercel.app/trending/tv)

#### Result :

[response_trending_tv.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_tranding_tv.json)

#### Menampilkan List Tv Series Trending berdasarkan Page

#### Request :

```http
  GET /trending/tv/<page>
```

#### Example : [https://idlix-api.vercel.app/trending/tv/2](https://idlix-api.vercel.app/trending/tv/2)

| Parameter | Tipe     | Deskripsi                   |
| :-------- | :------- |:----------------------------|
| `page` | `string` | **Required**. Nomor halaman |

#### Result :

[response_trending_tv_page.json](https://github.com/sandrocods/IdlixAPI/blob/master/response_json/response_tranding_tv_page.json)

### Error Response

1. Error Slug / another

```json
{
  "message": "Unable to process request",
  "status": "error"
}
```

2. Data Not Found

```json
{
  "cache_time": "2022-08-20 01:53:45",
  "data": [
  ],
  "status": "success"
}
```

3. API Route Not Found

```json
{
  "message": "API Route Not Found",
  "status": "error"
}
```

4. Error Genre

```json
{
  "message": "genre is required",
  "status": "error"
}
```

5. Error Page

```json
{
  "message": "page is required",
  "status": "error"
}
```


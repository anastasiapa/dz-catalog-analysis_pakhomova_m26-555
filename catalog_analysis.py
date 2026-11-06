
import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average_age)


def duration_in_hours(minutes):
    hours = minutes // 60
    rest_minutes = minutes % 60
    return f"{hours}ч {rest_minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif 7 <= rating < 9:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year < 2015:
            return "старые"
        case _:
            return "недавние"


def print_non_comedy_titles(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    long_movies = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            long_movies += 1
    return long_movies


def normalize_title(title):
    normalized_title = []
    for word in title.split():
        normalized_title.append(word[0].upper() + word[1:])
    return " ".join(normalized_title)


def make_slug(title):
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    normalized_title = normalize_title(movie["title"])
    sorted_genres = ", ".join(sorted(movie["genres"]))

    result = f'"{normalized_title}" ({movie["year"]}) — {movie["rating"]}/10, '
    result += f'{duration_in_hours(movie["duration_min"])}, жанры: {sorted_genres}'
    return result


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    genres = {}
    for movie in movies:
        for current_genre in movie["genres"]:
            genres[current_genre] = genres.get(current_genre, 0) + 1
    return genres


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


current_average_rating = average_rating(movies)

above_average_movies = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > current_average_rating
}


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def check_generator(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    top_movies_duration = sum(
        movie["duration_min"]
        for movie in movies
        if movie["rating"] > 7
    )
    print(top_movies_duration)


def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    print()

    print("Топ-3 фильма:")
    movies_by_title = {movie["title"]: movie for movie in movies}
    for title, rating in top_n_by_rating(movies):
        print(f"  {format_report_line(movies_by_title[title])}")
    print()

    print("Фильмов по жанрам:")
    genres = count_by_genre(movies)
    for genre, count in sorted(
        genres.items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"  {genre} — {count}")
    print()

    print("Все жанры каталога: " + ", ".join(sorted(all_genres(movies))))


if __name__ == "__main__":
    build_report(movies)
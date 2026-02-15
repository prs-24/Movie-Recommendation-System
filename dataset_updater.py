import requests
import pandas as pd
from datetime import datetime
import os

API_KEY = "2e63a072e8de4b91b0e69b4a01a53a64"
BASE_URL = "https://api.themoviedb.org/3"

def fetch_movies(endpoint, pages=5):
    all_results = []

    for page in range(1, pages + 1):
        url = f"{BASE_URL}/{endpoint}?api_key={API_KEY}&page={page}"
        response = requests.get(url)
        results = response.json().get("results", [])
        all_results.extend(results)

    return all_results


def get_genre_mapping():
    movie_url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}"
    tv_url = f"{BASE_URL}/genre/tv/list?api_key={API_KEY}"

    movie_genres = requests.get(movie_url).json()["genres"]
    tv_genres = requests.get(tv_url).json()["genres"]

    genre_map = {}
    for g in movie_genres + tv_genres:
        genre_map[g["id"]] = g["name"]

    return genre_map



def collect_data():
    genre_map = get_genre_mapping()

    endpoints = [
        "trending/all/day",
        "movie/top_rated",
        "movie/popular",
        "tv/popular"
    ]

    all_data = []

    for ep in endpoints:
        results = fetch_movies(ep)

        for item in results:

            if item.get("media_type") == "person":
                continue

            all_data.append({
                "id": item.get("id"),
                "title": item.get("title") or item.get("name"),
                "overview": item.get("overview"),
                "genres": ", ".join([str(g) for g in item.get("genre_ids", [])]),
                "popularity": item.get("popularity"),
                "vote_average": item.get("vote_average"),
                "poster_path": item.get("poster_path") if item.get("poster_path") else "",
                "backdrop_path": item.get("backdrop_path") if item.get("backdrop_path") else "",
                "release_date": item.get("release_date") or item.get("first_air_date"),
                "media_type": item.get("media_type", "movie"),
                "timestamp": datetime.now()
            })

    return pd.DataFrame(all_data)

def update_dataset():
    new_data = collect_data()
    file_name = "movies.csv"

    if os.path.exists(file_name):
        existing = pd.read_csv(file_name)
        combined = pd.concat([existing, new_data])
        combined = combined.drop_duplicates(subset=["id"])
        combined = combined.drop_duplicates(subset=["title"])
    else:
        combined = new_data

    combined.to_csv(file_name, index=False)
    print("✅ movies.csv updated successfully!")

if __name__ == "__main__":
    update_dataset()

import os
from datetime import datetime, timedelta
import subprocess

def check_and_update():
    if not os.path.exists("movies.csv"):
        subprocess.run(["python", "dataset_updater.py"])
        return

    last_modified = datetime.fromtimestamp(os.path.getmtime("movies.csv"))

    if datetime.now() - last_modified > timedelta(hours=24):
        print("Updating dataset...")
        subprocess.run(["python", "dataset_updater.py"])

check_and_update()



import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

print("Loading dataset...")

df = pd.read_csv("movies.csv")
df["overview"] = df["overview"].fillna("")

print("Building TF-IDF matrix...")

tfidf = TfidfVectorizer(stop_words="english")
df["combined_features"] = df["overview"] + " " + df["genres"].fillna("")
tfidf_matrix = tfidf.fit_transform(df["combined_features"])

similarity = cosine_similarity(tfidf_matrix)

print("Model ready!\n")


def recommend(title, top_n=5):

    if title not in df["title"].values:
        matches = get_close_matches(title, df["title"], n=1, cutoff=0.6)
        if not matches:
            return ["Movie not found"]
        title = matches[0]
        print(f"Did you mean: {title}?")

    idx = df[df["title"] == title].index[0]

    scores = list(enumerate(similarity[idx]))

    results = []

    searched_movie = df[df["title"] == title].iloc[0]

    hero_data = {
        "title": searched_movie["title"],
        "overview": searched_movie["overview"],
        "rating": round(searched_movie["vote_average"], 1),
        "genres": searched_movie["genres"],
        "backdrop": searched_movie["backdrop_path"]
    }


    for i, sim_score in scores:
        if i == idx:
            continue

        rating = df.iloc[i]["vote_average"]
        popularity = df.iloc[i]["popularity"]

        # Normalize
        rating_score = rating / 10
        popularity_score = popularity / df["popularity"].max()

        final_score = (sim_score * 0.7) + (rating_score * 0.2) + (popularity_score * 0.1)

        results.append((i, final_score))

    results = sorted(results, key=lambda x: x[1], reverse=True)

    recommendations = []
    seen = set()

    for i, score in results:
        title_candidate = df.iloc[i]["title"]

        if title_candidate not in seen:
            recommendations.append({"title": title_candidate,
                                    "poster": df.iloc[i]["poster_path"],
                                    "rating": round(df.iloc[i]["vote_average"], 1)})
            seen.add(title_candidate)

        if len(recommendations) == top_n:
            break

    return hero_data, recommendations



if __name__ == "__main__":
    movie_name = input("Enter movie name: ")
    recs = recommend(movie_name)

    print("\nRecommended Movies:")
    for r in recs:
        print(r)

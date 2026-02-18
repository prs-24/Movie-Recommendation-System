# 🎬 Movie Recommendation System

A content-based movie recommendation web application built using **FastAPI**, **Scikit-Learn**, and the **TMDB API**.
The system suggests movies and TV shows based on similarity using TF-IDF vectorization and cosine similarity, with a dynamic dataset that can be expanded automatically.

🌐 **Live Demo:**
https://movie-recommendation-system-bkl8.onrender.com/

---

## 🚀 Features

* 🎯 Content-based recommendation using TF-IDF similarity
* 🎥 Movie & TV dataset fetched dynamically from TMDB API
* 🖼 Poster-based recommendation UI (Netflix-style layout)
* 🎬 Hero banner for searched movie
* 🔎 Intelligent title matching with fuzzy search
* 📊 Weighted ranking using popularity and ratings
* ⚡ FastAPI backend with Jinja2 templating
* 🌍 Deployed publicly on Render (production environment)
* 🔄 Dataset can be expanded and auto-updated

---

## 🧠 How It Works

1. Movies and TV data are fetched from the TMDB API.
2. Text features (overview, genres, title) are combined.
3. TF-IDF vectorization converts text into numerical features.
4. Cosine similarity calculates similarity between titles.
5. Weighted scoring improves recommendation quality using:

   * Similarity score
   * Popularity
   * Average rating
6. Top recommendations are displayed with posters.

---

## 🏗 Tech Stack

**Backend**

* FastAPI
* Python
* Pandas
* Scikit-Learn
* Requests

**Frontend**

* HTML
* CSS
* Jinja2 Templates

**Deployment**

* Render (Cloud Platform)

**Data Source**

* TMDB API (The Movie Database)

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── main.py                 # FastAPI application
├── recommender.py          # Recommendation engine
├── dataset_updater.py      # Dataset fetching & processing
├── movies.csv              # Movie dataset
├── requirements.txt        # Dependencies
│
└── templates/
    └── index.html          # Frontend UI
```

---

## ⚙️ Installation (Local Setup)

Clone the repository:

```bash
git clone https://github.com/prs-24/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🔑 TMDB API Setup

1. Create an account at https://www.themoviedb.org/
2. Generate an API key
3. Add your API key inside `dataset_updater.py`

---

## 🔄 Dataset Expansion & Auto Update (Planned)

Future improvements include:

* Automated dataset updates using GitHub Actions
* Larger dataset coverage
* Background update jobs
* Database integration (PostgreSQL / MongoDB)

---

## 🎯 Future Improvements

* Autocomplete search suggestions
* Hybrid recommendation (content + collaborative filtering)
* User accounts & personalization
* Explainable recommendations ("Why recommended?")
* Database storage instead of CSV
* React frontend upgrade

---

## 👨‍💻 Author

**Prateek**
GitHub: https://github.com/prs-24

---

## ⭐ Acknowledgements

* TMDB API for movie data
* Scikit-Learn for machine learning tools
* FastAPI for backend framework

---

## 📜 License

This project is for educational and portfolio purposes.

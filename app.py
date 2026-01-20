import streamlit as st
import pickle
import pandas as pd
import os
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MOVIES_PATH = os.path.join(BASE_DIR, "movies.pkl")
SIMILARITY_PATH = os.path.join(BASE_DIR, "similarity.pkl")

MOVIES_URL = "https://github.com/arjitMathur/Movie_recommendation_system/releases/download/models-v1/movies.pkl"
SIMILARITY_URL = "https://github.com/arjitMathur/Movie_recommendation_system/releases/download/models-v1/similarity.pkl"


def download_file(url, path):
    if not os.path.exists(path):
        with st.spinner(f"Downloading {os.path.basename(path)}..."):
            response = requests.get(url, timeout=120)
            response.raise_for_status()
            with open(path, "wb") as f:
                f.write(response.content)


download_file(MOVIES_URL, MOVIES_PATH)
download_file(SIMILARITY_URL, SIMILARITY_PATH)


movies = pickle.load(open(MOVIES_PATH, "rb"))
similarity = pickle.load(open(SIMILARITY_PATH, "rb"))


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movie_indices = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_indices]


st.title("Movie Recommender System")

movies_list = movies["title"].values

option = st.selectbox(
    "Select a movie, and we’ll recommend more movies for you.",
    movies_list,
    index=None,
    placeholder="Select a Movie...",
)

if st.button("Recommend"):
    if option:
        recommendations = recommend(option)
        for movie in recommendations:
            st.write(movie)

import streamlit as st
import pickle
import pandas as pd
import os

def recommend(movie):
    movie_index=movies[movies['title']== movie].index[0]
    distances=similarity[movie_index]
    movie_index=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    l=[]
    for i in movie_index:
        l.append(movies.iloc[i[0]].title)
    return l

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies = pickle.load(open(os.path.join(BASE_DIR, 'movies.pkl'), 'rb'))
similarity = pickle.load(open(os.path.join(BASE_DIR, 'similarity.pkl'), 'rb'))


movies_list=movies['title'].values
st.title('Movie Recommender System')

option = st.selectbox(
    "Select a movie, and we’ll recommend more movies for you.",
    movies_list,
    index=None,
    placeholder="Select a Movie...",
)

if st.button("Recommend"):
    ls=recommend(option)
    for i in ls:
        st.write(i)


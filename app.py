import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index=movies[movies['title']== movie].index[0]
    distances=similarity[movie_index]
    movie_index=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    l=[]
    for i in movie_index:
        l.append(movies.iloc[i[0]].title)
    return l
    
movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

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


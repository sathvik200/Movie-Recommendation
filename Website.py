import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similiarity = pickle.load(open('similiarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similiarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
    
st.title('Movie Recommender System')

Selected_Movie_Name = st.selectbox(
"Which movie have you watched?",
movies['title'].values
)

if st.button("Recommend"):
    Recommendations = recommend(Selected_Movie_Name)
    for i in Recommendations:
        st.write(i)
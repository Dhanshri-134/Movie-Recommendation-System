
import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = requests.get(url)
    data = data.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movieIndex = movies[movies['title'] == movie].index[0]
    distances = Similarity[movieIndex]
    result = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    result = [(index, float(value)) for index, value in result]

    recommended_movie_names =[]
    recommended_movie_posters = []
    for i in result[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        #Poster Fetching
        recommended_movie_posters.append(fetch_poster(i[0]))
    return recommended_movie_names,recommended_movie_posters




moviesList = pickle.load(open('movies_dict.pkl','rb'))
Similarity = pickle.load(open('Similarity.pkl','rb'))


# movies = pd.DataFrame(moviesList['title'].values)
movies = pd.DataFrame(moviesList)

st.title('Movie Recommender System')

MovieChoice = st.selectbox(
    'How would you like ?',
    (movies['title'].values)
)

if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(MovieChoice)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

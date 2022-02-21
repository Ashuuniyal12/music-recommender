import pickle
import pandas as pd
import streamlit as st
import requests

import recommenders

song_df = pickle.load(open('song_df.pkl', 'rb'))

st.title("Music Recommender System")
st.text("By- Rishabh")
st.text(" ")

selected_song = st.selectbox('Enter a movie name', song_df['song'].values)
if st.button('Recommend'):
    ir = recommenders.item_similarity_recommender_py()
    ir.create(song_df, 'user_id', 'song')
    name = ir.recommend(song_df['user_id'][5])
    songlist = []
    songlist = name['song']
    st.text(songlist[0])
    st.text(songlist[1])
    st.text(songlist[2])
    st.text(songlist[3])
    st.text(songlist[4])
    st.text(songlist[5])
    st.text(songlist[6])
    st.text(songlist[7])
    st.text(songlist[8])
    st.text(songlist[9])








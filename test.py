import streamlit as st
import numpy as np
import pandas as pd
import flag


dataframe = pd.read_csv('player_stats_dataset.csv')
# Set page config
st.set_page_config(page_title='Soccer Players Stats', page_icon=':soccer:', initial_sidebar_state='expanded')

games_list = sorted(list(set(dataframe['player'])))
players = pd.read_csv('players_details.csv')
# Drop-down menu "Select Football Game"
st.sidebar.markdown('## Select Player ')
st.sidebar.markdown(flag.flag('Israel'))
menu_game = st.sidebar.selectbox('Select a player at your choice', games_list, index=14)

selected_player =players. loc[players['Name'] == menu_game]
st.write(f'my name is {menu_game} i born in {selected_player["Nationality"].iloc[0]} in {selected_player["Birth_Date"].iloc[0]}  ')

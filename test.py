import streamlit as st
import numpy as np
import pandas as pd
dataframe = pd.read_csv('player_stats_dataset.csv')
# Set page config
st.set_page_config(page_title='Soccer Players Stats', page_icon=':soccer:', initial_sidebar_state='expanded')

games_list = list(set(dataframe['player']))

# Drop-down menu "Select Football Game"
st.sidebar.markdown('## Select Player ')
menu_game = st.sidebar.selectbox('Select a player at your choice', games_list, index=14)
st.sidebar.markdown("""Here you can select one of 15 football games from the UEFA Euro 2020 knockout stage: """)
st.sidebar.markdown(""" 
                    * eight games in the round of 16
                    * four quarter-finals
                    * two semi-finals
                    * one final
                    """)
st.dataframe(dataframe.loc[dataframe['player'] == menu_game])
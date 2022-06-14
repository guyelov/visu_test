import streamlit as st
import numpy as np
import pandas as pd
dataframe = pd.read_csv('player_stats_dataset.csv')
st.dataframe(dataframe)
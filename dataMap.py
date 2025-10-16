import pandas as pd 
import streamlit as st
import numpy as np 

map_data = pd.DataFrame( 
np.random.randn(100, 2) / [50,50] + [37.76, -122.4], 
columns = ['lat', 'lon']) 
st.map(map_data) 

# print(map_data)
st.dataframe(map_data);
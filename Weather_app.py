import os
import pytz
import pyowm
import streamlit as st
from matplotlib import dates
from datetime import datetime
from matplotlib import pyplot as plt

owm = pyowm.OWM("1d7b48f22fc1a802e2be1716972facae")
mgr = owm.weather_manager()

st.title("WEATHER FORCASTING BY SID")
st.write("### Write the name of a City and select the Temperature Unit and Graph Type from the sidebar")

place=st.text_input("NAME OF THE CITY :", "")
if place == None:
    st.write("Write a CITY Name!")

unit=st.selectbox("Select Temperature Unit",("Celsius","Fahrenheit"))
g_type=st.selectbox("Select Graph Type",("Line Graph","Bar Graph")) 

def bar(days,temp_min,temp_max):
    plt.bar(days,temp_min)
    plt.bar(days,temp_max)


def line_graph(days,temp_min,temp_max):
    plt.plot(days,temp_min)
    plt.plot(days,temp_max)
      

import streamlit as st
import math

# Titel
st.title("Mijn Eerste Streamlit App")

# Tekst
st.write("Welkom bij mijn app!")

# Slider
x = st.slider("Geef je gewicht in", 1, 100)
y=st.slider("Geef je lengte in", 1, 200)
st.write(f"Jouw BMI bedraagt {x/(y/100)**2}")

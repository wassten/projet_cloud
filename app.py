#import
from logging import PlaceHolder
import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import datetime as dt
import plotly.express as px
import json
import seaborn as sns
import time
import os
import sys
import locale
locale.setlocale(locale.LC_ALL, '')
from PIL import Image
from functools import wraps
from time import time
#footer
import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent
from htbuilder.funcs import rgba, rgb
from sklearn.linear_model import LinearRegression






dataframe = "full_paris_view.csv"
df = pd.read_csv(dataframe)
df.dropna(inplace=True)

X = df[['code_postal', 'surface_reelle_bati', 'nombre_pieces_principales']]
y = df["valeur_fonciere"]
model=LinearRegression()
model.fit(X,y)


# nombre_pieces_principales
# type_local
# code_postal
# surface_reelle_bati
nb_piece = st.text_input(label="Nombre de pièces", key="nb_piece")
type_local = st.text_input(label="Type de local", key="type_local")
cp = st.text_input(label="Code postal", key="cp")
surface = st.text_input(label="Surface à bâtir", key="surface")

if st.button(label="Prédire", key="submit"):
    y_pred = model.predict([[nb_piece], [type_local], [cp], [surface]])
    st.title(y_pred)



#Footer and Layer with images and links (LinkedIn)
from htbuilder.units import px

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 57px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        background_color='#C1EAFF',
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(0, 0, 13, 0),
        border_style="inset",
        border_width=px(1)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def layout2(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { top: 50px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        top=0,
        margin=px(-50, 0, 0, 0),
        width=percent(100),
        background_color='#C1EAFF',
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        border='solid',
        border_width=px(2),
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        "Made in ",
        image('https://i.postimg.cc/wTbVHYDJ/st-removebg-preview.jpg',
              width=px(25), height=px(25)),
        " with 💙 by ",
        link("https://www.linkedin.com/in/wassim-zouitene/", "FONCI'AZURE"),
        " at 🏠",
    ]
    layout(*myargs)

def header():
    myargs = [
        image('https://i.postimg.cc/RFyHy4kV/logo2.jpg',width=px(550), height=px(35))
    ]
    layout2(*myargs)

footer()


 

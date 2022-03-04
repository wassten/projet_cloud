#import
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


#Important variable
path = "./"
files = "full_"
file_end = ".csv"
col_list = ['date_mutation',
        'nature_mutation',
        'valeur_fonciere',
        'code_postal',
        'type_local',
        'longitude', 
        'latitude',
        "code_departement",
        'nature_culture'
        ]

st.sidebar.header("Navigation")
#Fonction
file = open("time.txt", "w+")
def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        file.write('Temps écoulé : {}'.format((end-start)) + "sec")
        return result
    return wrapper







st.info('Source of the dataset :  https://www.data.gouv.fr/en/datasets/demandes-de-valeurs-foncieres/ ')


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
        "FONCI'AZURE",
        " at Efrei Paris",
    ]
    layout(*myargs)

def header():
    myargs = [
        image('https://i.postimg.cc/GmL547SX/FONCIAZURE-name.png',width=px(150), height=px(100))
    ]
    layout2(*myargs)

footer()
header()

 

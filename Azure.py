import streamlit as st
import numpy as np
import pandas as pd 
st.set_option('deprecation.showPyplotGlobalUse', False)



def checkboxed(df,a):
    agree = st.checkbox(str(a))
    if agree:        
        st.write(df)

def write_smthg_stylish(text, font_family, color, font_size):
    st.title("")
    smthg = '<p style="font-family:' + font_family+ '; color:' + color + '; font-size:'+  str(font_size) + 'px;">' + text + '</p>'
    st.markdown(smthg, unsafe_allow_html=True)

def main():
    file = '/Users/hatimmanowaraly/Desktop/EFREIM1/DataViz/Projet DataViz/full_IdF_data.csv'
    df = pd.read_csv(file)

    st.title("Project Fonci'Azure")

    checkboxed(df,'Inspecter les données :')

    write_smthg_stylish("Choisissez l'adresse code voie :", 'cursive', 'White',  30)
    adresse_code_voie = st.number_input(label = 'adresse_code_voie')
    
    write_smthg_stylish("Choisissez le code postal :", 'cursive', 'White',  30)
    code_postal = st.number_input('code_postal')

    write_smthg_stylish("Choisissez le code commune :", 'cursive', 'White',  30)
    code_commune = st.number_input('code_commune')

    write_smthg_stylish("Choisissez le code departement :", 'cursive', 'White',  30)
    code_departement = st.number_input('code_departement')

    write_smthg_stylish("Choisissez la surface réelle bâtie :", 'cursive', 'White',  30)
    surface_reelle_bâtie = st.number_input('surface_reelle_bati')

    write_smthg_stylish("Choisissez la surface terrain :", 'cursive', 'White',  30)
    surface_terrain = st.number_input('surface_terrain')

    write_smthg_stylish("Choisissez le type du local :", 'cursive', 'White',  30)
    type_local = st.number_input('type_local')

    write_smthg_stylish("Choisissez le nombre de pieces principales :", 'cursive', 'White',  30)
    nombre_pieces_principales = st.number_input('nombre_pieces_principales')
    
    write_smthg_stylish("Choisissez la longitude :", 'cursive', 'White',  30)
    longitude = st.number_input('longitude')

    write_smthg_stylish("Choisissez la latitude :", 'cursive', 'White',  30)
    latitude = st.number_input(label = 'latitude')


    
if __name__ == "__main__":
    main()



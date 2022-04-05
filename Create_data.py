import pandas as pd



def load_data(year): #Loading du DataFrame contenant l'année choisie
    if year == 16:
        file = '/Users/hatimmanowaraly/Desktop/EFREIM1/DataViz/Projet DataViz/full_2016.csv'
    if year == 17:
        file = '/Users/hatimmanowaraly/Desktop/EFREIM1/DataViz/Projet DataViz/full_2017.csv'
    if year == 18:
        file = '/Users/hatimmanowaraly/Desktop/EFREIM1/DataViz/Projet DataViz/full_2018.csv'
    if year == 19:
        file = '/Users/hatimmanowaraly/Desktop/EFREIM1/DataViz/Projet DataViz/full_2019.csv'
    if year == 20:
        file = '/Users/hatimmanowaraly/Desktop/EFREIM1/DataViz/Projet DataViz/full_2020.csv'
    data = pd.read_csv(file)
    return data


def preprocessing(data, code): #Sélection des colonnes utiles ainsi que des lignes correspondant uniquement à la région IdF
    data = pd.DataFrame(data, columns = ['adresse_code_voie','code_postal', 'code_commune', 'code_departement','valeur_fonciere','surface_reelle_bati', 'surface_terrain', 'type_local', 'nombre_pieces_principales','latitude','longitude'])
    data = data[data['code_departement'] == code ]
    data = data[data['surface_reelle_bati'].notna()]
    data = data[data['valeur_fonciere'].notna()]
    data = data[data['surface_terrain'].notna()]
    data = data.sample(n = 130)
    return data


def concatenate_one_data(data): #Concatenation de l'ensemble des départements d'IdF par année
    dict = {75 : 'df_75', 77 : 'df_77', 78 : 'df_78', 91 : 'df_91', 92 : 'df_92', 93 : 'df_93', 94 : 'df_94', 95 : 'df_95'}
    for i in dict.keys():
        dict[i] = preprocessing(data,i)
    
    return pd.concat([dict[75], dict[77], dict[78], dict[91], dict[92], dict[93], dict[94], dict[95]], axis = 0)


def concatenate_all_data(): #Concaténation de l'ens des fichiers de 2016 à 2020 afin d'avoir un maximum de données
    
    df_16 = load_data(16)
    df_16_Idf = concatenate_one_data(df_16)
    df_17 = load_data(17)
    df_17_Idf = concatenate_one_data(df_17)
    df_18 = load_data(18)
    df_18_Idf = concatenate_one_data(df_18)
    df_19 = load_data(19)
    df_19_Idf = concatenate_one_data(df_19)
    df_20 = load_data(20)
    df_20_Idf = concatenate_one_data(df_20)

    return pd.concat([df_16_Idf, df_17_Idf, df_18_Idf, df_19_Idf, df_20_Idf], axis = 0)


def main():
    df_final = concatenate_all_data()
    df_final = df_final.sort_values(by = ['code_postal'])
    df_final.to_csv('/Users/hatimmanowaraly/Desktop/EFREIM1/DataViz/Projet DataViz/full_IdF_data.csv')

main()
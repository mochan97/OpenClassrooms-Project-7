#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# On lit le nombre de colonnes du jeu de données:
def nbr_columns(data):
    return len(data.columns)

# On lit le nombre de lignes du jeu de données:
def nbr_rows(data):
    return len(data.index)

# On lit le nombre de Not a Number du jeu de données:
def NaN_count(data):
    return data.isna().sum().sum()

# On lit le pourcentage de Not a Number du jeu de données:
def NaN_percent(data):
    return data.isna().sum().sum()/data.size

# On calcule le nombre de colonnes qui sont en doublon dans le jeu de données:
def duplicate_columns_count(data):
    return len(data.columns.values.tolist())-len(data.columns.unique())

# On calcule le nombre de lignes qui sont en doublon dans le jeu de données:
def duplicate_rows_count(data):
    return len(data)-len(data.drop_duplicates())

# On calcule le pourcentage de lignes qui sont en doublon dans le jeu de données:
def duplicate_rows_percent(data):
    return duplicate_rows_count(data)/nbr_rows(data)

# On créé une fonction qui affiche les statistiques ci-dessus du jeu de données d'entrée:
def dataset_overview(data):
    print('Nombre de colonnes : {}'.format(nbr_columns(data)))
    print('Nombre de lignes : {}'.format(nbr_rows(data)))
    print('Nombre de NaN : {}'.format(NaN_count(data)))
    print('Pourcentage de NaN (%) : {:.2%}'.format(NaN_percent(data)))
    print('Nombre de colonnes en doublon : {}'.format(duplicate_columns_count(data)))      
    print('Nombre de lignes en doublon : {}'.format(duplicate_rows_count(data)))
    print('Pourcentage de lignes en doublon (%) : {:.2%}'.format(duplicate_rows_percent(data)))
    return None


# In[3]:


# On créé une fonction qui affiche chaque colonne qui contient des NaN et qui compte le nombre de lignes
#qui a des NaN:
def NaN_overview(dataframe):
    series_NaN = 100 * (dataframe.isna().sum()/len(dataframe))
    print('Total number of columns: ', len(series_NaN))
    number_of_NaN_in_series_NaN = 0
    for element in series_NaN:
        if element > 0 :
            number_of_NaN_in_series_NaN += 1
    print('Number of columns with NaN: ', number_of_NaN_in_series_NaN)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(series_NaN)
    return None


# In[4]:


# On crée une fonction qui créé un histogramme pour une colonne d'un dataframe, retourne les percentiles
# et un boxplot de la variable colonne:
import math
def feature_distribution(dataframe, feature):
    
    #Calcul des statistiques
    print("moy:     ", round(dataframe[feature].mean(), 1))
    print("5%tile:  ", round(np.nanpercentile(dataframe[feature].values.tolist(), 5), 1))
    print("25%tile: ", round(np.nanpercentile(dataframe[feature].values.tolist(), 25), 1))
    print("50%tile: ", round(np.nanpercentile(dataframe[feature].values.tolist(), 50), 1))
    print("75%tile: ", round(np.nanpercentile(dataframe[feature].values.tolist(), 75), 1))
    print("95%tile: ", round(np.nanpercentile(dataframe[feature].values.tolist(), 95), 1))
    #print("mod:     ", dataframe[feature].mode())
    #print("skw:     ", round(dataframe[feature].skew(), 2))
    #print("kur:     ", round(dataframe[feature].kurtosis(), 2))
    
    #fig, ax = plt.subplots(1,1)
    #dataframe[feature].hist() # Crée l'histogramme
    #ax.set_title(feature)
    #plt.show() # Affiche l'histogramme
    #fig = plt.figure(figsize=(10, 1));
    
    #Tracé de l'histogramme
    fig, ax = plt.subplots(figsize = (6,4));
    data = dataframe[feature]

        # Calcul des pourcentiles
    quant_5, quant_25, quant_50, quant_75, quant_95 = data.quantile(0.05), data.quantile(0.25), data.quantile(0.5), data.quantile(0.75), data.quantile(0.95)

        # [quantile, opacity, length]
    quants = [[quant_5, 0.6, 0.16], [quant_25, 0.8, 0.26], [quant_50, 1, 0.36],  [quant_75, 0.8, 0.46], [quant_95, 0.6, 0.56]]

        # Annotations (on tracer l'histogramme mais c'est juste pour récupérer la valeur ymax)
    y, x, _ = plt.hist(data)
    ymax = y.max()
    y1 = ymax*0.1  
    y2 = ymax*0.2  
    y3 = ymax*0.3  
    y4 = ymax*0.4  
    y5 = ymax*0.5  
    ax.text(quant_5-.1, y1, "5%t", size = 10, alpha = 0.8)
    ax.text(quant_25-.13, y2, "25%t", size = 11, alpha = 0.85)
    ax.text(quant_50-.13, y3, "50%t", size = 12, alpha = 1)
    ax.text(quant_75-.13, y4, "75%t", size = 11, alpha = 0.85)
    ax.text(quant_95-.25, y5, "95%t", size = 10, alpha =.8)

        # Tracé des pourcentiles en rouge
    for i in quants:
        ax.axvline(i[0], alpha = i[1], ymax = i[2], color='red', linestyle = ":")

        # Tracé de l'histogramme (pour écraser le 1er tracé de l'histogramme plus haut)
    plt.hist(data, color = "skyblue", ec="white") # Crée l'histogramme
    plt.title(feature)
    plt.show() # Affiche l'histogramme
    
    #Tracé du boxplot
    ax = plt.axes()
    plt.xticks(rotation=90)
    data = dataframe[feature]
    min_raw = round(dataframe[feature].min())
    min_r = round(min_raw, abs(1 - (len(str(min_raw)))))
    max_raw = round(dataframe[feature].max())
    max_r = round(max_raw, abs(1 - (len(str(max_raw)))))
    step = (max_r - min_r) / 20
    if (step != 0):
        plt.xticks(np.arange(min_r, max_r, step))
        red_circle = dict(markerfacecolor='red', marker='o', markeredgecolor='black')
        mean_shape = dict(markerfacecolor='green', marker='D', markeredgecolor='green')
        ax = sns.boxplot(x = data, orient="h", color='skyblue', flierprops=red_circle, showmeans=True, meanprops=mean_shape).set_title(feature);
    else:
        red_circle = dict(markerfacecolor='red', marker='o')
        mean_shape = dict(markerfacecolor='green', marker='D', markeredgecolor='green')
        plt.boxplot(x=dataframe[feature], vert=False, flierprops=red_circle, 
             showmeans=True, meanprops=mean_shape);


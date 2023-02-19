#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# On créé une fonction diminue la taille prise par des valeurs numériques en changeant le data type.
# les valeurs numériques en float64 seront converties en float32 grâce à downcast="float".
# les valeurs numériques en int64 seront converties en int32 grâce à downcast="integer".

def downcast_numerical_column_V2(df):
    for column in df:
        if df[column].dtype == 'float64':
            df[column]=pd.to_numeric(df[column], downcast="float")
        if df[column].dtype == 'int64':
            df[column]=pd.to_numeric(df[column], downcast="integer")


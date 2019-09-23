# Fase 5: Análisis de datos

# # imports 

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

import requests
import json
from bs4 import BeautifulSoup

import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# from loadCredentials import loadCredentials

from sklearn import svm
"""
from funciones_scraping import get_languages
from funciones_tiempo import timeit
from funciones_plot_confusion_matrix import plot_confusion_matrix

"""

pd.options.display.max_columns = None


# Cargamos el dataframe de resultante de data-cleaning
CLEAN_FILE_PATH = './output/codewar_users_clean.csv' 

df = pd.read_csv(CLEAN_FILE_PATH, index_col=0)
print(df.shape)


# 5.1 Correlación | heatmap

correlation = df.corr(method='pearson')

fig, ax = plt.subplots(figsize=(12,10)) 
ax = sns.heatmap(correlation, cmap="YlGnBu")

CORR_PNG = './output/corr.png'

fig.savefig(CORR_PNG)

# TO CONTINUE
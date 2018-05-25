#from openpyxl import load_workbook

import pandas as pd
import numpy as np
import csv

FILE_PATH = 'C:\\Users\\Lenovo\\Desktop\\embeddingscsv.csv'
SHEET = 'embeddings'

words = pd.read_table(FILE_PATH, sep=' ', index_col=0,header=None,quoting=csv.QUOTE_NONE,na_values=None,keep_default_na=False)

def vec(w):
    return words.loc[w].as_matrix()

words_matrix = words.as_matrix()

def find_closest_word(v):
    diff = words_matrix - v
    delta = np.sum(diff * diff, axis=1)
    i = np.argmin(delta)
    return words.iloc[i].name

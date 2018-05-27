#from openpyxl import load_workbook

import pandas as pd
import numpy 
import csv
import pickle

FILE_PATH = 'C:\\Users\\Lenovo\\Desktop\\embeddings.csv'
SHEET = 'embeddings'
### Manual
words = pd.read_csv(FILE_PATH, sep =',', delimiter = '\n')
def vec(w):
    return words.loc[w].as_matrix()

words_matrix = words.values

def find_closest_word(v):
    diff = words_matrix - v
    delta = np.sum(diff * diff, axis=1)
    i = np.argmin(delta)
    return words.iloc[i].name

def W2V(data):
    size = len(data)
    vectorialSpace = {}
    for i in range(size):
        fullVector = data.iloc[i].values[0].split(",")
        try:
            vectorialSpace[fullVector[0]] = numpy.array(list(map(float,fullVector[1:])))
        except:
            print(fullVector)
    fp = open("W2V.pickle", "wb")
    pickle.dump(vectorialSpace, fp)
    fp.close()

W2V(words)


        
    

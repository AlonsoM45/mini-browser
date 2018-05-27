import math
import CosineSimilarity as cs
import operator
import numpy as np
import queue as q
import pickle
from time import time

#INDEXING FUNCTIONS

def newDocumentIndex(document, indexIDF):
    words = document.split(" ")
    index = {}
    for w in words:
        countWord(index,indexIDF, w)
    return index

def countWord(index, indexIDF, word):
    index[word] = index.get(word, 0) 
    indexIDF[word] = indexIDF.get(word,0) + 1


#TF-IDF FUNCTIONS
def similarity(TF, IDF, words, nDocs):
    vectorA = q.Queue(maxsize = len(words))
    vectorB = q.Queue(maxsize = len(words))
    for w in words:
        valueTF = TF.get(w,0)
        valueIDF = IDF.get(w,0) +1
        vectorA.put(valueTF*(nDocs / valueIDF))
        vectorB.put( nDocs / valueIDF)
    vectorA = np.array(queueToList(vectorA))
    vectorB = np.array(queueToList(vectorB))
    return cs.cosSimilarity(vectorA, vectorB)

def queueToList(Q):
    L = []
    while(not Q.empty()):
        L.append(Q.get())
    return L

def sortedInsert(L, element, maxsize):
    i = 0
    while  i < len(L) and L[i][1] < element[1] :
        i = i + 1
    L.insert(i, element)
    diff = len(L) - maxsize
    if diff > 0:
        L = L[:diff]
    return L

def searchTFIDF(query, maxTFnumber, IDF, maxsize, maxTFsize=1000000):
    vectors = []
    words = query.split(" ")
    lowest = (0, 0)
    TFnumber = 0
    while TFnumber < maxTFnumber:        
        with open(str(TFnumber)+'.pickle', 'rb') as handle:
            TF = pickle.load(handle)
        lowest = 0
        for i in range(len(TF)):
            similarityDoc = similarity(TF[i],IDF, words, len(TF))
            if (similarityDoc >= lowest or len(vectors) < maxsize) and similarityDoc > 0.75:
                ID = maxTFsize * TFnumber + i
                vectors = sortedInsert( vectors, (ID, similarityDoc), maxsize)
                lowest = vectors[0][1]
        TFnumber = TFnumber + 1
        handle.close()
    vectors.reverse()
    print(vectors)
    return vectors


def searchTFIDF(query, maxTFnumber, IDF, maxsize, maxTFsize=1000000):
    vectors = q.Queue()
    words = query.split(" ")
    TFnumber = 0
    while TFnumber < maxTFnumber:        
        with open(str(TFnumber)+'.pickle', 'rb') as handle:
            TF = pickle.load(handle)
        for i in range(len(TF)):
            similarityDoc = similarity(TF[i],IDF, words, len(TF))
            if similarityDoc > 0.90:
                ID = maxTFsize * TFnumber + i
                vectors.put((ID, similarityDoc))
        TFnumber = TFnumber + 1
        handle.close()
        
    vectorType = [('id',int), ('similarity', float)]
    final = np.array(queueToList(vectors), dtype = vectorType)
    sortedList = np.sort(final, order = 'similarity')
    sortedList = sortedList[::-1]
    return sortedList

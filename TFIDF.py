import math
import CosineSimilarity as cs
import operator
import numpy as np
from textblob import TextBlob as tb
import queue as q

#INDEXING FUNCTIONS



def newDocumentIndex(document, indexIDF):
    words = document.split(" ")
    index = {}
    for w in words:
        countWord(index,indexIDF, w)
    return index

def countWord(index, indexIDF, word):
    index[word] = index.get(word, 0) + 1
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

def lowestSort(L, maxsize):
    L = sorted(L, key = lambda tup: tup[1], reverse = True)
    while len(L) > maxsize:
        del L[-1]
    return L, L[-1][0]
"""
def searchTFIDF(query, TF, IDF):
    vectors = {}
    words = query.split(" ")
    for i in range(len(TF)):
        similarityDoc = similarity(TF[i],IDF, words, len(TF))
        if (similarityDoc !=0):
            vectors[i] = similarityDoc
    sortedList = sorted(vectors.items(), key=operator.itemgetter(1), reverse=True)
    return sortedList
"""
def searchTFIDF(query, TF, IDF, maxsize):
    vectors = []
    words = query.split(" ")
    lowest = 0
    for i in range(len(TF)):
        similarityDoc = similarity(TF[i],IDF, words, len(TF))
        if similarityDoc > lowest:
            vectors.append( (i, similarityDoc))
            vectors, lowest = lowestSort(vectors, maxsize)
    return vectors

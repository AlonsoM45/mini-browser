import math
import CosineSimilarity as cs
import operator
import numpy as np
import queue as q
maxTFsize = 1000000
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

def sortedInsert(L, element):
    i = 0
    while  i < len(L) and L[i] < element :
        i = i + 1
    L.insert(i, element)
    diff = len(L) - maxsize
    if diff > 0:
        L = L[:diff]
    return L
    
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
    lowest = (0, 0)
    for i in range(len(TF)):
        similarityDoc = similarity(TF[i],IDF, words, len(TF))
        if similarityDoc > lowest[1] or len(vectors) < maxsize:
            L = sortedInsert( vectors, (i, similarityDoc))
            lowest = L[0]
    vectors.reverse()
    return vectors

def searchTFIDF(query, maxTFnumber, IDF, maxsize, maxTFsize):
    vectors = []
    words = query.split(" ")
    lowest = (0, 0)
    TFnumber = 0
    while TFnumber <= maxTFnumber:        
        with open('filename.pickle', 'rb') as handle:
            TF = pickle.load(handle)
        for i in range(len(TF)):
            similarityDoc = similarity(TF[realIndex],IDF, words, len(TF))
            if similarityDoc > lowest[1] or len(vectors) < maxsize:
                ID = maxTFsize * TFnumber + i
                vectors = sortedInsert( vectors, (ID, similarityDoc))
                lowest = vectors
    vectors.reverse()
    return vectors

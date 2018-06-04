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
    index[word] = index.get(word, 0) + 1
    indexIDF[word] = indexIDF.get(word,0) + 1


#TF-IDF FUNCTIONS
def similarity(TF, IDF, words, queryVector, nDocs):
    vectorA = map(lambda w: TF.get(w,0) *(nDocs /  (IDF.get(w,0) + 1) ), words)
    vectorA = np.array(list(vectorA))
    return cs.cosSimilarity(vectorA, queryVector)

def vectorize(IDF, query, nDocs):
    return np.array(list(map(lambda x: nDocs/ (IDF.get(x, 0) + 1), query.split())))
    
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

def searchTFIDF(query, maxTFnumber, IDF, maxsize, maxTFsize=100000):
    vectors = q.Queue()
    words = query.split(" ")
    TFnumber = 0
    queryVector = vectorize(IDF, query, maxTFnumber * maxTFsize)
    print (maxTFnumber)
    while TFnumber < maxTFnumber:
        
        with open(str(TFnumber)+'.pickle', 'rb') as handle:
            TF = pickle.load(handle)
        for i in range(len(TF)):
            similarityDoc = similarity(TF[i],IDF, words, queryVector, len(TF))
            if similarityDoc > 0.5:
                ID = maxTFsize * TFnumber + i
                vectors.put((ID, similarityDoc))
        TFnumber = TFnumber + 1
        handle.close()
    vectorType = [('id',int), ('similarity', float)]
    final = np.array(queueToList(vectors), dtype = vectorType)
    sortedList = np.sort(final, order = 'similarity')
    sortedList = sortedList[::-1]
    return sortedList

def probTFIDF(query, maxTFnumber, IDF, maxsize, maxTFsize=100000, parts = 70):
    vectors = q.Queue()
    words = query.split(" ")
    TFnumber = 0
    queryVector = vectorize(IDF, query, maxTFnumber * maxTFsize)
    while TFnumber < maxTFnumber:        
        with open(str(TFnumber)+'.pickle', 'rb') as handle:
            TF = pickle.load(handle)
        for i in np.random.choice(len(TF), int(len(TF)*parts/100), replace = False):
            similarityDoc = similarity(TF[i], IDF, words, queryVector, len(TF))
            if similarityDoc > 0.5:
                ID = maxTFsize * TFnumber + i
                vectors.put((ID, similarityDoc))
        TFnumber = TFnumber + 1
        handle.close()
    vectorType = [('id',int), ('similarity', float)]
    final = np.array(queueToList(vectors), dtype = vectorType)
    sortedList = np.sort(final, order = 'similarity')
    sortedList = sortedList[::-1]
    return sortedList

def extendQuery(query, number, W2V):
    extended = ""
    for word in query.split():
        for nextWord in selectNearest(word, number, W2V):
            extended = extended +  " " + nextWord[0]
    return extended + " " + query

def selectNearest(word, number, W2V):
    nearest = q.Queue()
    wordVector = W2V.get(word, 0)
    if wordVector == 0:
        return []
    for entry in W2V:
        nearest.put( (entry, cs.cosSimilarity(wordVector, W2V[entry])))
    print('HERE')
    nearest = queueToList(nearest)
    nearest.sort(reverse = True, key = lambda x: x[1])
    return nearest[:number]

import math
import CosineSimilarity as cs
import operator
import numpy as np

#INDEXING FUNCTIONS
def newIndex(documents):
    indexTF  = []
    indexIDF = {}
    for doc in documents:
        newIndex = newDocumentIndex(doc)
        indexTF.append(newIndex)
        for k in newIndex.keys():
            countWord(indexIDF, k)
    return indexTF, indexIDF

def newDocumentIndex(document):
    words = document.split(" ")
    index = {}
    for w in words:
        countWord(index, w)
    return index

def countWord(index, word):
    try:
        index[word] = index[word] + 1
    except:
        index[word] = 1

#TF-IDF FUNCTIONS
def similarity(TF, IDF, words, nDocs):
    vector = []
    for w in words:
        try:
            valueTF = TF[w]
        except:
            valueTF = 0
        try:
            valueIDF = IDF[w] +1
        except:
            valueIDF = 1
        vector.append(valueTF*(nDocs / valueIDF))
    #vectorB = np.array(list(map(lambda x: TF[x] * IDF[x], words)))
    return vector

def searchTFIDF(query, documents):
    nDocs = len(documents)
    TF, IDF = newIndex(documents)
    vectors = {}
    words = query.split(" ")
    for i in range(len(documents)):
        vectors[i] = similarity(TF[i],IDF, words, nDocs)
    sortedList = sorted(vectors.items(), key=operator.itemgetter(1), reverse=True)
    return sortedList

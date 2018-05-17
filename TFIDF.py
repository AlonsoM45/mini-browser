import math
import CosineSimilarity as cs
import operator
import numpy as np

#INDEXING FUNCTIONS
def newIndex(documents):
    indexTF  = []
    indexIDF = {}
    for doc in documents:
        newIndex = newDocumentIndex(doc[0])
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
    vectorA = []
    vectorB = []
    for w in words:
        try:
            valueTF = TF[w]
        except:
            valueTF = 0
        try:
            valueIDF = IDF[w] +1
        except:
            valueIDF = 1
        vectorA.append(valueTF*(nDocs / valueIDF))
        vectorB.append( nDocs / valueIDF)    
    vectorA = np.array(vectorA)
    vectorB = np.array(vectorB)
    return cs.cosSimilarity(vectorA, vectorB)

def searchTFIDF(query, TF, IDF):
    vectors = {}
    words = query.split(" ")
    for i in range(len(TF)):
        similarityDoc = similarity(TF[i],IDF, words, len(TF))
        if (similarityDoc !=0):
            vectors[i] = similarityDoc
    sortedList = sorted(vectors.items(), key=operator.itemgetter(1), reverse=True)
    return sortedList

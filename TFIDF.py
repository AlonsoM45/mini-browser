import math
import CosineSimilarity as cs
import operator
import numpy as np
from textblob import TextBlob as tb

def newIndex(documents):
    indexTF  = []
    indexIDF = {}
    for doc in documents:
        newIndex = newDocumentIndex(doc)
        indexTF.append(newIndex)
        for k in newIndex.keys():
            addWord(indexIDF, k)
    return indexTF, indexIDF

    
def newDocumentIndex(document):
    words = document.split(" ")
    index = {}
    for word in words:
        addWord(index, word)
    return index


def addWord(index, word):
    try:
        index[word] = index[word] + 1
    except:
        index[word] = 1

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(TF, IDF, word):
    return tf(word, blob) * idf(word, bloblist)

def similarity(TF, IDF, words):
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
        vector.append(valueTF*valueIDF)
    #vectorB = np.array(list(map(lambda x: TF[x] * IDF[x], words)))
    print(vector)
    return vector

def searchTFIDF(query, documents):
    TF, IDF = newIndex(documents)
    vectors = {}
    words = query.split(" ")
    for i in range(len(documents)):
        vectors[i] = similarity(TF[i],IDF, words)
    print(vectors)
    sortedList = sorted(vectors.items(), key=operator.itemgetter(1), reverse=True)
    print(sortedList)
    return sortedList

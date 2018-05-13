import math
import operator
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)




def searchIFIDF(documents, query):
    similarity = {}
    bloblist =[]
    bloblist += tbDocuments(documents)
    words = query.split(" ")
    for i in range(len(bloblist)):
        v =  list(map( lambda x: tfidf(x, bloblist[i], bloblist), words))
        cant = 0.0
        for num in v:
            cant += num
        similarity[i] = cant
    sortedList = sorted(similarity.items(), key=operator.itemgetter(1), reverse=True)
    return sortedList
    
def tbDocuments(documents):
    bloblist = []
    for doc in documents:
        bloblist += [tb(doc)]
    return bloblist



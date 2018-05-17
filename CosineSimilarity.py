from numpy import dot 
from numpy.linalg import norm as magnitude

def cosSimilarity(A, B):
    dotProduct = dot(A,B)
    magnitudeA = magnitude(A)
    magnitudeB = magnitude(B)
    if dotProduct != 0:
        return dotProduct / (magnitudeA * magnitudeB)
    else:
        return 0


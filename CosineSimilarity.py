from numpy import dot 
from numpy.linalg import norm as magnitude

def cosSimilarity(A, B):
    dotProduct = dot(A,B)
    magnitudeA = magnitude(A)
    magnitudeB = magnitude(B)
    return dotProduct / (magnitudeA * magnitudeB)


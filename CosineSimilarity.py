from numpy import dot 
from numpy.linalg import norm as magnitude

def cosSimilarity(A, B):
    dotProduct = dot(A,B)
    if dotProduct != 0:
        return dotProduct / (magnitude(A) * magnitude(B))
    else:
        return 0


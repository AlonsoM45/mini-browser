from os import walk, getcwd, path
import pyodbc
from TFIDF import newDocumentIndex,countWord

def newIndex(ruta = getcwd()):
    indexTF  = []
    indexIDF = {}
    cantDocuments = 0
    for (root, _, archivos) in walk(ruta+"\\TXT"):
        for archivo in archivos:
            cantDocuments+=1
            pathText = path.join(root, archivo)
            text = cargarArchivo(pathText)
            newIndex = newDocumentIndex(text)
            indexTF.append(newIndex)
            for k in newIndex.keys():
                countWord(indexIDF, k)
    return indexTF, indexIDF, cantDocuments


def buscarArchivo(searched):
    ruta = getcwd()
    for (root, _, archivos) in walk(ruta+"\\TXT"):
        for archivo in archivos:
            if(archivo == searched):
                pathText = path.join(root, searched)
                return cargarArchivo(pathText)

def cargarArchivo(archivo):
    fo = open(archivo, "r") 
    resultado = fo.read()
    fo.close()
    return str(resultado)


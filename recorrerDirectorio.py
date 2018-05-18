from os import walk, getcwd, path
import pyodbc
from TFIDF import newDocumentIndex


def newIndex(ruta = getcwd()):
    paths = []
    indexTF  = []
    indexIDF = {}
    for (root, _, archivos) in walk(ruta+"\\TXT"):
        for archivo in archivos:
            pathText = path.join(root, archivo)
            paths.append(pathText)
            text = cargarArchivo(pathText)
            newIndex = newDocumentIndex(text, indexIDF)
            indexTF.append(newIndex)
    return indexTF, indexIDF, paths


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


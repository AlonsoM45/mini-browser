from os import walk, getcwd, path
import pyodbc
import json
from TFIDF import newDocumentIndex
import numpy as np


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
    guardar(indexTF,indexIDF, paths)
    return indexTF, indexIDF, paths


def buscarArchivo(searched):
    ruta = getcwd()
    for (root, _, archivos) in walk(ruta+"\\TXT"):
        for archivo in archivos:
            if(archivo == searched):
                pathText = path.join(root, searched)
                return cargarArchivo(pathText)

def cargarArchivo(archivo):
    fo = open(archivo) 
    resultado = fo.readline()
    fo.close()
    return str(resultado)

def guardar (indexTF, indexIDF, paths):
    fo = open("indexTF.JSON", "w") #abre en forma de sobrrescribirlo, si no existe lo crea
    TF = json.dumps(indexTF)
    fo.write(TF)
    fo.close()
    fo = open("indexIDF.JSON", "w") #abre en forma de sobrrescribirlo, si no existe lo crea
    IDF = json.dumps(indexIDF)
    fo.write(IDF)
    fo.close()
    fo = open("paths.JSON", "w") #abr en forma de sobrrescribirlo, si no existe lo crea
    PATHS = json.dumps(paths)
    fo.write(PATHS)
    fo.close()

def cargarJSON():
    fo = open("indexTF.JSON", "r") 
    TF = json.loads(fo.read())
    fo.close()
    fo = open("indexIDF.JSON", "r") 
    ITF = json.loads(fo.read())
    fo.close()
    fo = open("paths.JSON", "r") 
    PATHS = json.loads(fo.read())
    fo.close()
    return TF, ITF, PATHS



from os import walk, getcwd, path
import json
from TFIDF import newDocumentIndex
import numpy as np
import threading
import pickle
threadCount = 0

def newIndex(ruta = getcwd()):
    paths = []
    indexTF  = []
    indexIDF = {}
    TFsize = 0
    TFnumber = 0
    totalSize = 0
    for (root, _, archivos) in walk(ruta+"\\TXT"):
        for archivo in archivos:
            pathText = path.join(root, archivo)
            paths.append(pathText)
            text = cargarArchivo(pathText)
            newIndex = newDocumentIndex(text, indexIDF)
            indexTF.append(newIndex)
            TFsize = TFsize  + 1
            if TFsize == 1000000:
                with open(str(TFnumber)+'.pickle', 'wb') as handle:
                    pickle.dump(indexTF, handle, protocol=pickle.HIGHEST_PROTOCOL)
                    TFnumber = TFnumber  + 1
                    indexTF = []
                    TFsize = 0
                    handle.close()
        if TFsize > 0:
            with open(str(TFnumber)+'.pickle', 'wb') as handle:
                pickle.dump(indexTF, handle, protocol=pickle.HIGHEST_PROTOCOL)
                TFnumber = TFnumber  + 1
                indexTF  = []
                TFsize   = 0
                handle.close()
    guardar(indexIDF, paths)
    return indexIDF, paths, TFnumber 

def cargarArchivo(archivo):
    fo = open(archivo) 
    resultado = fo.readline()
    fo.close()
    return str(resultado)

def guardar (indexIDF, paths):
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



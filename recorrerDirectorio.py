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
                    print (TFnumber)
        if TFsize > 0:
            with open(str(TFnumber)+'.pickle', 'wb') as handle:
                pickle.dump(indexTF, handle, protocol=pickle.HIGHEST_PROTOCOL)
                TFnumber = TFnumber  + 1
                indexTF  = []
                TFsize   = 0
                handle.close()
                
    
    guardar(indexIDF, paths,  TFnumber )
    return indexIDF, paths, TFnumber 

def cargarArchivo(archivo):
    fo = open(archivo) 
    resultado = fo.readline()
    fo.close()
    return str(resultado)

def guardar (indexIDF, paths,TFnumber ):
    fo = open("indexIDF.JSON", "w") #abre en forma de sobrrescribirlo, si no existe lo crea
    IDF = json.dumps(indexIDF)
    fo.write(IDF)
    fo.close()
    fo = open("paths.JSON", "w") #abr en forma de sobrrescribirlo, si no existe lo crea
    PATHS = json.dumps(paths)
    fo.write(PATHS)
    fo.close()
    fo = open("TFnumber.JSON", "w") #abr en forma de sobrrescribirlo, si no existe lo crea
    TFNUMBER = json.dumps(TFnumber)
    fo.write(TFNUMBER)
    fo.close()

def cargarJSON():
    fo = open("indexIDF.JSON", "r") 
    ITF = json.loads(fo.read())
    fo.close()
    fo = open("paths.JSON", "r") 
    PATHS = json.loads(fo.read())
    fo.close()
    fo = open("TFnumber.JSON", "r") 
    TFNUMBER = json.loads(fo.read())
    fo.close()
    return ITF, PATHS, TFNUMBER


def newIndex2(ruta = getcwd()):
    paths = []
    indexTF  = []
    indexIDF = {}
    TFsize = 0
    Times =0
    Documents = 0
    TFnumber = 0
    while(Documents < 100000):
        pathText = path.join("C:\\Users\\Virtual\\Documents\\TXT\\", str(Times)+".txt")
        try:
            text = cargarArchivo(pathText)
            paths.append(pathText)
            newIndex = newDocumentIndex(text, indexIDF)
            indexTF.append(newIndex)
            Documents += 1
            TFsize  += 1
        except:
            pass
        Times +=1
        if TFsize == 10000:
            with open(str(TFnumber)+'.pickle', 'wb') as handle:
                print (TFnumber)
                pickle.dump(indexTF, handle, protocol=pickle.HIGHEST_PROTOCOL)
                TFnumber  += 1
                indexTF = []
                TFsize = 0
                handle.close()
                
    if TFsize > 0:
        with open(str(TFnumber)+'.pickle', 'wb') as handle:
            pickle.dump(indexTF, handle, protocol=pickle.HIGHEST_PROTOCOL)
            TFnumber +=  1
            indexTF  = []
            TFsize   = 0
            handle.close()

    guardar(indexIDF, paths,  TFnumber )
    return indexIDF, paths, TFnumber 
import json
import os
import shutil
import FormatJSON as RJ
def readJSON(filename):
    RJ.formatJSON(filename)
    try:
        shutil.rmtree("TXT")
        os.makedirs("TXT")
    except:
        print ("No se pudo compa")
    with open(filename) as file:
        data = json.load(file)
        for entry in data:
            #print(entry["reviewText"])
            outFile = open("TXT\\"+ entry["asin"]+".txt", "w")
            outFile.write(entry["reviewText"])
            outFile.close
readJSON("C:\\Users\\Rubén González V\\OneDrive\\TEC\\3 Semestre\\Analisis de Algoritmos\\mini-browser\\100000.json")
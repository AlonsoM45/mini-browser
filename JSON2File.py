import json
import os
import shutil
import FormatJSON as RJ
def readJSON(filename):
    RJ.formatJSON(filename)
    try:
        shutil.rmtree("TXT")
    except:
        print ("No se pudo borrar")
    os.makedirs("TXT")
    with open(filename) as file:
        data = json.load(file)
        for i,entry in enumerate(data):
            outFile = open("TXT\\"+ str(i)+".txt", "w")
            outFile.write(entry["reviewText"])
            outFile.close
readJSON("C:\\Users\\Rubén González V\\Desktop\\mini-browser\\10000.json")
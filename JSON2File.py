import json
import os
import shutil

import gzip

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


def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)
def read():
    os.makedirs("TXT")
    i=0
    for review in parse("C:\\Users\\Rubén González V\\Desktop\\mini-browser\\reviews_Books.json.gz"):
        outFile = open("TXT\\"+ str(i)+".txt", "w")
        outFile.write(review['reviewText'])
        outFile.close
        i +=1

#read()

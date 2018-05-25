import json
import os
import shutil

import gzip

import FormatJSON as RJ
def readJSON(filename):
    #RJ.formatJSON(filename)
    try:
       shutil.rmtree("TXT")
    except:
       print ("No se pudo borrar")
    os.makedirs("TXT")
    with open(filename) as file:
        data = json.load(file)
        i= 0
        for review in data:
            outFile = open("TXT\\"+ str(i)+".txt", "w")
            outFile.write(review['reviewText'])
            outFile.close
            i +=1
readJSON("C:\\Users\\Virtual\\Documents\\GitHub\\mini-browser\\1000.json")


def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)
def read():
    os.makedirs("TXTA")
    i = 19787777
    for review in parse("C:\\Users\\Virtual\\Documents\\reviews_Books.json.gz"):
        outFile = open("TXTA\\"+ str(i)+".txt", "w")
        outFile.write(review['reviewText'])
        outFile.close
        i +=1

#read()

import json
import ReadJSON as RJ
def readJSON(filename):
    RJ.formatJSON(filename)
    with open(filename) as file:
        data = json.load(file)
        for entry in data:
            #print(entry["reviewText"])
            outFile = open( entry["asin"], "w")
            outFile.write(entry["reviewText"])
            outFile.close

import os

def formatJSON(fname, copy = False):
    try:
        inFile = open(fname, "r")
        outFile = open( fname + ".copy", "w")
        outFile.write("[")
        lines = inFile.readlines()
        if lines[0][0] == "[":
            inFile.close()
            outFile.close()
            os.remove(fname + ".copy")
            return True
        for line in lines:
            if line == lines[-1]:
                newline = line.replace("}","}]")
            else:
                newline = line.replace("}","},")
            outFile.write(newline)
        inFile.close()
        outFile.close()
        if not copy:
            os.remove(fname)
            os.rename(fname + ".copy", fname)
        return True
    except:
        return False

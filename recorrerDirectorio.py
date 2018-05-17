from os import walk, getcwd, path

def ls(ruta = getcwd()):
    listaarchivos = []
    for (root, _, archivos) in walk(ruta+"\\TXT"):
        for archivo in archivos:
            pathText = path.join(root, archivo)
        listaarchivos.extend(archivos)
    return listaarchivos

def buscarArchivo(searched):
    ruta = getcwd()
    listaarchivos = []
    for (root, _, archivos) in walk(ruta+"\\TXT"):
        for archivo in archivos:
            if(archivo == searched):
                pathText = path.join(root, searched)
                return cargarArchivo(pathText)

def cargarArchivo(archivo):
    fo = open(archivo, "r") 
    resultado = fo.read()
    fo.close()
    return resultado

ls()


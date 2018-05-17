from os import walk, getcwd

def ls(ruta = getcwd()):
    listaarchivos = []
    for (_, _, archivos) in walk(ruta+"\\TXT"):
        print (archivos)
        #for archivo in archivos:
            
        listaarchivos.extend(archivos)
    return listaarchivos

ls()

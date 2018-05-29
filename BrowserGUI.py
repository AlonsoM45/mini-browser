from tkinter import *
import tkinter
from random import choice
from TFIDF import searchTFIDF, probTFIDF
from recorrerDirectorio import newIndex, cargarArchivo, cargarJSON
from time import time

class menu(tkinter.Tk):
    def __init__(menu):
        tkinter.Tk.__init__(menu)
        menu.title("Mini Google")
        menu.geometry("500x200")

        lbl1= Label(menu, text= "Path:", font="20")
        lbl1.place(x=20, y= 20)

        menu.btnNormalIndex= Button(menu, text="Usar 2 Millones", width=20, heigh=2, command=normalIndex)
        menu.btnNormalIndex.place(x=300, y=100)
        menu.btnNewIndex= Button(menu, text="Indexar Nuevo", width=20, heigh=2, command= NewIndex)
        menu.btnNewIndex.place(x=300, y=10)
        menu.textBoxPath = Entry(menu, width=30)
        menu.textBoxPath.place(x=100, y= 20)

class self(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Mini Google")
        self.geometry("1150x550")

        lbl1= Label(self, text= "Texto:", font="20")
        lbl1.place(x=70, y= 10)
        lbl2= Label(self, text= "Cantidad de Resultados: ", font="20")
        lbl2.place(x=15, y= 75)
        lbl3= Label(self, text= "Exactitud Probabilístico: ", font="20")
        lbl3.place(x=15, y= 275)
        #TextBox
        self.textBoxSearch = Entry(self, width=30)
        self.textBoxSearch.place(x=15, y= 50)
        self.textBoxQuantity = Entry(self, width=30)
        self.textBoxQuantity.place(x=15, y= 110)
        self.textBoxProb = Entry(self, width=30)
        self.textBoxProb.place(x=15, y= 315)
        checkBox = 0
        self.checkW2V = Checkbutton(self, text="Word 2 Vec", variable=checkBox,  font="20")
        self.checkW2V.place(x= 50, y =140)
        #Button
        self.btnNormalSearch= Button(self, text="Buscar Normal", width=20, heigh=2, command=self.normalSearch)
        self.btnNormalSearch.place(x=20, y=200)
        self.btnProbSearch= Button(self, text="Buscar Probabilistico",width=20, heigh=2,command= self.probSearch)
        self.btnProbSearch.place(x=20, y=350)
        self.btnViewDocument= Button(self, text="Ver Documento",width=20, heigh=2,command= self.viewDocument)
        self.btnViewDocument.place(x=850, y=20)
        #ListBox
        self.scrollbarList = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self, yscrollcommand=self.scrollbarList.set ,width=70, heigh=30)
        self.scrollbarList.config(command=self.listbox.yview)
        self.scrollbarList.pack(side=LEFT, fill=Y)
        self.listbox.place(x=250, y=10)
        
        #TextArea
        self.scrollbarText = Scrollbar(self, orient=VERTICAL)
        self.textArea = Text(self,width=50, heigh=25,yscrollcommand=self.scrollbarText.set)
        self.scrollbarText.config(command=self.textArea.yview)
        self.scrollbarText.pack(side=RIGHT, fill=Y)
        self.textArea.place(x=700, y=90)

        #List
        self.list = []
        

    def normalSearch(self):
        global IDF, paths, totalSize 
        query = self.textBoxSearch.get()
        quantity = self.textBoxQuantity.get()
        self.listbox.delete(0, END)
        self.list =[]
        inicial = time()
        #result = searchTFIDF(query, TF, IDF, int(quantity))
        print (totalSize)
        result = searchTFIDF(query, totalSize, IDF, int(quantity))
        final = time()
        print ("Duró buscando: "+str(final - inicial)+" segundos")
        
        realQuantity = min(int(quantity), len(result))
        #arreglar
        
        for x in range(int(realQuantity)):
            doc = cargarArchivo(paths[result[x][0]])
            self.list += [doc]
            self.listbox.insert(END, doc)

    def probSearch(self):
        global IDF, paths, totalSize
        query = self.textBoxSearch.get()
        quantity = self.textBoxQuantity.get()
        self.listbox.delete(0, END)
        self.list =[]
        inicial = time()
        #result = searchTFIDF(query, TF, IDF, int(quantity))
        result = probTFIDF(query, totalSize, IDF, int(quantity))
        final = time()
        print ("Duró buscando: "+str(final - inicial)+" segundos")
        
        realQuantity = min(int(quantity), len(result))
        #arreglar
        
        for x in range(int(realQuantity)):
            doc = cargarArchivo(paths[result[x][0]])
            self.list += [doc]
            self.listbox.insert(END, doc)
    
    def viewDocument(self):
        index = self.listbox.curselection()
        self.textArea.delete(1.0, END)
        self.textArea.insert(END, self.list[int(index[0])])





def normalIndex():
    global IDF, paths, totalSize
    inicial = time()
    IDF, paths, totalSize = cargarJSON()
    final = time()
    print ("Duró indexando: "+str(final - inicial)+" segundos")
    self().mainloop()
    

def NewIndex():
    global IDF, paths, totalSize
    path =  menu.textBoxPath.get()
    inicial = time()
    IDF, paths, totalSize = newIndex(path)
    final = time()
    print ("Duró indexando: "+str(final - inicial)+" segundos")
    self().mainloop()
    




    


menu().mainloop()


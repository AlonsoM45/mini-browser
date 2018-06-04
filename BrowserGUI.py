from tkinter import *
import tkinter
from random import choice
from TFIDF import searchTFIDF, probTFIDF, extendQuery
from recorrerDirectorio import newIndex, cargarArchivo, cargarJSON
from time import time
import pickle

class menu(tkinter.Tk):
    def __init__(menu):
        tkinter.Tk.__init__(menu)
        menu.title("Mini Google")
        menu.geometry("600x200")

        lbl1= Label(menu, text= "Path:", fg = "antique white", bg = "IndianRed4", font = ("Courier", 12))
        lbl1.place(x=20, y= 20)
        menu.configure(background='IndianRed4')

        menu.btnNormalIndex= Button(menu, text="Usar 2 Millones", fg = "antique white", bg = "salmon4", font = ("Courier", 12), width=20, heigh=2, command=normalIndex)
        menu.btnNormalIndex.place(x=300, y=100)
        menu.btnNewIndex= Button(menu, text="Indexar Nuevo",  fg = "antique white", bg = "salmon4", font = ("Courier", 12), width=20, heigh=2, command= menu.NewIndex)
        menu.btnNewIndex.place(x=300, y=10)
        menu.textBoxPath = Entry(menu, width=30)
        menu.textBoxPath.place(x=100, y= 20)

    def NewIndex(menu):
        global IDF, paths, totalSize, W2V
        path =  menu.textBoxPath.get()
        print (path)
        inicial = time()
        IDF, paths, totalSize = newIndex(path)
        final = time()
        print ("Duró indexando: "+str(final - inicial)+" segundos")
        W2V = LoadW2V()
        self().mainloop()

class self(tkinter.Tk):
    def __init__(self):
        global checkBox
        tkinter.Tk.__init__(self)
        self.title("Mini Google")
        self.geometry("1150x550")
        self.configure(background = "IndianRed4")

        lbl1= Label(self, text= "Texto:", fg = "antique white", bg = "IndianRed4", font = ("Courier", 11))
        lbl1.place(x=60, y= 10)
        lbl2= Label(self, text= "Cantidad de Resultados: ", fg = "antique white", bg = "IndianRed4", font = ("Courier", 11))
        lbl2.place(x=35, y= 75)
        lbl3= Label(self, text= "Exactitud: ", fg = "antique white", bg = "IndianRed4", font = ("Courier", 11))
        lbl3.place(x=60, y= 275)
        lbl4= Label(self, text="Resultados",width=40,fg = "antique white", bg = "IndianRed4", font = ("Courier", 13))
        lbl4.place(x=300, y=20)
        #TextBox
        self.textBoxSearch = Entry(self, width=30)
        self.textBoxSearch.place(x=40, y= 50)
        self.textBoxQuantity = Entry(self, width=30)
        self.textBoxQuantity.place(x=40, y= 110)
        self.textBoxProb = Entry(self, width=30)
        self.textBoxProb.place(x=40, y= 315)
        #Button
        self.btnNormalSearch= Button(self, text="Búsqueda Normal", width=30, heigh=2, command=self.normalSearch, fg = "antique white", bg = "salmon4", font = ("Courier", 10))
        self.btnNormalSearch.place(x=25, y=200)
        self.btnProbSearch= Button(self, text="Búsqueda Probabilística",width=30, heigh=2,command= self.probSearch, fg = "antique white", bg = "salmon4", font = ("Courier", 10))
        self.btnProbSearch.place(x=25, y=350)
        self.btnViewDocument= Button(self, text="Ver Documento",width=40, heigh=2,command= self.viewDocument,  fg = "antique white", bg = "salmon4", font = ("Courier", 11))
        self.btnViewDocument.place(x=740, y=20)
        #ListBox
        self.scrollbarList = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self,width=40, heigh=24, yscrollcommand=self.scrollbarList.set , font = ("Courier", 11))
        self.scrollbarList.config(command=self.listbox.yview)
        self.scrollbarList.pack(side=LEFT, fill=Y)
        self.listbox.place(x=310, y=90)
        
        #TextArea
        self.textArea = Text(self,width=40, heigh=25, font = ("Courier", 11))
        self.scrollbarText = Scrollbar(self, orient=VERTICAL)
        self.textArea.configure(yscrollcommand=self.scrollbarText.set)
        self.scrollbarText.config(command=self.textArea.yview)
        self.scrollbarText.pack(side=RIGHT, fill=Y)
        self.textArea.place(x=740, y=90)

        #List
        self.list = []
        self.checkbox = BooleanVar(self)
        self.checkW2V = Checkbutton(self, text="Word 2 Vec", variable=self.checkbox,command=self.checkbox_clicked, fg = "antique white", bg = "IndianRed4", font = ("Courier", 11))
        self.checkW2V.place(x= 50, y =140)
        
    def checkbox_clicked(self):
        print(self.checkbox.get())
        
    def normalSearch(self):
        global IDF, paths, totalSize, W2V
        query = self.textBoxSearch.get()
        quantity = self.textBoxQuantity.get()
        self.listbox.delete(0, END)
        self.list =[]
        inicial = time()
        #result = searchTFIDF(query, TF, IDF, int(quantity))
        print (totalSize)
        
        

        if self.checkbox.get() == 1 :
            query = extendQuery(query, 2, W2V, IDF)
            print (query)
            
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
        global IDF, paths, totalSize, W2V, checkBox
        query = self.textBoxSearch.get()
        quantity = int(self.textBoxQuantity.get())
        correctness = int(self.textBoxProb.get())
        
        self.listbox.delete(0, END)
        self.list =[]
        inicial = time()
        #result = searchTFIDF(query, TF, IDF, int(quantity))

        if self.checkbox.get() == 1 :
            query = extendQuery(query, 2, W2V, IDF)
            print (query)
        
        result = probTFIDF(query, totalSize, IDF, quantity, correctness )
        final = time()
        print ("Duró buscando: "+str(final - inicial)+" segundos")
        
        realQuantity = min(quantity, len(result))
        #arreglar
        
        for x in range(int(realQuantity)):
            doc = cargarArchivo(paths[result[x][0]])
            self.list += [doc]
            self.listbox.insert(END, doc)
    
    def viewDocument(self):
        index = self.listbox.curselection()
        self.textArea.delete(1.0, END)
        self.textArea.insert(END, self.list[int(index[0])])



W2V = {}

def normalIndex():
    global IDF, paths, totalSize, W2V
    inicial = time()
    IDF, paths, totalSize = cargarJSON()
    final = time()
    print ("Duró indexando: "+str(final - inicial)+" segundos")
    W2V = LoadW2V()
    self().mainloop()
    


    
def LoadW2V():
    fp = open("W2V.pickle", "rb")
    W2V = pickle.load(fp)
    fp.close()
    return W2V



    


menu().mainloop()


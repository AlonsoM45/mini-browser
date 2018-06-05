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
        menu.geometry("500x200")
        w = Canvas(menu, width=500, height=200,bg ='#d4d4d4')
        w.pack()
        w.create_line(0, 90, 500, 90)


        lbl1= Label(menu, text= "Path:", bg ='#d4d4d4', font = ("Serif", 12))
        lbl1.place(x=25, y= 30)
        menu.configure(background='#d4d4d4')
        

        menu.btnNormalIndex= Button(menu, text="Usar 2 Millones", fg = "white", bg = "#176BEF", font = ("Serif", 12), width=20, heigh=3, command=normalIndex)
        menu.btnNormalIndex.place(x=150, y=110)
        menu.btnNewIndex= Button(menu, text="Indexar Nuevo",  fg = "white", bg = "#176BEF", font = ("Serif", 12), width=20, heigh=3, command= menu.NewIndex)
        menu.btnNewIndex.place(x=300, y=10)
        menu.textBoxPath = Entry(menu, width=30)
        menu.textBoxPath.place(x=100, y= 30)

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
        self.geometry("950x600")
        w = Canvas(self, width=950, height=600)#,bg ='#d4d4d4')
        
        w.create_rectangle(370, 65, 890, 135, width = 1)
        w.create_rectangle(20, 5, 890, 135, width = 2)
        w.create_rectangle(20, 65, 370, 135, width = 1)

        lbl1= Label(self, text= "Texto:", fg = "#4285f4",  font = ("Serif", 14))
        lbl1.place(x=60, y= 20)
        lbl2= Label(self, text= "Cantidad de Resultados: ", fg =  "#4285f4", font = ("Serif", 14))
        lbl2.place(x=420, y= 20)
        lbl3= Label(self, text= "Exactitud: ", fg = "#4285f4",  font = ("Serif", 14))
        lbl3.place(x=400, y= 90)
        #lbl4= Label(self, text="Resultados",width=40,fg = "antique white", bg = "IndianRed4", font = ("Courier", 13))
        #lbl4.place(x=500, y=20)
        #TextBox

        self.textBoxSearch = Entry(self, width=25, font = ("Serif", 13))
        self.textBoxSearch.place(x=150, y= 20)
        self.textBoxQuantity = Entry(self, width=7, font = ("Serif", 13))
        self.textBoxQuantity.place(x=650, y= 20)
        self.textBoxProb = Entry(self, width=7, font = ("Serif", 13))
        self.textBoxProb.place(x=500, y= 90)
        
        #Button
        self.btnNormalSearch= Button(self, text="Búsqueda Normal", width=30, heigh=2, command=self.normalSearch, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.btnNormalSearch.place(x=60, y=75)
        self.btnProbSearch= Button(self, text="Búsqueda Probabilística",width=30, heigh=2,command= self.probSearch, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.btnProbSearch.place(x=600, y=75)
        self.btnViewDocument= Button(self, text="Ver",width=7, heigh=2,command= self.viewDocument, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.btnViewDocument.place(x=440, y=300)
        
        #ListBox
        self.scrollbarList = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self,width=43, heigh=20, yscrollcommand=self.scrollbarList.set , font = ("Courier", 11))
        self.scrollbarList.config(command=self.listbox.yview)
        self.scrollbarList.pack(side=LEFT, fill=Y)
        self.listbox.place(x=30, y=150)
        
        #TextArea
        self.textArea = Text(self,width=40, heigh=21, font = ("Courier", 11))
        self.scrollbarText = Scrollbar(self, orient=VERTICAL)
        self.textArea.configure(yscrollcommand=self.scrollbarText.set)
        self.scrollbarText.config(command=self.textArea.yview)
        self.scrollbarText.pack(side=RIGHT, fill=Y)
        self.textArea.place(x=535, y=150)
        
        #List
        self.list = []
        self.checkbox = BooleanVar(self)
        self.checkW2V = Checkbutton(self, text="Word 2 Vec", variable=self.checkbox,command=self.checkbox_clicked,  fg = "#4285f4",  font = ("Serif", 14))
        self.checkW2V.place(x= 750, y =20)
        w.pack()
        
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



    


self().mainloop()


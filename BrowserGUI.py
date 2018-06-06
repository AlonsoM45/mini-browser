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
        w = Canvas(menu, width=500, height=200)
        w.pack()
        w.create_line(0, 90, 500, 90)


        lbl1= Label(menu, text= "Path:", fg ='#4285f4', font = ("Serif", 14))
        lbl1.place(x=25, y= 30)
        

        menu.btnNormalIndex= Button(menu, text="Usar 2 Millones", activebackground="#4285f4", fg = "white", bg = "#db4437", font = ("Serif", 13), width=20, heigh=3, command=normalIndex)
        menu.btnNormalIndex.place(x=150, y=110)
        menu.btnNewIndex= Button(menu, text="Indexar Nuevo", activebackground="#4285f4", fg = "white", bg = "#db4437", font = ("Serif", 13), width=20, heigh=3, command= menu.NewIndex)
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
        self.geometry("950x590")
        w = Canvas(self, width=950, height=590, bg="#f2f2f2")
        
        w.create_rectangle(370, 115, 890, 185, width = 1)
        w.create_rectangle(20, 55, 890, 185, width = 2)
        w.create_rectangle(20, 115, 370, 185, width = 1)

        labelGoogle1 = Label(self, text= "M", fg = "#4285f4",  font = ("Futura", 25))
        labelGoogle1.place(x=360, y= 10)
        labelGoogle2 = Label(self, text= "i", fg = "#db4437",  font = ("Futura", 25))
        labelGoogle2.place(x=390, y= 10)
        labelGoogle3 = Label(self, text= "n", fg = "#f4b400",  font = ("Futura", 25))
        labelGoogle3.place(x=400, y= 10)
        labelGoogle4 = Label(self, text= "i", fg = "#4285f4",  font = ("Futura", 25))
        labelGoogle4.place(x=420, y= 10)
        labelGoogle1 = Label(self, text= "G", fg = "#4285f4",  font = ("Futura", 25))
        labelGoogle1.place(x=452, y= 10)
        labelGoogle2 = Label(self, text= "o", fg = "#db4437",  font = ("Futura", 25))
        labelGoogle2.place(x=480, y= 10)
        labelGoogle3 = Label(self, text= "o", fg = "#f4b400",  font = ("Futura", 25))
        labelGoogle3.place(x=500, y= 10)
        labelGoogle4 = Label(self, text= "g", fg = "#4285f4",  font = ("Futura", 25))
        labelGoogle4.place(x=520, y= 10)
        labelGoogle5 = Label(self, text= "l", fg = "#0f9058",  font = ("Futura", 25))
        labelGoogle5.place(x=540, y= 10)
        labelGoogle6 = Label(self, text= "e", fg = "#db4437",  font = ("Futura", 25))
        labelGoogle6.place(x=550, y= 10)
        lbl1= Label(self, text= "Texto:", fg = "#4285f4",  font = ("Serif", 14))
        lbl1.place(x=60, y= 70)
        lbl2= Label(self, text= "Cantidad de Resultados: ", fg =  "#4285f4", font = ("Serif", 14))
        lbl2.place(x=420, y= 70)
        lbl3= Label(self, text= "Exactitud: ", fg = "#4285f4",  font = ("Serif", 14))
        lbl3.place(x=400, y= 140)
        labelCreditos = Label(self, text= "Rubén González Villanueva  -  Andrés Obando Alfaro  -  Luis Alonso Montero Marin", fg = "#4285f4",  font = ("Futura", 11))
        labelCreditos.place(x=200, y= 570)
        #TextBox

        self.textBoxSearch = Entry(self, width=25, font = ("Serif", 13))
        self.textBoxSearch.place(x=150, y= 70)
        self.textBoxQuantity = Entry(self, width=7, font = ("Serif", 13))
        self.textBoxQuantity.place(x=650, y= 70)
        self.textBoxProb = Entry(self, width=7, font = ("Serif", 13))
        self.textBoxProb.place(x=500, y= 140)
        
        #Button
        self.btnNormalSearch= Button(self, text="Búsqueda Normal",activebackground="#4285f4",width=30, heigh=2, command=self.normalSearch, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.btnNormalSearch.place(x=60, y=125)
        self.btnProbSearch= Button(self, text="Búsqueda Probabilística",activebackground="#4285f4",width=30, heigh=2,command= self.probSearch, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.btnProbSearch.place(x=600, y=125)
        self.btnViewDocument= Button(self, text="Ver",width=7, activebackground="#4285f4",heigh=2,command= self.viewDocument, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.btnViewDocument.place(x=440, y=350)
        
        #ListBox
        self.scrollbarList = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self,width=43, heigh=20, yscrollcommand=self.scrollbarList.set , font = ("Courier", 11))
        self.scrollbarList.config(command=self.listbox.yview)
        self.scrollbarList.pack(side=LEFT, fill=Y)
        self.listbox.place(x=30, y=200)
        
        #TextArea
        self.textArea = Text(self,width=40, heigh=21,  font = ("Courier", 11))
        self.scrollbarText = Scrollbar(self, orient=VERTICAL)
        self.textArea.configure(yscrollcommand=self.scrollbarText.set)
        self.scrollbarText.config(command=self.textArea.yview)
        self.scrollbarText.pack(side=RIGHT, fill=Y)
        self.textArea.place(x=535, y=200)

        
        #List
        self.list = []
        self.checkbox = BooleanVar(self)
        self.checkW2V = Checkbutton(self, text="Word 2 Vec", variable=self.checkbox,command=self.checkbox_clicked,  fg = "#4285f4",  font = ("Serif", 14))
        self.checkW2V.place(x= 750, y =70)
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
        for word in self.textBoxSearch.get().split():            
            textA = self.list[int(index[0])]
            startA = re.search(word, textA).start()
            endA = startA + len(word)
            self.textArea.tag_add("start", "1."+str(startA), "1."+str(endA))
            self.textArea.tag_config("start", background="black", foreground="yellow")



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


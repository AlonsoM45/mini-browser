from tkinter import *
import tkinter
from random import choice
from TFIDF import searchTFIDF, newIndex
import pyodbc




class self(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Mini Google")
        self.geometry("1000x600")

        lbl1= Label(self, text= "Texto:", font="20")
        lbl1.place(x=20, y= 10)
        lbl2= Label(self, text= "Cantidad de Resultados: ", font="20")
        lbl2.place(x=20, y= 50)
        #TextBox
        self.textBoxSearch = Entry(self, width=30)
        self.textBoxSearch.place(x=200, y= 10)
        self.textBoxQuantity = Entry(self, width=30)
        self.textBoxQuantity.place(x=200, y= 50)
        #Button
        self.btnNormalSearch= Button(self, text="Buscar Normal", width=20, heigh=2, command=self.normalSearch)
        self.btnNormalSearch.place(x=20, y=100)
        self.btnProbSearch= Button(self, text="Buscar Probabilistico",width=20, heigh=2,command= self.probSearch)
        self.btnProbSearch.place(x=200, y=100)
        self.btnViewDocument= Button(self, text="Ver Documento",width=20, heigh=2,command= self.viewDocument)
        self.btnViewDocument.place(x=620, y=525)
        #ListBox
        self.scrollbarList = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self, yscrollcommand=self.scrollbarList.set ,width=70, heigh=30)
        self.scrollbarList.config(command=self.listbox.yview)
        self.scrollbarList.pack(side=RIGHT, fill=Y)
        self.listbox.place(x=500, y=10)
        
        #TextArea
        self.scrollbarText = Scrollbar(self, orient=VERTICAL)
        self.textArea = Text(self,width=50, heigh=20,yscrollcommand=self.scrollbarText.set)
        self.scrollbarText.config(command=self.textArea.yview)
        self.scrollbarText.pack(side=LEFT, fill=Y)
        self.textArea.place(x=20, y=200)

        #List
        self.list = []


    def normalSearch(self):
        quest = self.textBoxSearch.get()
        quantity = self.textBoxQuantity.get()
        self.listbox.delete(0, END)
        self.list =[]
        result = searchTFIDF(quest, TF, IDF, len(documents))
        realQuantity = min(int(quantity), len(result))
        #arreglar
        for x in range(int(realQuantity)):
            self.list += [documents[result[x][0]]]
            self.listbox.insert(END, documents[result[x][0]])

    def probSearch(self):
        quest = self.textBoxSearch.get()
        quantity = self.textBoxQuantity.get()
        uniformDocuments = uniform(documents,70)

        self.listbox.delete(0, END)
        self.list =[]
        result = searchTFIDF(quest, uniformDocuments)
        print(result)
        realQuantity = min(int(quantity), len(result))
        #arreglar
        for x in range(int(realQuantity)):
            self.list += [uniformDocuments[result[x][0]]]
            self.listbox.insert(END, [uniformDocuments[result[x][0]]])

    def viewDocument(self):
        index = self.listbox.curselection()
        self.textArea.delete(1.0, END)
        self.textArea.insert(END, self.list[int(index[0])])

def uniform(documents, porcentage):
    available = []
    #arreglar
    for i in range(len(documents)):
        available += [i]

    newDocuments = []
    num = (len(documents)*porcentage)//100
    #arreglar
    for i in range (num):
        randomNum = choice(available)-1
        newDocuments += [documents[available.pop(randomNum)]]
    return newDocuments



documents = []



cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};"
                      "Server= DESKTOP-5TPABM1;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Google.dbo.Reseñas')
doc = map(list,cursor)
documents = list(doc)



TF, IDF = newIndex(documents)


self().mainloop()















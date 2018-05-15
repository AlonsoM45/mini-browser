from tkinter import *
import tkinter
from random import choice
from TFIDF import searchIFIDF


def cargarArchivo(archivo):
    fo = open(archivo, "r") 
    resultado = fo.read()
    fo.close()
    return eval(resultado)

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
        self.btnViewDocument.place(x=60, y=550)
        #ListBox
        self.scrollbarList = Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self, yscrollcommand=self.scrollbarList.set ,width=60, heigh=20)
        self.scrollbarList.config(command=self.listbox.yview)
        self.scrollbarList.pack(side=LEFT, fill=Y)
        self.listbox.place(x=20, y=200)
        
        #TextArea
        self.scrollbarText = Scrollbar(self, orient=VERTICAL)
        self.textArea = Text(self,width=50, heigh=30,yscrollcommand=self.scrollbarText.set)
        self.scrollbarText.config(command=self.textArea.yview)
        self.scrollbarText.pack(side=RIGHT, fill=Y)
        self.textArea.place(x=500, y=10)

        #List
        self.list = []


    def normalSearch(self):
        quest = self.textBoxSearch.get()
        quantity = self.textBoxQuantity.get()
        self.listbox.delete(0, END)
        self.list =[]
        result = searchIFIDF(documents, quest)
        realQuantity = min(int(quantity), len(result))
        #arreglar
        for x in range(int(realQuantity)):
            self.list += [documents[result[x][0]]]
            self.listbox.insert(END, [documents[result[x][0]]])

    def probSearch(self):
        quest = self.textBoxSearch.get()
        quantity = self.textBoxQuantity.get()
        uniformDocuments = uniform(documents,70)

        self.listbox.delete(0, END)
        self.list =[]
        result = searchIFIDF(uniformDocuments, quest)
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


documents += ["""Python is a 2000 made-for-TV horror movie directed by Richard
Clabaugh. The film features several cult favorite actors, including William
Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy,
Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the
A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean
Whalen. The film concerns a genetically engineered snake, a python, that
escapes and unleashes itself on a small town. It includes the classic final
girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles,
California and Malibu, California. Python was followed by two sequels: Python
II (2002) and Boa vs. Python (2004), both also made-for-TV films."""]

documents += ["""Python, from the Greek word (πύθων/πύθωνας), is a genus of
nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
recognised.[2] A member of this genus, P. reticulatus, is among the longest
snakes known."""]

documents += ["""The Colt Python is a .357 Magnum caliber revolver formerly
manufactured by Colt's Manufacturing Company of Hartford, Connecticut.
It is sometimes referred to as a "Combat Magnum".[1] It was first introduced
in 1955, the same year as Smith & Wesson's M29 .44 Magnum. The now discontinued
Colt Python targeted the premium revolver market segment. Some firearm
collectors and writers such as Jeff Cooper, Ian V. Hogg, Chuck Hawks, Leroy
Thompson, Renee Smeets and Martin Dougherty have described the Python as the
finest production revolver ever made."""]








self().mainloop()















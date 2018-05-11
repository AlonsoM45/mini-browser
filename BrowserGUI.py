from tkinter import *
import tkinter


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
        self.textArea.delete(1.0, END)
        self.textArea.insert(END,"Busqueda Normal")
        self.listbox.delete(0, END)
        for x in range(0, int(quantity)):
            self.list = self.list + [x]
            self.listbox.insert(END, self.list[x])

    def probSearch(self):
        quest = self.textBoxSearch.get()
        quantity = self.textBoxQuantity.get()
        self.textArea.delete(1.0, END)
        self.textArea.insert(END,"Busqueda Probabilistica")
        self.listbox.delete(0, END)
        for x in range(0, int(quantity)):
            self.listbox.insert(END, self.list[x])

    def viewDocument(self):
        index = self.listbox.curselection()
        self.textArea.delete(1.0, END)
        self.textArea.insert(END, self.list[int(index[0])])

self().mainloop()













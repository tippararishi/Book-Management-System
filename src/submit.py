'''
This Module is for Submitting Books
'''
from tkinter import *
from tkinter import messagebox
from src import database
class submitBooks:
    def __init__(self,mainFrame):
        self.submitFrame=mainFrame
        labelContainer=Frame(self.submitFrame,bg='#98C1D9')
        entryFrame=Frame(self.submitFrame,bg='#98C1D9')
        labelContainer.grid(row=1,column=1)
        entryFrame.grid(row=1,column=2,padx=20)

        #LABELS
        userName=Label(labelContainer,bg='#98C1D9',text='User Name',font=('Verdana 14'))
        isinId=Label(labelContainer,bg='#98C1D9',text='ISIN',font=('Verdana 14'))
        bookName=Label(labelContainer,bg='#98C1D9',text='Book Name',font=('Verdana 14'))
        price=Label(labelContainer,bg='#98C1D9',text='Price',font=('Verdana 14'))
        qty=Label(labelContainer,bg='#98C1D9',text='Quantity',font=('Verdana 14'))

        userName.grid(row=1,column=1,pady=10)
        bookName.grid(row=2,column=1,pady=10)
        price.grid(row=3,column=1,pady=10)
        qty.grid(row=4,column=1,pady=10)
        isinId.grid(row=5,column=1,pady=10)

        #ENTRY
        self.userNameEntry=Entry(entryFrame,font=('Verdana 14'))
        self.bookNameEntry=Entry(entryFrame,font=('Verdana 14'))
        self.priceEntry=Entry(entryFrame,font=('Verdana 14'))
        self.qtyEntry=Entry(entryFrame,font=('Verdana 14'))
        self.isinEntry=Entry(entryFrame,font=('Verdana 14'))

        self.userNameEntry.grid(row=1,column=1,pady=10)
        self.bookNameEntry.grid(row=2,column=1,pady=10)
        self.priceEntry.grid(row=3,column=1,pady=10)
        self.qtyEntry.grid(row=4,column=1,pady=10)
        self.isinEntry.grid(row=5,column=1,pady=10)

        #SUBMIT 
        submitBtn=Button(self.submitFrame,text='SUBMIT',bg='#293241',fg='#E0FBFC',command=self.addBooks,font=('Verdana 16'))
        submitBtn.grid(row=2,column=2)

    def openWin(self,mainFrame):
        submitBooks(mainFrame)

    def addBooks(self):
        userName=self.userNameEntry.get()
        b_name=self.bookNameEntry.get()
        price=int(self.priceEntry.get())
        qty=int(self.qtyEntry.get())
        isin=self.isinEntry.get()

        dbase=database.booksTable(isin,b_name,price,qty)
        dbase.insertIntoTable()
        messagebox.showinfo('Success','Books Added!')
'''
This Module Contains The Home Window 
'''
from tkinter import *
from tkinter import messagebox
from src import database
class homeWind:
    def __init__(self,mainFrame,user):
        self.homeFrame=mainFrame
        self.topFrame=Frame(self.homeFrame,bg='#293241')
        self.topFrame.grid(row=1,column=1)
        self.contentFrame=Frame(self.homeFrame,bg='#98C1D9')
        self.contentFrame.grid(row=2,column=1)

        #Labels
        welcomeMsg=Label(self.topFrame,bg ='#293241',fg='white',text="Welcome, {} !".format(user),font=('Verdana 20'))
        userName=Label(self.contentFrame,text="User Name",font=('Verdana 14'),bg='#98C1D9',fg='white')
        bookName=Label(self.contentFrame,text="Book Name",font=('Verdana 14'),bg='#98C1D9',fg='white')
        isin=Label(self.contentFrame,text="ISIN",font=('Verdana 14'),bg='#98C1D9',fg='white')

        welcomeMsg.grid(row=1,column=3,pady=20)
        userName.grid(row=1,column=1,padx=10)
        bookName.grid(row=2,column=1,padx=10)
        isin.grid(row=3,column=1,padx=10)

        #Entry
        self.userNameEntry=Entry(self.contentFrame,font=('Verdana 14'))
        self.bookNameEntry=Entry(self.contentFrame,font=('Verdana 14'))
        self.isinEntry=Entry(self.contentFrame,font=('Verdana 14'))
        self.userNameEntry.insert(0,user)
        self.userNameEntry.configure(state='disabled')

        self.userNameEntry.grid(row=1,column=2)
        self.bookNameEntry.grid(row=2,column=2)
        self.isinEntry.grid(row=3,column=2)

        #Submit Button
        self.submitbtn=Button(mainFrame,text="ORDER",command=self.orderBook,font=('Verdana 14'),bg='#293241',fg='#E0FBFC')
        self.submitbtn.grid(row=3,column=1) 

    def isAvailable(self,isin,name):
        data=database.database()
        data.executeDDLCommand("SELECT BOOK_NAME FROM BOOKS WHERE ISIN='{}' AND BOOK_NAME='{}' AND QUANTITY >=1".format(isin,name))
        if data.rowcount()==1:
            return True
        else:
            return False

    def orderBook(self):
        b_name=self.bookNameEntry.get()
        isin=self.isinEntry.get()
        data=database.database()

        if self.isAvailable(isin,b_name):
            self.submitbtn.configure(text="ORDER SUCCESSFULL")
            data.executeUpdate("UPDATE BOOKS SET QUANTITY=QUANTITY-1 WHERE ISIN='{}'".format(isin))
        else:
            messagebox.showerror('Error','Book Not Available')
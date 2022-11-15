'''
This Module Contains Login Page
'''
from tkinter import *
from tkinter import messagebox
from src import database
from src import home
from src import register
class login:
    def __init__(self,mainFrame):
        #FRAMES
        self.loginFrame=mainFrame
        labelContainer=Frame(self.loginFrame,bg='#98C1D9')
        entryContainer=Frame(self.loginFrame,bg='#98C1D9')
        labelContainer.grid(row=1,column=1,padx=10)
        entryContainer.grid(row=1,column=2,padx=10)

        #LABELS
        self.userName=Label(labelContainer,text='User Name: ',font=('Verdana 14'),bg='#98C1D9',fg='white')
        self.phoneNo=Label(labelContainer,text='Phone Number: ',font=('Verdana 14'),bg='#98C1D9',fg='white')
        self.password=Label(labelContainer,text='Password: ',font=('Verdana 14'),bg='#98C1D9',fg='white')
        self.userName.grid(row=1,column=1,pady=10)
        self.phoneNo.grid(row=2,column=1,pady=10)
        self.password.grid(row=3,column=1,pady=10)

        #ENTRY
        self.userNameEntry=Entry(entryContainer,font=('Verdana 14'))
        self.passwordEntry=Entry(entryContainer,show='*',font=('Verdana 14'))
        self.phoneNoEntry=Entry(entryContainer,font=('Verdana 14'))
        self.userNameEntry.grid(row=1,column=1,pady=10)
        self.phoneNoEntry.grid(row=2,column=1,pady=10)
        self.passwordEntry.grid(row=3,column=1,pady=10)

        #BUTTON
        self.submitBtn=Button(mainFrame,text='LOGIN',bg='#293241',fg='#E0FBFC',command=self.validateCredentials,font=('Verdana 14'))
        self.backBtn=Button(mainFrame,text='REGISTER',bg='#293241',fg='#E0FBFC',command=self.openRegister,font=('Verdana 14'))
        self.backBtn.grid(row=2,column=3)
        self.submitBtn.grid(row=2,column=2)


    def openWin(self,mainFrame):
        login(mainFrame)

    def clearFrame(self):
        for widget in self.loginFrame.winfo_children():
            widget.destroy()

    def openRegister(self):
        self.clearFrame()
        registerWindow=register.registerWin(self.loginFrame)
        registerWindow.openWin(self.loginFrame)

    def validateCredentials(self):
        username=self.userNameEntry.get()
        passwd=self.passwordEntry.get()
        phNo=self.phoneNoEntry.get()

        command="SELECT * FROM USERS WHERE USER_NAME='{}' AND PASSWORD='{}' AND PHONE_NUMBER='{}'".format(username,passwd,phNo)
        db=database.database()
        db.executeDDLCommand(command)
        count=db.rowcount()
        if count==1:
            messagebox.showinfo('Login Success','Login Successfull')
            self.clearFrame()
            homeWin=home.homeWind(self.loginFrame,username)
        else:
            messagebox.showerror('Error','Login Failed! Incorrect User Name or Password or Phone Number. Try Again!')

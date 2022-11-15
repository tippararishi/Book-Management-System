'''
This Module Contains Users
'''
from src import database
from tkinter import messagebox
class user:
    def __init__(self,name,addr,gender,phNo,emailId,passwd):
        self.name=name
        self.address=addr
        self.gender=gender
        self.phNo=phNo
        self.emailId=emailId
        self.passwd=passwd

    def userExist(self):
        command="SELECT USER_NAME FROM USERS WHERE PHONE_NUMBER={}".format(self.phNo)
        db=database.database()
        db.executeDDLCommand(command)
        count=db.rowcount()
        if count>=1:
            return True
        else:
            return False
    def addUserToDatabase(self):
        db=database.database()
        if self.userExist():
            messagebox.showerror('Error','User Already Exist! Try Again')
        else:
            new_user=database.usersTable(self.phNo,self.name,self.gender,self.address,self.emailId,self.passwd)
            new_user.insertIntoTable()

    
    



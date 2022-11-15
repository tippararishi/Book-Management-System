'''
This Module Contains The Database
'''
import mysql.connector as sqltor

class database:
    def __init__(self,passwd='login'):
        self._password=passwd
        self.db=sqltor.connect(host='localhost',user='root',password=self._password)
        self.cursor=self.db.cursor()
        #Creating DATABASE
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS book_management_system')
        self.cursor.execute('USE book_management_system')

        #Creating TABLES
        self.cursor.execute('CREATE TABLE IF NOT EXISTS BOOKS(ISIN VARCHAR(12) PRIMARY KEY,BOOK_NAME VARCHAR(100) NOT NULL,BOOK_PRICE INT(4) NOT NULL,QUANTITY INT(3))')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS USERS(PHONE_NUMBER VARCHAR(11) PRIMARY KEY,USER_NAME VARCHAR(100) NOT NULL,GENDER VARCHAR(2) NOT NULL,ADDRESS VARCHAR(100),EMAIL_ID VARCHAR(100) NOT NULL, PASSWORD VARCHAR(9) NOT NULL)')

    def checkCon(self):
        if self.db.is_connected():
            print("Successfull")
        else:
            print("Failed")
    #Execute  DML Commands
    def executeDMLCommand(self,command):
        self.cursor.execute(command)
        self.db.commit()

    #Update DATA
    def executeUpdate(self,command):
        self.cursor.execute(command)
        self.db.commit()

    #Execute DDL Commands
    def executeDDLCommand(self,command):
        self.cursor.execute(command)

    #Row Count
    def rowcount(self):
        data=self.cursor.fetchall()
        count = 0
        for x in data:
            count+=1
        return count

class usersTable:
    def __init__(self,phNo,name,gender,address,email,passwd):
        self.phoneNo=phNo
        self.userName=name
        self.gender=gender
        self.address=address
        self.emailID=email
        self._password=passwd
        self.table="USERS"

    def insertIntoTable(self):
        command="INSERT INTO USERS(PHONE_NUMBER,USER_NAME,GENDER,ADDRESS,EMAIL_ID,PASSWORD) VALUES('{}','{}','{}','{}','{}','{}')".format(self.phoneNo,self.userName,self.gender,self.address,self.emailID,self._password)
        db=database()
        db.executeDMLCommand(command)

class booksTable:
    def __init__(self,isin,b_name,b_price,qtny):
        self.isin=isin
        self.b_name=b_name
        self.b_price=b_price
        self.quantity=qtny
        self.table="BOOKS"

    # Insert Into Table
    def insertIntoTable(self):
        command="INSERT INTO BOOKS(ISIN,BOOK_NAME,BOOK_PRICE,QUANTITY) VALUES('{}','{}',{},{})".format(self.isin,self.b_name,self.b_price,self.quantity)
        db=database()
        db.executeDMLCommand(command)
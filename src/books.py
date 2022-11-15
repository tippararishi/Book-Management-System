'''
This Module Contains Books
'''
import database
class books:
    def __init__(self,b_name,price,author,isin,user,qtny):
        self.isin=isin
        self.bookname=b_name
        self.price=price
        self.user=user
        self.quantity=qtny

    def bookExist(self):
        command="SELECT ISIN FROM BOOKS WHERE BOOK_NAME={}".format(self.bookname)
        database.database.executeDDLCommand(command)
        count=database.database.rowcount()
        if count>=1:
            return True
        else:
            return False

    def addBooksToDatabase(self):
        new_book=database.booksTable(self.isin,self.bookname,self.price,self.quantity)
        new_book.insertIntoTable()
    def addBooks(self,b_name,price,isin,user,qtny):
        books(b_name,price,isin,user,qtny)
        if self.bookExist()==False:
            self.addBooksToDatabase()
        else:
            command="UPDATE BOOKS SET QUANTITY=QUANTITY+{} WHERE BOOK_NAME={}".format(self.quantity,self.bookname)
            database.database.executeUpdate(command)
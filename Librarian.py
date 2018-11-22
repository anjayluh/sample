__author__ = 'Anjayluh'
class Librarian(object):


    def __init__(self):
        self.idNo = raw_input('ID number')
        self.lname = raw_input('Lbrarian Name')

    def printinfo(self):
        print "\nLIBRARIAN INFORMATION\n"
        print ('%-20s %-20s ' % ("Name", "Id Number"))
        print ('%-20s %-20s ' % (self.lname, self.idno))

    def __str__(self):
        return (self.lname)

#lib1 = Librarian()

class Book(Librarian):

    def __init__(self):
        Librarian.__init__(self)

        self.title = raw_input('Title')
        self.author = raw_input('Author')
        self.cost = raw_input('Book cost')

    def printinfo(self):
        print ('%-20s %-200s ' % (self.title, self.cost))
#bk1 = Book()

class Borrower(Book):


    def __init__(self, desk=[]):
        Book.__init__(self)
        self.idno = raw_input("idno:")
        self.name = raw_input("Name:")
        self.course = raw_input("Course: ")
        self.desk = desk


    def printinfo(self):
        print "\n*******************BORROWER INFORMATION**********************"
        print ('%-20s %-20s %-20s' % ("Name", "Id Number", "Course"))
        print ('%-20s %-20s %-20s' % (self.name, self.idno, self.course))

#borrower1 = Borrower()

class Loan(Borrower):

    def __init__(self):
            Borrower.__init__(self)
            self.date_borrowed = raw_input('Date the book was borrowed')
            self.date_returned = raw_input('Date it was returned\n If it hasn\'t been retuned, put today\'s date')
            self.date_agreed = raw_input('The supposed to be return date')
            self.fine = 50000


    def borrowing(self, inventory , borrower, allbooks=[]):

        books = []
        booksno = []
        count = 0
        bookno = raw_input(" How many books do you want to borrow\n Choose a number below 8 and above 0: ")
        if bookno > 8 or bookno < 0:
            print "Please enter valid number"
        else:
            allbooks.append(bookno)


            num = 0
            for book in inventory.bookList:
                print "%d %s" %(num,book.bookname)
                num += 1

            bookname = raw_input("5. Enter the book code (separated by commas): ")

            bookchoices = []

            for bookcode in bookname.split(","):
                code = int(bookcode)
                bookchoices.append(code)
                borrower.desk.append(inventory.bookList[code] )

            for choice in bookchoices:
                inventory.bookList.remove(inventory.bookList[choice])
    def __str__(self):
        return (Borrower)
loan1 = Loan()
class Return(object):
    def __init__(self,bookList = []):
        self.bookList = bookList
    def main():
        print "\n*******************WELCOME TO MUKLIB**********************"

    return1 = Return()
    return1.bookList.append(Books("OOP principles", 60000))
    return1.bookList.append(Books("Agile methods", 30000))
    return1.bookList.append(Books("Think like abillionaire", 30000))
    return1.bookList.append(Books("Data Stactures and Algorithims", 20000))
    return1.bookList.append(Books("Java in 21 days", 10000))
    return1.bookList.append(Books("Clean Code", 5000))

    borrower1 = Borrower()
    # print borrower1.name

    # inventory ,allbooks=[]
    loan1 = Loan()
    loan1.borrowing(return1,borrower1)
    print "Name of Student: {}".format(borrower1.name)
    print "Books Borrowed"
    for book in borrower1.desk:
        print ("{}".format(book.bookname))
    print "Total number of books: {}".format(len(borrower1.desk))



main()

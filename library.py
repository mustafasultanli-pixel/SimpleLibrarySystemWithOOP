from students import *

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.students = []

    def addBook(self, book):
        self.books.append(book)
    def addStudent(self, student):
        self.students.append(student)
    def showBooks(self):
        if not self.books:
            print("There are no books.")
            return
        for book in self.books:
            book.showInfo()
            print("----------------")
    def showStudents(self):
        if not self.students:
            print("There are no books.")

        for student in self.students:
            student.showInfo()
            print("----------------")


    # def addBook(self, book):
    # def addStudent(self, student):
    # def showBooks(self):
    # def showStudents(self):
    # def searchBook(self, bookID):
    # def searchStudents(self, studentID):
    # def borrowBook(self, studentID, bookID):
    # def returnBook(self, studentID, bookID):
    
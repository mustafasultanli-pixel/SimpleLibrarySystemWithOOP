class Book:
    def __init__(self, bookID, title, author, pageCount):
        self.bookID = bookID
        self.title = title
        self.author = author
        self.pageCount = pageCount

    def showInfo(self):
        print(f"""

        ID: {self.bookID}
        Title: {self.title}
        Author: {self.author}
        pageCount: {self.pageCount}

        """)

book1 = Book(1, "Clean Code", "Rober Martin", 464)
book2 = Book(2, "Python Crash Course", "Eric Matthes", 560)
book3 = Book(3, "Atomic Habits", "James Clear", 320)


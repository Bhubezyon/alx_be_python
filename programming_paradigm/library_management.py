class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        self._is_checked_out = False

    def return_book(self):
        self._is_checked_out = True

    def is_available(self):
        return self._is_checked_out
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title and book._is_available():
                book.check_out()
                return book
            print(f"Book '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book._is_available():
                book.return_book()
                return book
        print(f"Book '{title}' was not checked out.")

    def list_available_books (self):
        for book in self.books:
            if book.is_available():
                print(book.is_available()) 
 
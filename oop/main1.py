from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a library instance
    library = Library()
    
    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stepheson", 500)
    paper_novel = PrintBook("The  Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to library"

    library.add_book(classic_book)

    library.add_book(classic_book)

    library.add_book(paper_novel)

    # List all books in the library
    library.list_books()

if __name__ == "__main__":
    main
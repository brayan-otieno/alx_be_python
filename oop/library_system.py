# Base class for Book
class Book:
    def __init__(self, title, author):
        """Constructor: Initializes the Book instance with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation for the Book."""
        return f"Book: {self.title} by {self.author}"

# Derived class for EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Constructor: Initializes EBook with title, author, and file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size  # EBook-specific attribute
    
    def __str__(self):
        """String representation for EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class for PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Constructor: Initializes PrintBook with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # PrintBook-specific attribute
    
    def __str__(self):
        """String representation for PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class that uses composition to manage a collection of books
class Library:
    def __init__(self):
        """Constructor: Initializes an empty list to store books."""
        self.books = []
    
    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook to the library collection."""
        self.books.append(book)
    
    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)

# main.py
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()

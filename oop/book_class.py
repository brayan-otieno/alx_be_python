class Book:
<<<<<<< HEAD
    # Constructor (__init__): Initializes the Book instance with title, author, and year
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor (__del__): Prints a message when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

    # String Representation (__str__): Returns a user-friendly string
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official Representation (__repr__): Returns a string that can recreate the object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Test the Book class
=======
    def __init__(self, title, author, year):
        """Constructor: Initializes a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """Destructor: Prints 'Deleting (title of the book)' upon object deletion."""
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """String Representation: Returns a human-readable string for the book."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official Representation: Returns a string that would recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# main.py
from book_class import Book

>>>>>>> 8a20141e46704b7df1e8dd178902557ef0d9d434
def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()

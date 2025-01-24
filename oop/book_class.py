class Book:
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

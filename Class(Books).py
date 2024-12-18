class Book:
   def __init__(self, title, author):
       """Initialize the book with title, author, and availability."""
       self.title = title
       self.author = author
       self.is_available = True  # Book is available by default
   def borrow(self):
       """Mark the book as borrowed if available."""
       if self.is_available:
           self.is_available = False
           print(f"'{self.title}' has been borrowed.")
           return True
       print(f"'{self.title}' is unavailable.")
       return False
   def return_book(self):
       """Mark the book as available if it was borrowed."""
       if not self.is_available:
           self.is_available = True
           print(f"'{self.title}' has been returned.")
           return True
       print(f"'{self.title}' was not borrowed.")
       return False

class Member:
   def __init__(self, name):
       """Initialize the member with their name and an empty list of borrowed books."""
       self.name = name
       self.borrowed_books = []
   def borrow_book(self, book):
       """Borrow a book if it's available."""
       if book.borrow():
           self.borrowed_books.append(book)
   def return_book(self, book):
       """Return a book if it is in the borrowed books list."""
       if book in self.borrowed_books and book.return_book():
           self.borrowed_books.remove(book)

class Library:
   def __init__(self, name):
       """Initialize the library with a name and empty collections for books and members."""
       self.name = name
       self.books = []
       self.members = []
   def add_book(self, book):
       """Add a book to the library's collection."""
       self.books.append(book)
       print(f"'{book.title}' added to the library.")
   def register_member(self, member):
       """Register a new member in the library system."""
       self.members.append(member)
       print(f"Member '{member.name}' registered.")
   def list_books(self):
       """List all available books in the library."""
       available_books = [book for book in self.books if book.is_available]
       if available_books:
           print("Available books:")
           for book in available_books:
               print(f"- {book.title} by {book.author}")
       else:
           print("No books are currently available.")

# Test the system
library = Library("Grand City Library")
# Add books to the library
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("Pride and Prejudice", "Jane Austen"))
library.add_book(Book("Moby Dick", "Herman Melville"))
# Register members
member1 = Member("Emma")
member2 = Member("Liam")
library.register_member(member1)
library.register_member(member2)
# List available books in the library
library.list_books()
# Borrow and return books for a member
book1 = library.books[0]
book2 = library.books[1]
# Member1 borrows a book
member1.borrow_book(book1)
library.list_books()  # List books after borrowing
# Member1 returns the borrowed book
member1.return_book(book1)
library.list_books()  # List books after returning
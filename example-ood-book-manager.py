# Defining a Book class
class Book:
    def __init__(self, title, author, genre, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.genre}, {self.isbn})"

# Creating a collection of books using a list
library = [
    Book("1984", "George Orwell", "Dystopian", "9780451524935"),
    Book("To Kill a Mockingbird", "Harper Lee", "Fiction", "9780061120084"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", "9780743273565"),
    Book("Brave New World", "Aldous Huxley", "Dystopian", "9780060850524")
]

# Searching for books by genre (Filtering)
dystopian_books = [book for book in library if book.genre == "Dystopian"]
print("Dystopian Books:", dystopian_books)

# Sorting books alphabetically by title
library.sort(key=lambda book: book.title)
print("Sorted Library:", library)

# Using a dictionary to organize books by ISBN for quick lookup
book_index = {book.isbn: book for book in library}
print("Lookup by ISBN:", book_index["9780061120084"])
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False
    def get_is_checked_out(self):
        return self.__is_checked_out
    def set_is_checked_out(self, is_checked_out):
        self.__is_checked_out = is_checked_out
    def return_book(self):
        self.__is_checked_out = False
    def check_out_book(self):
        self.__is_checked_out = True
    
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book:Book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out_book()
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
    def list_available_books(self):
        for book in self._books:
            if not book.get_is_checked_out():
                print(f"{book.title} by {book.author}")
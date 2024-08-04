class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f'Title: {self.title} by author: {self.author}'


class Library:
    def __init__(self, books: list[Book]):
        self.books: list[Book] = books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        to_remove = [b for b in self.books if b.title == title]

        if not to_remove:
            raise ValueError('The book is not in the list')

        if len(to_remove) > 1:
            raise ValueError('Too many book were found')

        self.books.remove(to_remove[0])

    def get_books_by_author(self, author: str):
        return [b for b in self.books if b.author == author]

    def get_book_by_title(self, title: str):
        books = [b for b in self.books if b.title == title]

        if not books:
            raise ValueError('No such title')

        return books


if __name__ == '__main__':
    book = Book('the book', 'i')
    book2 = Book('the book2', 'i')
    book3 = Book('book', 'asd')

    library = Library([book, book2, book3])

    print(library.get_book_by_title('the book'))
    print(library.get_books_by_author('i'))

    book4 = Book('the book4', 'x')
    library.add_book(book4)

    print(library.get_book_by_title('the book4'))

    print(library.get_books_by_author('fff'))
    print(library.get_book_by_title('fff'))

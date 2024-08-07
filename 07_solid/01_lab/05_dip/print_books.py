















class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class PaperFormatter:
    def format(self, book):
        return book.content[:3]


class Printer:
    def get_book(self, book: Book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book


base_formatter = Formatter()
book = Book('aaa aaa')
paper_formatter = PaperFormatter()
p = Printer()
print(p.get_book(book, base_formatter))
print(p.get_book(book, paper_formatter))

Create:
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book

output: <Book: 1984>

Update:
book.title = "Nineteen Eighty-Four"
book.save()
book

output: <Book: Nineteen Eighty-Four>

Retrieve:

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

output: ('1984', 'George Orwell', 1949)

Delete:
book.delete()

output: (1, {'bookshelf.Book': 1})
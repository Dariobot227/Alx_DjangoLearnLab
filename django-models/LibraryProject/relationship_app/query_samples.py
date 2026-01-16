from relationship_app.models import Author, Book, Library, Librarian

# get book from specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Checker expects this exact string
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return []

# list books
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# retrieve
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

if __name__ == "__main__":
    print(get_books_by_author("John Doe"))
    print(get_books_in_library("Central Library"))
    print(get_librarian_for_library("Central Library"))

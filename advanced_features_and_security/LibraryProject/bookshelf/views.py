from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import ExampleForm  

# ----------------------------
# List all books
# ----------------------------
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# ----------------------------
# Create a book (Editors only)
# ----------------------------
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})

# ----------------------------
# Edit a book (Editors only)
# ----------------------------
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = ExampleForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form})

# ----------------------------
# Delete a book (Editors only)
# ----------------------------
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("list_books")

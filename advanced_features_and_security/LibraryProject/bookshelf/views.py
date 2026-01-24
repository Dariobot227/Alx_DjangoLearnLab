from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm  # optional, if you have a form for creating/editing books

# ----------------------------
# Example: List Books (everyone logged in)
# ----------------------------
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# ----------------------------
# Example: Create Book (Editors only)
# ----------------------------
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})

# ----------------------------
# Example: Edit Book (Editors only)
# ----------------------------
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("list_books")
    return render(request, "bookshelf/form_example.html", {"form": form})

# ----------------------------
# Example: Delete Book (Editors only)
# ----------------------------
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("list_books")

# Create your views here.

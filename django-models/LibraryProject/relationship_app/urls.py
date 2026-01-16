from django.urls import path
from .views import list_books, LibraryDetailView
from .views import (
    list_books,
    LibraryDetailView,
    UserLoginView,
    UserLogoutView,
    register,
    admin_view,
    librarian_view, 
    member_view,
    add_book,
    edit_book,
    delete_book,
)
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # Authentication URLs
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
     path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),

    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]

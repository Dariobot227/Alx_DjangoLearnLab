from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Comprehensive test suite for Book API.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='tester',
            password='pass1234'
        )

        self.author = Author.objects.create(name='George Orwell')

        self.book1 = Book.objects.create(
            title='1984',
            publication_year=1949,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title='Animal Farm',
            publication_year=1945,
            author=self.author
        )

        self.list_url = reverse('book-list')

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.data['title'], '1984')

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        self.client.login(username='tester', password='pass1234')
        url = reverse('book-create')
        data = {
            'title': 'Homage to Catalonia',
            'publication_year': 1938,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        self.client.login(username='tester', password='pass1234')
        url = reverse('book-update', args=[self.book1.id])
        data = {
            'title': 'Nineteen Eighty-Four',
            'publication_year': 1949,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Nineteen Eighty-Four')

    def test_delete_book(self):
        self.client.login(username='tester', password='pass1234')
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        response = self.client.get(self.list_url, {'publication_year': 1949})
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Animal'})
        self.assertEqual(response.data[0]['title'], 'Animal Farm')

    def test_order_books(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.data[0]['title'], '1984')

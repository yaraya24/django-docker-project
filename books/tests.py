from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book, Review

class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )

        self.user = get_user_model().objects.create_superuser(
            username = 'reviewer',
            email='reviewer@admin.com',
            password='testpassword123'
        )

        

        self.review = Review.objects.create(
            book = self.book,
            author = self.user,
            review = "An excellent book."
        )
        self.client.login(username='reviewer', password='testpassword123')
    
    def test_book_listing(self):
        self.assertEqual(self.book.title, 'Harry Potter')
        self.assertEqual(self.book.author, 'JK Rowling')
        self.assertEqual(self.book.price, '25.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_review(self):
        self.assertEqual(self.review.book, self.book)
        self.assertEqual(self.review.author.username, 'reviewer')
        self.assertEqual(self.review.review, "An excellent book.")

    def test_detail_book_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, f"An excellent book. by {self.user.username}")

    def test_search_feature(self):
        response = self.client.get(reverse('search_results'), data={'q':'Harry'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/search_results.html')
        self.assertContains(response, 'Search')
        self.assertContains(response, 'Rowling')
        self.assertNotContains(response, 'Not found')


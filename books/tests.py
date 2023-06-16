from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Book

class BooksTests(TestCase):
    def setUp(self):
        purchaser = get_user_model().objects.create(username="tester", password = "tester")
        Book.objects.create(name="rake", description="horror story",purchaser=purchaser)


    def test_list_page_status_code(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_list_page_template(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('book_list')
        response = self.client.get(url)
        books = response.context['object_list']
        self.assertEqual(len(books),1)
        self.assertEqual(books[0].name, "rake")
        self.assertEqual(books[0].description, "horror story")
        self.assertEqual(books[0].purchaser.username,"tester")

    def test_detail_page_status_code(self):
        url = reverse('book_detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('book_detail', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'book_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('book_detail', args=(1,))
        response = self.client.get(url)
        book = response.context['book']
        self.assertEqual(book.name, "rake")
        self.assertEqual(book.description, "horror story")
        self.assertEqual(book.purchaser.username,"tester")
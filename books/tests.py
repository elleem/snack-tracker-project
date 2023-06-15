from django.test import SimpleTestCase
from django.urls import reverse
from .models import Book

class SnacksTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_book_list_page_template(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'book_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_status_code(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')
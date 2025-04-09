from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):

    def setUp(self):
        Book.objects.create(
            name="The Alchemist",  
            isbn=9780061122415,
            author="Paulo Coelho",
            category="Biographie"
        )

    def test_book_created_successfully(self):
        """Check if the book is created and data is correct"""
        book = Book.objects.get(isbn=9780061122415)
        self.assertEqual(book.name, "The Alchemist")
        self.assertEqual(book.author, "Paulo Coelho")
        self.assertEqual(book.category, "Biographie")
        self.assertEqual(str(book), "The Alchemist[9780061122415]")  # __str__ test

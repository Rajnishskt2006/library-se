import unittest
from src.library import Library


class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        self.library.add_book("B001", "Python Basics", "Guido")
        self.assertIn("B001", self.library.books)

    def test_add_duplicate_book_raises_error(self):
        self.library.add_book("B001", "Python Basics", "Guido")
        with self.assertRaises(ValueError):
            self.library.add_book("B001", "Advanced Python", "Someone")


if __name__ == "__main__":
    unittest.main()
    def test_borrow_book_success(self):
        self.library.add_book("B002", "DSA", "CLRS")
        self.library.borrow_book("B002")
        self.assertEqual(self.library.books["B002"]["status"], "Borrowed")

    def test_borrow_already_borrowed_book_raises_error(self):
        self.library.add_book("B003", "OS", "Tanenbaum")
        self.library.borrow_book("B003")
        with self.assertRaises(ValueError):
            self.library.borrow_book("B003")

    def test_return_book(self):
        self.library.add_book("B004", "CN", "Kurose")
        self.library.borrow_book("B004")
        self.library.return_book("B004")
        self.assertEqual(self.library.books["B004"]["status"], "Available")

    def test_generate_report_contains_header(self):
        report = self.library.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report[0])

    def test_generate_report_contains_book_entry(self):
        self.library.add_book("B005", "AI", "Russell")
        report = self.library.generate_report()
        self.assertTrue(any("B005" in line for line in report))


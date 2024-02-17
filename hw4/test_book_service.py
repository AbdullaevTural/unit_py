import unittest
from unittest.mock import Mock
from book_service import BookService

mock_data = {
    'ID': '15',
    'name': 'The Goldfinch'
}

mock_fetch_books = Mock([mock_data])

mock_fetch_books.configure_mock(return_value=mock_data)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.service = BookService(mock_fetch_books)

    def test_fetching_by_id(self):
        self.assertDictEqual(self.service.fetch_by_id(15), mock_data)

    def test_fetching_all(self):
        self.assertDictEqual(self.service.fetch_all_books(), mock_data)


if __name__ == '__main__':
    unittest.main()

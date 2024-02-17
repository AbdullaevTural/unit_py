class BookService:

    def __init__(self, fetch_books):
        self.book_service = fetch_books

    def fetch_by_id(self, book_id):
        return self.book_service(book_id)

    def fetch_all_books(self):
        return self.book_service()

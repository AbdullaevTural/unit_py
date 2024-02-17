
books = [
    {
        'ID': 1,
        'name': 'test1',
    },
    {
        'ID': 2,
        'name': 'test2',
    },
    {
        'ID': 3,
        'name': 'test3',
    },
    {
        'ID': 4,
        'name': 'test4',
    },
]


def fetch_books(book_id: int | None = None):
    if book_id:
        return filter(lambda book: book.ID == book_id, books)
    return books


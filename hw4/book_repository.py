
books = [
    {
        'ID': 1,
        'name': 'Jane Eyre',
    },
    {
        'ID': 2,
        'name': 'Jane Eyre',
    },
    {
        'ID': 3,
        'name': 'Jane Eyre',
    },
    {
        'ID': 4,
        'name': 'Jane Eyre',
    },
]


def fetch_books(book_id: int | None = None):
    if book_id:
        return filter(lambda book: book.ID == book_id, books)
    return books


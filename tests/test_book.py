from lib.book import Book

#Testing if Book object constructred with given 
#arguments
def test_book_construct():
    book = Book(1, "Test Book", "Test Author")
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author_name == "Test Author"
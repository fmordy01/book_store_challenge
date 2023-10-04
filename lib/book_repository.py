from lib.book import Book

class BookRepository():

    def __init__(self, connection):
        self._connection = connection

    # Selecting all records
    # No arguments
    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            book = Book(row['id'], row['title'], row['author_name'])
            books.append(book)
        return books
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books;

        # Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    
    #def find(self, id):
        # Executes the SQL query:
        # 'SELECT id, title, author_name FROM books WHERE id = %s', [id];

        # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    # def create(book)
       # self._connection.execute('INSERT INTO books (title, genre) VALUES (%s, %s), [
       #     book.name, book.genre
       # ])

    # def update(student)
    # 

    # def delete(student)
    # 
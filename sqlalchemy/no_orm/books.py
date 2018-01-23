from __future__ import print_function
from book import Book

class Books(object):
    def __init__(self, criteria=None):
        if criteria is None:
            self.__criteria__ = []
        else:
            self.__criteria__ = criteria

    def select(self, conn):
        cursor = conn.cursor()
        if len(self.__criteria__) > 0:
            cursor.execute('''
                SELECT b.id, title, name, published_in
                FROM books b
                JOIN authors a
                  ON b.author_id = a.id
                WHERE {} {} ?
            '''.format(
                    self.__criteria__[0],
                    self.__criteria__[1],
                ),
                (
                    self.__criteria__[2],
                ),
            )
        else:
            cursor.execute('''
                SELECT b.id, title, name, published_in
                FROM books b
                JOIN authors a
                  ON b.author_id == a.id
            ''')
        return cursor

    def update(self, conn, field, new_value):
        for row in self.select(conn):
            book = Book(
                row['id'],
                row['title'],
                row['author_id'],
                row['published_in'],
            )
            setattr(book, field, new_value)
            book.save(conn)

    def list(self, conn):
        for row in self.select(conn):
            for member in row:
                print(member, end=" ")
            print("")

    def delete(self, conn):
        for row in self.select(conn):
            book = Book(
                row['id'],
                row['title'],
                row['author_id'],
                row['published_in'],
            )
            book.delete(conn)
            print("")

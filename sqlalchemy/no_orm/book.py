from datetime import datetime
from authors import Authors
import sqlite3

class Book(object):
    def __init__(self, book_id, title, author_name, published_in):
        self.id = book_id
        self.title = title
        if not author_name is None:
            conn = sqlite3.connect('../db/books.db')
            authors = Authors(['name', '=', author_name])
            self.author_id = authors.select(conn).fetchone()[0]
            conn.close()
        self.published_in = published_in

    def save(self, conn):
        if self.id is None:
            conn.execute(
                'INSERT INTO books VALUES(?, ?, ?, ?)',
                (
                    self.id,
                    self.title,
                    self.author_id,
                    self.published_in,
                ),
            )
            conn.commit()
            self.id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
        else:
            conn.execute(
                'UPDATE books SET title = ?, author_id = ?, published_in = ? WHERE id = ?',
                (
                    self.title,
                    self.author_id,
                    self.published_in,
                    self.id,
                ),
            )
            conn.commit()

    def delete(self,conn):
        conn.execute(
            '''DELETE FROM books WHERE id = ?''',
            (self.id,),
        )
        conn.commit()

    @property
    def published_in(self):
        return self.__published_in.date()

    @published_in.setter
    def published_in(self, published_in):
        self.__published_in = datetime.strptime(published_in, '%Y-%m-%d')

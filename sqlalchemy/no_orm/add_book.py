#!/usr/bin/env python
from book import Book
import sqlite3
import sys

if len(sys.argv) != 4:
    print("ERROR: Book's title, author name, and date of publishing (YYYY-MM-DD) must be specified")
    sys.exit(1)

conn = sqlite3.connect('../db/books.db')
new_book = Book(None, sys.argv[1], sys.argv[2], sys.argv[3])
new_book.save(conn)
print(
    'Book {}, published in {}, written by {}, inserted with id {}'.format(
        new_book.title,
        new_book.published_in,
        new_book.author_id,
        new_book.id,
    ))
conn.close()

#!/usr/bin/env python
from author import Author
import sqlite3
import sys

if len(sys.argv) != 3:
    print("ERROR: Author's name and date of birth (YYYY-MM-DD) must be specified")
    sys.exit(1)

conn = sqlite3.connect('../db/books.db')
new_author = Author(None, sys.argv[1], sys.argv[2])
new_author.save(conn)
print(
    'Author {}, born on {}, inserted with id {}'.format(
        new_author.name,
        new_author.birth,
        new_author.id,
    ))
conn.close()

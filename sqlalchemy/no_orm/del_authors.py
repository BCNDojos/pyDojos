#!/usr/bin/env python
from authors import Authors
import sqlite3
import sys

conn = sqlite3.connect('../db/books.db')
conn.row_factory = sqlite3.Row
if len(sys.argv) == 1:
    authors = Authors()
elif len(sys.argv) == 4:
    authors = Authors(sys.argv[1:4])
else:
    print("ERROR: Either field, operator and value or empty arguments can be specified.")
    conn.close()
    sys.exit(1)

authors.delete(conn)
conn.close()

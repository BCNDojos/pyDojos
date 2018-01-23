#!/usr/bin/env python
from authors import Authors
import sqlite3
import sys

conn = sqlite3.connect('../db/books.db')
conn.row_factory = sqlite3.Row
if len(sys.argv) != 6:
    print("ERROR: Search field, operator, search value, updated field, and new value must be specified.")
    conn.close()
    sys.exit(1)
else:
    authors = Authors(sys.argv[1:4])

authors.update(conn, sys.argv[4], sys.argv[5])
conn.close()

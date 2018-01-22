#!/usr/bin/env python
from authors import Authors
import sqlite3

conn = sqlite3.connect('../db/books.db')
conn.row_factory = sqlite3.Row
authors = Authors()
authors.list(conn)
conn.close()

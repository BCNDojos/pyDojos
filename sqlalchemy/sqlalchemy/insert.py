from datetime import date
from base import Base, engine, Session
from models import Author, Book

Base.metadata.create_all(engine)

session = Session()

author_1 = Author('J.R.R. Tolkien', date(1892, 1, 3))
author_2 = Author('J.K. Rowling', date(1965, 7, 31))
author_3 = Author('Stephen King', date(1947, 9, 21))

book_1 = Book('The Hobbit', date(1937, 9, 21), author_1)
book_2 = Book('The Lord of the Rings', date(1954, 7, 29), author_1)
book_3 = Book('Harry Potter', date(1997, 6, 26), author_2)
book_4 = Book('Carrie', date(1974, 1, 1), author_3)
book_5 = Book('Salem Lot', date(1975, 1, 1), author_3)
book_6 = Book('The Shining', date(1977, 1, 1), author_3)
book_7 = Book('Rage', date(1977, 1, 1), author_3)

session.add(author_1)
session.add(author_2)
session.add(author_3)

session.add(book_1)
session.add(book_2)
session.add(book_3)
session.add(book_4)
session.add(book_5)
session.add(book_6)
session.add(book_7)

session.commit()
session.close()

from datetime import date
from base import Session, engine
from models import Base, Author, Book

Base.metadata.create_all(engine)
session = Session()

author_1 = Author(name='J.R.R. Tolkien', birth=date(1892, 1, 3))
author_2 = Author(name='J.K. Rowling', birth=date(1965, 7, 31))
author_3 = Author(name='Stephen King', birth=date(1947, 9, 21))

book_1 = Book(title='The Hobbit', published_in=date(1937, 9, 21), author_id=1)
book_2 = Book(title='The Lord of the Rings', published_in=date(1954, 7, 29), author_id=1)
book_3 = Book(title='Harry Potter', published_in=date(1997, 6, 26), author_id=2)
book_4 = Book(title='Carrie', published_in=date(1974, 1, 1), author_id=3)
book_5 = Book(title='Salem Lot', published_in=date(1975, 1, 1), author_id=3)
book_6 = Book(title='The Shining', published_in=date(1977, 1, 1), author_id=3)
book_7 = Book(title='Rage', published_in=date(1977, 1, 1), author_id=3)

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

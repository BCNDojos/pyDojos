from datetime import date
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    birth = Column(Date)
    books = relationship('Book', lazy='joined')

    def __init__(self, name: str = '', birth: str = '2000-01-01'):
        localdate = list(map((lambda item: int(item)), birth.split('-')))
        self.name = name
        self.birth = date(localdate[0], localdate[1], localdate[2])

    def __repr__(self):
        return '\n<Author id={0} name={1}, birth={2}, books={3}>' \
            .format(self.id, self.name, self.birth, self.books)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    published_in = Column(Date, nullable=True)
    author_id = Column(Integer, ForeignKey('authors.id'))

    def __repr__(self):
        return '\n<Book id={0}, title={1}, published_in={2}, author_id={3}>' \
            .format(self.id, self.title, self.published_in, self.author_id)

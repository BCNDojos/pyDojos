from datetime import date
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from base import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    birth = Column(Date)
    books = relationship('Book', backref='authors')

    def __init__(self, name: str, birth: date):
        self.name = name
        self.birth = birth


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    published_in = Column(Date, nullable=True)
    author_id = Column(Integer, ForeignKey('authors.id'))

    def __init__(self, title: str, published_in: date, authors: Author):
        self.title = title
        self.published_in = published_in
        self.authors = authors

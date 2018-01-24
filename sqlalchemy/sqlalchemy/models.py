from datetime import date
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, synonym
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    _birth = Column(Date)
    books = relationship('Book', lazy='joined')

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        if type(value) == date:
            self._birth = value
        else:
            localdate = list(map((lambda item: int(item)), value.split('-')))
            self._birth = date(localdate[0], localdate[1], localdate[2])

    birth = synonym('_birth', descriptor=birth)

    def __init__(self, **kwargs):
        birth = kwargs['birth']
        name = kwargs['name']

        self.name = name
        self.birth = birth

    def __repr__(self):
        return '\n<Author [id={0}] name={1}, birth={2}, books={3}>' \
            .format(self.id, self.name, self.birth, self.books)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    _published_in = Column(Date, nullable=True)
    author_id = Column(Integer, ForeignKey('authors.id'))

    @property
    def published_in(self):
        return self._published_in

    @published_in.setter
    def published_in(self, value):
        if type(value) == date:
            self._published_in = value
        else:
            localdate = list(map((lambda item: int(item)), value.split('-')))
            self._published_in = date(localdate[0], localdate[1], localdate[2])

    published_in = synonym('_published_in', descriptor=published_in)

    def __init__(self, **kwargs):
        title = kwargs['title']
        published_in = kwargs['published_in']
        author_id = kwargs['author_id']

        self.title = title
        self.published_in = published_in
        self.author_id = author_id

    def __repr__(self):
        return '\n<Book [id={0}], title={1}, published_in={2}, author_id={3}>' \
            .format(self.id, self.title, self.published_in, self.author_id)


table_class_list = [Author, Book]

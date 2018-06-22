from datetime import date
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    birth = Column(Date)
    # books = relationship('Book', lazy='joined')

    def __repr__(self):
        return self.name
---
# theme : "white"
transition: "slide"
highlightTheme: "darkula"
---

# sqlalchemy
### The Python SQL Toolkit and Object Relational Mapper

<small>Created by Michael Bayer</small>

---

## Features

* No ORM Required
* Unit Of Work
* Function-based query construction
* Modular and Extensible

SQLAlchemy includes dialects for SQLite, Postgresql, MySQL, Oracle, MS-SQL, Firebird, Sybase and others.

---

## Basic Implementation

--

1) Create engine and connection

    # base.py

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///books.db')
    Session = sessionmaker(bind=engine)

--

2) Create declarative model

    # models.py

    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String

    Base = declarative_base()


    class Author(Base):
        __tablename__ = 'authors'

        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String, nullable=False)

--

3) Create Session and Query

    # list.py

    from base import Session
    from models import Authors

    session = Session()

    session.query(Authors).all()

---

## Examples

--

#### List
    session.query(Table_Model_Class).all()

#### Add
    session.add(record_instance)
    session.commit()

#### Delete
    session.delete(record_instance)
    session.commit()

#### Update
    session.merge(record_instance)
    session.commit()

---

## Implementation

--

<small>base.py</small>

    # base.py

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('sqlite:///books.db')
    Session = sessionmaker(bind=engine)

--

<small>models.py</small>

    # models.py

    from datetime import date
    from sqlalchemy import Column, Integer, String, Date
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()


    class Author(Base):
        __tablename__ = 'authors'

        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String, nullable=False)
        birth = Column(Date)

        def __init__(self, **kwargs):
            birth = 
            name = kwargs['name']

            self.name = kwargs['name']
            self.birth = kwargs['birth']

        def __repr__(self):
            return '\n<Author [id={0}] name={1}, birth={2}, books={3}>' \
                .format(self.id, self.name, self.birth, self.books)

--

<small>list.py</small>

    # list.py

    from base import Session
    from models import Author

    session = Session()

    print(session.query(table_class).all())

--

<small>add.py</small>

    # add.py

    from base import Session
    from models import Author

    session = Session()

    params = {'name': 'Test Name',  'birth': '2017-02-02'}
    record = Author(**params)
    session.add(record)
    session.commit()

--

<small>delete.py</small>

    # delete.py

    from base import Session
    from models import Author

    session = Session()

    record = session.query(Author).get(1)
    session.delete(record)
    session.commit()

--

<small>update.py</small>

    # update.py

    from base import Session
    from models import Author

    session = Session()

    record = session.query(Author).get(1)
    setattr(record, 'name', 'test name')
    session.merge(record)
    session.commit()
    
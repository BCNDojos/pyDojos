from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()


def clear_screen():
    print('\n' * 40)

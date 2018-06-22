from base import Session
from models import Author
from datetime import date


session = Session()

objeto = session.query(Author).get(2)

session.delete(objeto)
session.commit()
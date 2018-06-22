from base import Session
from models import Author
from datetime import date


session = Session()

objeto = session.query(Author).get(1)

print('nombre original', objeto)

objeto.name = 'NombreAutor'

session.merge(objeto)
session.commit()

print('nombre modificado', objeto)
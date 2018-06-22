from base import Session, engine
from models import Author, Base
from datetime import date

Base.metadata.create_all(engine)
session = Session()

objeto = Author()

name = input('name: ')
birth = input('birth: ')

localdate = list(map((lambda item: int(item)), birth.split('-')))
new_birth = date(localdate[0], localdate[1], localdate[2])

objeto.name = name
objeto.birth = new_birth

session.add(objeto)
session.commit()

print(session.query(Author).all())

print(objeto.name, objeto.birth)
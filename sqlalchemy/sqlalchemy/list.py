from base import Session
from models import Author, Book

session = Session()
tables_class = [Author, Book]

if __name__ == '__main__':
    tables = {index: table for index, table in enumerate(tables_class)}

    while True:
        print('Tables list:', '\n')
        print(tables, '\n')
        res = input('Enter \'table #\' or \'x\' to exit: ')

        if res.lower() == 'x' or res == '':
            break
        else:
            table = tables.get(int(res), None)

            if table is not None:
                print(session.query(table).all())
                input('press any key to continue...')
            else:
                print('Table not found', '\n')

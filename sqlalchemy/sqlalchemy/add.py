from base import Session
from models import Author, Book

session = Session()
tables_class = [Author, Book]

if __name__ == '__main__':
    tables = {index: table for index, table in enumerate(tables_class)}

    while True:
        print('Add records:', '\n')
        print('Tables list:', '\n')
        print(tables, '\n')
        res = input('Enter \'table #\' or \'x\' to exit: ')

        if res.lower() == 'x' or res == '':
            break
        else:
            table = tables.get(int(res), None)

            if table is not None:
                # Retrieve list of columns
                columns = [col.name for col in table.__table__.columns if col.name != 'id']
                print(columns)

                # Initialize a new record
                record = table()

                for col in columns:
                    val = input('type a value for {0}: '.format(col))
                    print(val)
                    setattr(record, col, val)

                if input('Add record? y/n') == 'y':
                    session.add(record)
                    session.commit()
            else:
                print('Table not found', '\n')

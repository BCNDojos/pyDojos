from sqlalchemy import inspect
from base import Session, engine, Base, clear_screen
from models import Author, Book

session = Session()
inspector = inspect(engine)


def get_class_by_tablename(tablename: str):
    """
    Return class reference mapped to table.
    :param tablename: String with name of table.
    :return: Class reference or None.
    """
    for c in Base._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
            return c


def get_columns(table: str):
    column_list = [col['name'] for col in inspector.get_columns(table) if col['name'] != 'id']
    return column_list


if __name__ == '__main__':

    tables = {index: table for index, table in enumerate(inspector.get_table_names())}

    while True:
        clear_screen()
        print('Tables list:', '\n')
        print(tables, '\n')
        res = input('Enter \'table #\' or \'x\' to exit: ')

        if res.lower() == 'x' or res == '':
            break
        else:
            table = tables.get(int(res), None)
            table_class = get_class_by_tablename(table)

            if table_class is not None:
                resultset = session.query(table_class).all()
                columns = get_columns(table)
                mapped = [{col: getattr(record, col) for col in columns} for record in resultset]

                print('\n'.join(['-'*20, table.upper().center(20), '-'*20]))
                print(mapped)

                input('press any key to continue...')
            else:
                print('Table not found', '\n')


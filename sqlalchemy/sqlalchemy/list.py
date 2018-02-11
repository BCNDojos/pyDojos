from base import Session
from models import table_class_list

session = Session()


def list_all(table_class):
    print(session.query(table_class).all())


if __name__ == '__main__':
    tables = {index: table for index, table in enumerate(table_class_list)}

    while True:
        print('Tables list:', '\n')
        print(tables, '\n')
        user_response = input('Enter \'table #\' or \'x\' to exit: ')

        if user_response.lower() == 'x' or user_response == '':
            break
        else:
            # Get the Table Class
            table = tables.get(int(user_response), None)

            if table is not None:
                # Query to DB
                list_all(table)
                input('press any key to continue...')
            else:
                print('Table not found', '\n')

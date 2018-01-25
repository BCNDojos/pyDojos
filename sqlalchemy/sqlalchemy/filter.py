from base import Session
from models import table_class_list

session = Session()


if __name__ == '__main__':
    tables = {index: table for index, table in enumerate(table_class_list)}

    while True:
        print('Filter table:', '\n')
        print('Tables list:', '\n')
        print(tables, '\n')
        user_response = input('Enter \'table #\' or \'x\' to exit: ')

        if user_response.lower() == 'x' or user_response == '':
            break
        else:
            # Get the Table Class
            table = tables.get(int(user_response), None)

            if table is not None:
                columns = {index: col.name
                           for index, col in enumerate(table.__table__.columns)
                           if col.name != 'id'}

                print(columns, '\n')
                user_response = input('Enter \'column #\' or \'c\' to cancel: ')
                if user_response.lower() == 'c' or user_response == '':
                    pass
                else:
                    # Get the Column
                    column = columns.get(int(user_response), None)
                    criteria = '%' + input('Enter the criteria for [{0}]: '.format(column)) + '%'

                    if column is not None:
                        # Query to DB
                        print(session.query(table).filter(getattr(table, column, None).like(criteria)).all())

                input('press any key to continue...')
            else:
                print('Table not found', '\n')

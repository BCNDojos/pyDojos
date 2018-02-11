from base import Session
from models import table_class_list

session = Session()

if __name__ == '__main__':
    tables = {index: table for index, table in enumerate(table_class_list)}

    while True:
        print('Add records:', '\n')
        print('Tables list:', '\n')
        print(tables, '\n')
        user_response = input('Enter \'table #\' or \'x\' to exit: ')

        if user_response.lower() == 'x' or user_response == '':
            break
        else:
            table = tables.get(int(user_response), None)

            if table is not None:
                # Retrieve list of columns
                columns = [col.name for col in table.__table__.columns if col.name != 'id']
                print(columns)

                # Initialize a new record
                data = {}

                for col in columns:
                    value = input('type a value for {0}: '.format(col))
                    data[col] = value

                if input('Add record? y/n') == 'y':
                    record = table(**data)
                    session.add(record)
                    session.commit()
            else:
                print('Table not found', '\n')

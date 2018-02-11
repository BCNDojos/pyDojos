from base import Session
from models import table_class_list
from list import list_all

session = Session()

if __name__ == '__main__':
    tables = {index: table for index, table in enumerate(table_class_list)}

    while True:
        print('Delete records:', '\n')
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

                record_id = input('Enter \'record #\' or \'c\' to cancel...')
                if record_id.lower() != 'c' and record_id != '':
                    # Get the Record ID
                    record = session.query(table).get(record_id)

                    if input('Add record? y/n') == 'y' and record is not None:
                        session.delete(record)
                        session.commit()

            else:
                print('Table not found', '\n')

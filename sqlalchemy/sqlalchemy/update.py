from base import Session
from models import table_class_list
from list import list_all

session = Session()

if __name__ == '__main__':
    tables = {index: table for index, table in enumerate(table_class_list)}

    while True:
        print('Modify records:', '\n')
        print('Tables list:', '\n')
        print(tables, '\n')
        user_response = input('Enter \'table #\' or \'x\' to exit: ')

        if user_response.lower() == 'x' or user_response == '':
            break
        else:
            table = tables.get(int(user_response), None)

            if table is not None:
                # Retrieve list of columns
                columns = [col.name.replace('_', '') for col in table.__table__.columns if col.name != 'id']

                # List all records
                list_all(table)

                record_id = input('Enter \'record #\' or \'c\' to cancel...')
                if record_id.lower() != 'c' and record_id != '':

                    if input('Update record? y/n') == 'y' and record_id is not None:
                        # Get the Record ID
                        record = session.query(table).get(record_id)

                        for col in columns:
                            value = input('type new value for {0} [{1}]: '.format(col, getattr(record, col, None)))
                            if value is not None:
                                setattr(record, col, value)

                        session.merge(record)
                        session.commit()
            else:
                print('Table not found', '\n')

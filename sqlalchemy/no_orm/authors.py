from __future__ import print_function
from author import Author

class Authors(object):
    def __init__(self, criteria=None):
        if criteria is None:
            self.__criteria__ = []
        else:
            self.__criteria__ = criteria

    def select(self, conn):
        cursor = conn.cursor()
        if len(self.__criteria__) > 0:
            cursor.execute(
                '''SELECT * FROM authors WHERE {} {} ?'''.format(
                    self.__criteria__[0],
                    self.__criteria__[1],
                ),
                (
                    self.__criteria__[2],
                ),
            )
        else:
            cursor.execute('SELECT * FROM authors')
        return cursor

    def update(self, conn, field, new_value):
        for row in self.select(conn):
            author = Author(
                row['id'],
                row['name'],
                row['birth'],
            )
            setattr(author, field, new_value)
            author.save(conn)

    def list(self, conn):
        for row in self.select(conn):
            for member in row:
                print(member, end=" ")
            print("")

    def delete(self, conn):
        for row in self.select(conn):
            author = Author(
                row['id'],
                row['name'],
                row['birth'],
            )
            author.delete(conn)
            print("")

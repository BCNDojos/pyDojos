from author import Author

class Authors(object):
    def __init__(self):
        pass

    def list(self, conn):
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM authors''')
        for row in cursor:
            for member in row:
                print member,
            print("")

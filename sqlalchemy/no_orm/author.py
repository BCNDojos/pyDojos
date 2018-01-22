from datetime import datetime

class Author(object):
    def __init__(self, author_id, name, birth):
        self.id = author_id
        self.name = name
        self.birth = birth

    def save(self, conn):
        conn.execute(
            'INSERT INTO authors VALUES(?, ?, ?)',
            (
                self.id,
                self.name,
                self.birth,
            ),
        )
        conn.commit()
        self.id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]

    def delete(self,conn):
        conn.execute(
            '''DELETE FROM authors WHERE id = ?''',
            (self.id,),
        )
        conn.commit()

    @property
    def birth(self):
        return self.__birth.date()

    @birth.setter
    def birth(self, birth):
        self.__birth = datetime.strptime(birth, '%Y-%m-%d')

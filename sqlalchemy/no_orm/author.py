from datetime import datetime

class Author(object):
    def __init__(self, author_id, name, birth):
        self.id = author_id
        self.name = name
        self.birth = birth

    def save(self, conn):
        if self.id is None:
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
        else:
            conn.execute(
                'UPDATE authors SET name = ?, birth = ? WHERE id = ?',
                (
                    self.name,
                    self.birth,
                    self.id,
                ),
            )
            conn.commit()

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

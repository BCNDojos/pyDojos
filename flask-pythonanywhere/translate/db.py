import sqlite3

class TranslateDB(object):
    __db_name = 'translate.db'
    __table_name = 'translations'

    def __init__(self):
        sql = 'CREATE TABLE IF NOT EXISTS {table} (word string, trans string)' \
            .format(table=self.__table_name)

        self.__execute(sql)

    def __connect_db(self):
        self.__connection = sqlite3.connect(self.__db_name)
        self.__cursor = self.__connection.cursor()

        return self

    def __close_db(self):
        self.__connection.commit()
        self.__connection.close()

    def __execute(self, sql):
        self.__connect_db() \
            .__cursor.execute(sql)

    def get_all_translations(self):
        sql = 'SELECT word, trans FROM {table}' \
            .format(table=self.__table_name)
        self.__execute(sql)
        result = [{ row[0]: row[1] } for row in self.__cursor.fetchall()]
        self.__close_db()

        return result

    def add_translation(self, word, trans):
        sql = 'INSERT INTO {table} (word, trans) VALUES ("{word}", "{trans}")' \
            .format(table=self.__table_name, word=word, trans=trans)
        self.__execute(sql)
        self.__close_db()

    def get_translation(self, word):
        sql = 'SELECT trans FROM {table} WHERE word="{word}"' \
            .format(table=self.__table_name, word=word)
        self.__execute(sql)
        result = self.__cursor.fetchone()
        self.__close_db()

        if result:
            return result[0]

        return None

    def update_translation(self, word, trans):
        sql = 'UPDATE {table} SET trans="{trans}" WHERE word="{word}"' \
            .format(table=self.__table_name, word=word, trans=trans)
        self.__execute(sql)
        self.__close_db()

    def remove_translation(self, word):
        sql = 'DELETE FROM {table} WHERE word="{word}"' \
            .format(table=self.__table_name, word=word)
        self.__execute(sql)
        self.__close_db()


translateDB = TranslateDB()

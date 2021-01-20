#importing from SQlite
import sqlite3

class Database():

    def __init__(self):
        self.connection = sqlite3.connect("dbase.db")
        self.createTable()

    def createTable(self):
        c = self.connection.cursor()

        c.execute("""create table if not exists users (
                     userid integer primary key autoincrement,
                     name text,
                     phone text,
                     email text,
                     username text,
                     password text)""")
        self.connection.commit()
        c.close()

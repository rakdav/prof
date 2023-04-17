from PyQt5.QtSql import *


class Connect:
    def __init__(self, server, dbname, username, password):
        self.server = server
        self.dbname = dbname
        self.username = username
        self.password = password

    def get_connect(self):
        db = QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName(f'Driver={{SQL SERVER}}; '
                           f'Server={self.server}; '
                           f'Database={self.dbname}; '
                           f'UID={self.username}; '
                           f'PWD={self.password}')
        return db

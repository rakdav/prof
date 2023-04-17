from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlQuery

import autorize
import choice
import sys
import group
import reg
import single
import Connect


class win_choice(QtWidgets.QWidget, choice.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_group.clicked.connect(self.btn_group_click)
        self.btn_single.clicked.connect(self.btn_single_click)
        self.log_win = None

    def btn_group_click(self):
        self.log_win = log_in_window()
        self.log_win.show()

    def btn_single_click(self):
        self.log_win = log_in_window()
        self.log_win.show()


class group_window(QtWidgets.QWidget, group.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class single_window(QtWidgets.QWidget, single.Ui_Form):
    def __init__(self, User=None):
        super().__init__()
        self.User = User
        self.setupUi(self)
        if self.User is not None:
            pass


def connect_to_sql_server():
    return Connect.Connect("HOMEPC\SQLEXPRESS", "main_db", "user1", "user1").get_connect()


class log_in_window(QtWidgets.QWidget, autorize.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_enter.clicked.connect(self.pb_enter_click)

    def pb_enter_click(self):
        db_connect = connect_to_sql_server()
        db_connect.open()
        query = QSqlQuery(db_connect)
        text_query = f"SELECT first_name FROM UserTable WHERE login='{self.le_login.text()}' " \
                     f"AND password='{self.le_password.text()}'"
        print(text_query)
        query.prepare(text_query)
        query.exec()
        if query.record() != 0:
            query.first()
            # print(query.value("first_name"))

        db_connect.close()


class reg_window(QtWidgets.QWidget, reg.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = win_choice()
    ui.show()
    sys.exit(app.exec_())

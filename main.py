from PyQt5 import QtWidgets

import autorize
import choice
import sys
import group
import reg
import single


class win_choice(QtWidgets.QWidget, choice.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_group.clicked.connect(self.btn_group_click)
        self.btn_single.clicked.connect(self.btn_single_click)
        self.group_win = None
        self.single_win = None

    def btn_group_click(self):
        self.group_win = log_in_window()
        self.group_win.show()

    def btn_single_click(self):
        self.single_win = log_in_window()
        self.single_win.show()


class group_window(QtWidgets.QWidget, group.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class single_window(QtWidgets.QWidget, single.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class log_in_window(QtWidgets.QWidget, autorize.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class reg_window(QtWidgets.QWidget, reg.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = win_choice()
    ui.show()
    sys.exit(app.exec_())

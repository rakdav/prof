# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autorize.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 173)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("padding: 5;\n"
"background-color: rgb(255, 170, 0);\n"
"border: None;\n"
"border-radius: 12;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_login = QtWidgets.QLineEdit(self.frame)
        self.le_login.setObjectName("le_login")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_login)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.le_password = QtWidgets.QLineEdit(self.frame)
        self.le_password.setObjectName("le_password")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_password)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_enter = QtWidgets.QPushButton(self.frame_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Arrows/arrow-right-s-line.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_enter.setIcon(icon)
        self.pb_enter.setObjectName("pb_enter")
        self.horizontalLayout.addWidget(self.pb_enter, 0, QtCore.Qt.AlignHCenter)
        self.pb_reg = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pb_reg.setFont(font)
        self.pb_reg.setStyleSheet("color: rgb(85, 85, 255);")
        self.pb_reg.setFlat(True)
        self.pb_reg.setObjectName("pb_reg")
        self.horizontalLayout.addWidget(self.pb_reg, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Вход в сисетму"))
        self.label_2.setText(_translate("Form", "Логин"))
        self.label_3.setText(_translate("Form", "Пароль"))
        self.pb_enter.setText(_translate("Form", "Вход"))
        self.pb_reg.setText(_translate("Form", "Нет аккаунта? зарегестрируйтесь!"))

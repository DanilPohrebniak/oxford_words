# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\PyQt\oxford_words\resources\login_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.horizontalWidget.setStyleSheet("background-image: url(\"D:/Python/PyQt/oxford_words/fon.png\");\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"background-attachment: fixed;\n"
"background-clip: padding-box")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMaximumSize(QtCore.QSize(350, 450))
        self.verticalWidget.setStyleSheet("background: white;\n"
"border-radius: 15px;")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loggin = QtWidgets.QLabel(self.verticalWidget)
        self.loggin.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.loggin.setFont(font)
        self.loggin.setAlignment(QtCore.Qt.AlignCenter)
        self.loggin.setObjectName("loggin")
        self.verticalLayout.addWidget(self.loggin)
        self.separator = QtWidgets.QFrame(self.verticalWidget)
        self.separator.setMaximumSize(QtCore.QSize(16777215, 2))
        self.separator.setStyleSheet("background-color: rgb(218, 220, 220);")
        self.separator.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.separator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.separator.setObjectName("separator")
        self.verticalLayout.addWidget(self.separator)
        self.usernameWidget = QtWidgets.QWidget(self.verticalWidget)
        self.usernameWidget.setMaximumSize(QtCore.QSize(16777215, 55))
        self.usernameWidget.setObjectName("usernameWidget")
        self.username_layout = QtWidgets.QVBoxLayout(self.usernameWidget)
        self.username_layout.setSpacing(0)
        self.username_layout.setObjectName("username_layout")
        self.username = QtWidgets.QLineEdit(self.usernameWidget)
        self.username.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.username.setText("")
        self.username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.username.setObjectName("username")
        self.username_layout.addWidget(self.username)
        self.separator_2 = QtWidgets.QFrame(self.usernameWidget)
        self.separator_2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.separator_2.setStyleSheet("background-color: rgb(218, 220, 220);")
        self.separator_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.separator_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.separator_2.setObjectName("separator_2")
        self.username_layout.addWidget(self.separator_2)
        self.verticalLayout.addWidget(self.usernameWidget)
        self.passwordWidget = QtWidgets.QWidget(self.verticalWidget)
        self.passwordWidget.setMaximumSize(QtCore.QSize(16777215, 55))
        self.passwordWidget.setObjectName("passwordWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.passwordWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.password = QtWidgets.QLineEdit(self.passwordWidget)
        self.password.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.password.setStyleSheet("")
        self.password.setText("")
        self.password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password)
        self.separator_3 = QtWidgets.QFrame(self.passwordWidget)
        self.separator_3.setMaximumSize(QtCore.QSize(16777215, 2))
        self.separator_3.setStyleSheet("background-color: rgb(218, 220, 220);")
        self.separator_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.separator_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.separator_3.setObjectName("separator_3")
        self.verticalLayout_2.addWidget(self.separator_3)
        self.verticalLayout.addWidget(self.passwordWidget)
        self.info_message = QtWidgets.QLabel(self.verticalWidget)
        self.info_message.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_message.setFont(font)
        self.info_message.setStyleSheet("color: rgb(255, 126, 128);")
        self.info_message.setText("")
        self.info_message.setAlignment(QtCore.Qt.AlignCenter)
        self.info_message.setObjectName("info_message")
        self.verticalLayout.addWidget(self.info_message)
        self.loginButton = QtWidgets.QPushButton(self.verticalWidget)
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.loginButton.setFont(font)
        self.loginButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.loginButton.setStyleSheet("background: #05cbf2;\n"
"border-radius: 10px;")
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.createUserButton = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createUserButton.sizePolicy().hasHeightForWidth())
        self.createUserButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setUnderline(True)
        self.createUserButton.setFont(font)
        self.createUserButton.setObjectName("createUserButton")
        self.verticalLayout.addWidget(self.createUserButton)
        self.horizontalLayout.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loggin.setText(_translate("MainWindow", "LOGIN"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.createUserButton.setText(_translate("MainWindow", "Create user"))

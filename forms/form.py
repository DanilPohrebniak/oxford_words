# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\PyQt\oxford_words\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1215, 568)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(143, 255, 160);\n"
"    transition: background-color 0.5s ease-in-out;\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        # self.centralwidget.setStyleSheet("background-image: url(\"D:/Python/PyQt/oxford_words/fon.png\");\n"
        self.centralwidget.setStyleSheet("background-image: url(resources/fon.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"background-attachment: fixed;\n"
"background-clip: padding-box")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setStyleSheet("background-image: url(:/newPrefix/fon.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"background-attachment: fixed;")
        self.mainWidget.setObjectName("mainWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.mainWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.eng_section = QtWidgets.QWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eng_section.sizePolicy().hasHeightForWidth())
        self.eng_section.setSizePolicy(sizePolicy)
        self.eng_section.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.eng_section.setObjectName("eng_section")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.eng_section)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.engButton_4 = QtWidgets.QPushButton(self.eng_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engButton_4.sizePolicy().hasHeightForWidth())
        self.engButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.engButton_4.setFont(font)
        self.engButton_4.setText("")
        self.engButton_4.setObjectName("engButton_4")
        self.gridLayout_3.addWidget(self.engButton_4, 2, 0, 1, 1)
        self.engButton_3 = QtWidgets.QPushButton(self.eng_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engButton_3.sizePolicy().hasHeightForWidth())
        self.engButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.engButton_3.setFont(font)
        self.engButton_3.setStyleSheet("")
        self.engButton_3.setText("")
        self.engButton_3.setObjectName("engButton_3")
        self.gridLayout_3.addWidget(self.engButton_3, 1, 0, 1, 1)
        self.eng_space_foot = QtWidgets.QFrame(self.eng_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eng_space_foot.sizePolicy().hasHeightForWidth())
        self.eng_space_foot.setSizePolicy(sizePolicy)
        self.eng_space_foot.setMaximumSize(QtCore.QSize(16777215, 350))
        self.eng_space_foot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eng_space_foot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eng_space_foot.setObjectName("eng_space_foot")
        self.gridLayout_3.addWidget(self.eng_space_foot, 5, 0, 1, 1)
        self.engButton = QtWidgets.QPushButton(self.eng_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engButton.sizePolicy().hasHeightForWidth())
        self.engButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.engButton.setFont(font)
        self.engButton.setText("")
        self.engButton.setObjectName("engButton")
        self.gridLayout_3.addWidget(self.engButton, 4, 0, 1, 1)
        self.engButton_2 = QtWidgets.QPushButton(self.eng_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engButton_2.sizePolicy().hasHeightForWidth())
        self.engButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.engButton_2.setFont(font)
        self.engButton_2.setText("")
        self.engButton_2.setObjectName("engButton_2")
        self.gridLayout_3.addWidget(self.engButton_2, 3, 0, 1, 1)
        self.eng_space_head = QtWidgets.QFrame(self.eng_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eng_space_head.sizePolicy().hasHeightForWidth())
        self.eng_space_head.setSizePolicy(sizePolicy)
        self.eng_space_head.setMaximumSize(QtCore.QSize(16777215, 200))
        self.eng_space_head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.eng_space_head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.eng_space_head.setObjectName("eng_space_head")
        self.gridLayout_3.addWidget(self.eng_space_head, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.eng_section, 1, 0, 1, 1)
        self.rus_section = QtWidgets.QWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rus_section.sizePolicy().hasHeightForWidth())
        self.rus_section.setSizePolicy(sizePolicy)
        self.rus_section.setObjectName("rus_section")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.rus_section)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.rusButton = QtWidgets.QPushButton(self.rus_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rusButton.sizePolicy().hasHeightForWidth())
        self.rusButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.rusButton.setFont(font)
        self.rusButton.setText("")
        self.rusButton.setObjectName("rusButton")
        self.gridLayout_4.addWidget(self.rusButton, 4, 0, 1, 1)
        self.rusButton_2 = QtWidgets.QPushButton(self.rus_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rusButton_2.sizePolicy().hasHeightForWidth())
        self.rusButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.rusButton_2.setFont(font)
        self.rusButton_2.setText("")
        self.rusButton_2.setObjectName("rusButton_2")
        self.gridLayout_4.addWidget(self.rusButton_2, 1, 0, 1, 1)
        self.rusButton_3 = QtWidgets.QPushButton(self.rus_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rusButton_3.sizePolicy().hasHeightForWidth())
        self.rusButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.rusButton_3.setFont(font)
        self.rusButton_3.setText("")
        self.rusButton_3.setObjectName("rusButton_3")
        self.gridLayout_4.addWidget(self.rusButton_3, 2, 0, 1, 1)
        self.rusButton_4 = QtWidgets.QPushButton(self.rus_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rusButton_4.sizePolicy().hasHeightForWidth())
        self.rusButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.rusButton_4.setFont(font)
        self.rusButton_4.setText("")
        self.rusButton_4.setObjectName("rusButton_4")
        self.gridLayout_4.addWidget(self.rusButton_4, 3, 0, 1, 1)
        self.rus_space_head = QtWidgets.QFrame(self.rus_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rus_space_head.sizePolicy().hasHeightForWidth())
        self.rus_space_head.setSizePolicy(sizePolicy)
        self.rus_space_head.setMaximumSize(QtCore.QSize(16777215, 200))
        self.rus_space_head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rus_space_head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rus_space_head.setObjectName("rus_space_head")
        self.gridLayout_4.addWidget(self.rus_space_head, 0, 0, 1, 1)
        self.rus_space_foot = QtWidgets.QFrame(self.rus_section)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rus_space_foot.sizePolicy().hasHeightForWidth())
        self.rus_space_foot.setSizePolicy(sizePolicy)
        self.rus_space_foot.setMaximumSize(QtCore.QSize(16777215, 350))
        self.rus_space_foot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rus_space_foot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rus_space_foot.setObjectName("rus_space_foot")
        self.gridLayout_4.addWidget(self.rus_space_foot, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.rus_section, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.mainWidget, 1, 0, 1, 1)
        self.footWidget = QtWidgets.QWidget(self.centralwidget)
        self.footWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.footWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.footWidget.setStyleSheet("background-image: url(:/newPrefix/back.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"background-attachment: fixed;\n"
"background-clip: padding-box;")
        self.footWidget.setObjectName("footWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.footWidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.nextButton = QtWidgets.QPushButton(self.footWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setMinimumSize(QtCore.QSize(300, 40))
        self.nextButton.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("QPushButton:pressed {\n"
"    background-color: rgb(187, 211, 255);\n"
"    transition: background-color 0.5s ease-in-out;\n"
"}")
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_5.addWidget(self.nextButton, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.footWidget, 4, 0, 1, 1)
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setMinimumSize(QtCore.QSize(0, 35))
        self.verticalWidget.setStyleSheet("background-image: url(:/newPrefix/back.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;\n"
"background-attachment: fixed;\n"
"background-clip: padding-box;")
        self.verticalWidget.setObjectName("verticalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.complete_label = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.complete_label.setFont(font)
        self.complete_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.complete_label.setObjectName("complete_label")
        self.horizontalLayout.addWidget(self.complete_label)
        self.complete = QtWidgets.QPushButton(self.verticalWidget)
        self.complete.setMaximumSize(QtCore.QSize(32, 32))
        self.complete.setStyleSheet("background-color: #E04F5F;")
        self.complete.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.complete.setIcon(icon)
        self.complete.setIconSize(QtCore.QSize(32, 32))
        self.complete.setObjectName("complete")
        self.horizontalLayout.addWidget(self.complete)
        self.gridLayout_2.addWidget(self.verticalWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.complete_label.setText(_translate("MainWindow", "Сomplete the training"))
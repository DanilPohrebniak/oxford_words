import forms.profile as profile
import utils.db_utils as db_utils

from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, profile.Ui_MainWindow):
    def __init__(self, login):
        super().__init__()
        self.main_window = None
        self.setupUi(self)
        self.setWindowTitle('Profile')
        self.login = login
        self.user = db_utils.UserDB()
        self.greetings.setText('Hey ' + login + '. Your current score is: ' + str(self.user.get_user_score(self.login)))
        self.pressing_logout()

    def pressing_logout(self):
        self.backButton.clicked.connect(lambda: self.open_main_menu())

    def open_main_menu(self):
        import app.main_menu as main_window
        self.main_window = main_window.MainWindow(self.login)
        self.close()
        self.main_window.show()
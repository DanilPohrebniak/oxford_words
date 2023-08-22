import forms.main_menu as home_page

from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, home_page.Ui_MainWindow):
    def __init__(self, login):
        super().__init__()
        self.main_window = None
        self.setupUi(self)
        self.setWindowTitle('Oxford words')
        self.login = login
        self.username.setText(login)
        self.pressing_logout()
        self.pressing_training()
        self.pressing_add_word()
        self.pressing_profile()

    def pressing_logout(self):
        self.logout.clicked.connect(lambda: self.open_login_form())

    def pressing_training(self):
        self.trainingButton.clicked.connect(lambda: self.open_training())

    def pressing_add_word(self):
        self.addWordButton.clicked.connect(lambda: self.add_word())

    def pressing_profile(self):
        self.profileButton.clicked.connect(lambda: self.open_profile())

    def open_login_form(self):
        import main as login_form
        self.main_window = login_form.App()
        self.close()
        self.main_window.show()

    def open_training(self):
        import app.form as form
        self.main_window = form.MainWindow(self.login)
        self.close()
        self.main_window.show()

    def add_word(self):
        import app.add_word as form
        self.main_window = form.MainWindow(self.login)
        self.close()
        self.main_window.show()

    def open_profile(self):
        import app.profile as form
        self.main_window = form.MainWindow(self.login)
        self.close()
        self.main_window.show()


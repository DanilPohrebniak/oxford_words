import sys
import forms.login_form as login

from PyQt5 import QtWidgets
import utils.db_utils as db_utils


class App(QtWidgets.QMainWindow, login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setupUi(self)
        self.user = db_utils.UserDB()
        self.pressing_login()
        self.pressing_register()

    def pressing_login(self):
        self.loginButton.clicked.connect(lambda: self.filling_check())

    def pressing_register(self):
        self.createUserButton.clicked.connect(lambda: self.open_register())

    def open_register(self):
        import app.register_form as register_form
        self.main_window = register_form.App()
        self.close()
        self.main_window.show()

    def filling_check(self):
        if self.username.text() == '' or self.password.text() == '':
            self.info_message.setText('Check the fields')
            return
        self.info_message.setText('')
        self.check()

    def check(self):
        import app.main_menu as mw
        if self.user.check_user(self.username.text(), self.password.text()):
            self.main_window = mw.MainWindow(self.username.text())
            self.close()
            self.main_window.show()
        else:
            self.info_message.setText('Check the entered data')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

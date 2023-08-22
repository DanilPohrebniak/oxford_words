import sys
import forms.register_form as register

from PyQt5 import QtWidgets
import utils.db_utils as db_utils


class App(QtWidgets.QMainWindow, register.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setupUi(self)
        self.user = db_utils.UserDB()
        self.pressing_login()

    def pressing_login(self):
        self.loginButton.clicked.connect(lambda: self.register())

    def register(self):
        if self.username.text() == '' or self.password.text() == '':
            self.info_message.setText('Check the fields')

        if self.user.create_user(self.username.text(), self.password.text()):
            self.open_main_menu()
        else:
            self.info_message.setText('User already exists')

    def open_main_menu(self):
        import app.main_menu as mw
        self.main_window = mw.MainWindow(self.username.text())
        self.close()
        self.main_window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

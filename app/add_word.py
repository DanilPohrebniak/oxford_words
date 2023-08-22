import forms.add_word as add_word

from utils.db_utils import WordDB
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, add_word.Ui_MainWindow):
    def __init__(self, login):
        super().__init__()
        self.main_window = None
        self.setupUi(self)
        self.setWindowTitle('Oxford words')
        self.login = login
        self.pressing_logout()
        self.pressing_save()

    def pressing_logout(self):
        self.backButton.clicked.connect(lambda: self.open_main_menu())

    def pressing_save(self):
        self.saveButton.clicked.connect(lambda: self.save_word())

    def open_main_menu(self):
        import app.main_menu as main_window
        self.main_window = main_window.MainWindow(self.login)
        self.close()
        self.main_window.show()

    def save_word(self):
        if self.eng_word.text() == '' or self.rus_word.text() == '':
            self.info_message.setText('The field is not filled in')
        else:
            element = WordDB()
            if element.check_existing_word(self.eng_word.text()):
                element.add_new_word(self.eng_word.text(), self.rus_word.text())
                self.open_main_menu()
            else:
                self.info_message.setText('Word already exists in the vocabulary.')



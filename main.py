import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import sounddevice as sd
import random
import forms.main_form as form
import utils.db_utils as db_utils
import utils.voicing_text as voicing


class MainWindow(QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        sd.query_devices()
        self.setupUi(self)
        self.score = 0
        self.db = db_utils.DB()
        self.voicing = voicing.Voicing()
        self.words = []
        self.selected_eng_button = None
        self.selected_rus_button = None
        for button in [self.engButton, self.engButton_2, self.engButton_3, self.engButton_4,
                       self.rusButton, self.rusButton_2, self.rusButton_3, self.rusButton_4]:
            button.clicked.connect(self.button_clicked)

        self.nextButton.clicked.connect(lambda: self.update_words())
        self.update_words()

    def update_words(self):
        self.words = self.db.fetch_words()
        random.shuffle(self.words)

        eng_buttons = [self.engButton, self.engButton_2, self.engButton_3, self.engButton_4]
        rus_buttons = [self.rusButton, self.rusButton_2, self.rusButton_3, self.rusButton_4]

        eng_words = [word[0] for word in self.words]
        rus_words = [word[1] for word in self.words]

        for i in range(4):
            eng_buttons[i].setText(eng_words[i])
            eng_buttons[i].setEnabled(True)

            rus_buttons[i].setText(rus_words[i])
            rus_buttons[i].setEnabled(True)

    def button_clicked(self):
        button = self.sender()  # Получаем отправителя события (нажатой кнопки)

        if button in [self.engButton, self.engButton_2, self.engButton_3, self.engButton_4]:
            # Выбрана английская кнопка
            self.selected_eng_button = button
            self.speak_text_from_button()

        if self.selected_eng_button is not None and self.selected_rus_button is not None:
            # Обе кнопки уже выбраны, ничего не делаем
            return

        if self.selected_eng_button is not None:
            # Проверяем соответствие русской кнопки
            if button in [self.rusButton, self.rusButton_2, self.rusButton_3, self.rusButton_4]:
                eng_text = self.selected_eng_button.text()
                rus_text = button.text()
                # if self.check_translation(eng_text, rus_text):
                if self.db.check_translation(eng_text, rus_text):
                    # Правильный перевод, делаем обе кнопки недоступными
                    self.score += 1
                    self.selected_eng_button.setEnabled(False)
                    button.setEnabled(False)
                else:
                    if self.score > 0:
                        self.score -= 1
                    # Неправильный перевод, продолжаем выбирать дальше
                    self.selected_eng_button = button
                    self.selected_rus_button = None
            return

        elif button in [self.rusButton, self.rusButton_2, self.rusButton_3, self.rusButton_4]:
            # Выбрана русская кнопка
            self.selected_rus_button = button

    def speak_text_from_button(self):
        button = self.sender()  # Получаем отправителя события (нажатой кнопки)
        self.voicing.speak_text(button.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

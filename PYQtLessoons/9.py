import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QVBoxLayout, QLineEdit, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 390, 50)
        self.setWindowTitle('Случайная строка')

        self.btn = QPushButton('Получить', self)
        self.btn.move(0, 0)
        self.btn.resize(80, 30)
        self.btn.clicked.connect(self.choice)
        self.ed = QLineEdit(self)
        self.ed.move(100, 0)
        self.ed.resize(280, 30)

    def choice(self):
        with open('output.txt', encoding='utf-8') as f:
            lines = f.readlines()
            self.ed.setText(lines[randint(0, len(lines)-1)])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

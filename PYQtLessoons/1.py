import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLineEdit


class FocusWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name_input_2 = QLineEdit(self)
        self.name_input_1 = QLineEdit(self)
        self.btn = QPushButton('->', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 462, 120)
        self.setWindowTitle('Фокус со словами')

        self.btn.resize(80, 40)
        self.btn.move(190, 30)
        self.btn.clicked.connect(self.change)

        self.name_input_1.resize(180, 40)
        self.name_input_1.move(1, 30)

        self.name_input_2.resize(180, 40)
        self.name_input_2.move(280, 30)

    def change(self):
        if self.btn.text() == '->' and self.name_input_1 is not None:
            self.btn.setText('<-')
            self.name_input_2.setText(self.name_input_1.text())
            self.name_input_1.clear()
        elif self.btn.text() == '<-' and self.name_input_2 is not None:
            self.btn.setText('->')
            self.name_input_1.setText(self.name_input_2.text())
            self.name_input_2.clear()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FocusWindow()
    ex.show()
    sys.exit(app.exec())

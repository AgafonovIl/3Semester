import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit


class Check(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 462, 120)
        self.setWindowTitle('Арифмометр')

        self.btn1 = QPushButton('+', self)
        self.btn1.resize(60, 40)
        self.btn1.move(100, 30)
        self.btn1.clicked.connect(lambda: self.ariphmetical_operations(self.btn1.text()))

        self.btn2 = QPushButton('-', self)
        self.btn2.resize(60, 40)
        self.btn2.move(160, 30)
        self.btn2.clicked.connect(lambda: self.ariphmetical_operations(self.btn2.text()))

        self.btn3 = QPushButton('*', self)
        self.btn3.resize(60, 40)
        self.btn3.move(220, 30)
        self.btn3.clicked.connect(lambda: self.ariphmetical_operations(self.btn3.text()))

        self.name_input_1 = QLineEdit('0', self)
        self.name_input_1.resize(60, 40)
        self.name_input_1.move(35, 30)

        self.name_input_2 = QLineEdit('0', self)
        self.name_input_2.resize(60, 40)
        self.name_input_2.move(285, 30)

        self.label = QLabel(self)
        self.label.setText('=')
        self.label.move(360, 40)

        self.name_input_3 = QLineEdit(self)
        self.name_input_3.resize(60, 40)
        self.name_input_3.move(385, 30)
        self.name_input_3.setEnabled(False)



    def ariphmetical_operations(self, sign):
        if sign == '+':
            self.name_input_3.setText(str(int(self.name_input_1.text()) + int(self.name_input_2.text())))
        elif sign == '-':
            self.name_input_3.setText(str(int(self.name_input_1.text()) - int(self.name_input_2.text())))
        elif sign == '*':
            self.name_input_3.setText(str(int(self.name_input_1.text()) * int(self.name_input_2.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Check()
    ex.show()
    sys.exit(app.exec_())

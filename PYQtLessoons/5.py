import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QApplication, QWidget,
                             QGridLayout, QButtonGroup)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 550, 120)
        self.setWindowTitle('Крестики-нолики')

        self.steps_of_x = []
        self.steps_of_o = []
        self.change = QButtonGroup()
        self.button0 = QRadioButton("0")
        self.buttonX = QRadioButton("X")
        self.buttonX.clicked.connect(self.for_x)
        self.button0.clicked.connect(self.for_o)

        self.button_start = QPushButton('Начать')

        self.text = QLabel("")
        self.layout = QGridLayout()
        self.zero = 0
        self.x = 0
        self.layout.addWidget(self.button0, 0, 1)
        self.layout.addWidget(self.buttonX, 0, 0)
        self.layout.addWidget(self.text, 4, 1)
        self.layout.addWidget(self.button_start, 5, 1)
        y = 1
        x = 0
        self.buttons = []
        self.button_start.clicked.connect(self.start)
        for i in range(9):
            self.button = QPushButton()
            self.button.setObjectName(str(i))
            self.buttons.append(self.button)
            self.layout.addWidget(self.button, y, x)
            self.button.clicked.connect(lambda state, numb=i: self.game(numb))
            if x == 2:
                x = 0
                y = y + 1
            else:
                x = x + 1
        self.setLayout(self.layout)

    def for_o(self):
        self.zero = 1
        self.x = 0

    def for_x(self):
        self.zero = 0
        self.x = 1

    def game(self, numb):
        winPos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        if self.zero == 1:
            self.sender().setText('O')
            self.sender().setEnabled(False)
            self.steps_of_o.append(numb)
            self.x = 1
            self.zero = 0
            if len(self.steps_of_o) == 5:
                self.text.setText('Ничья!')
                self.end()

            for i in range(len(winPos)):
                count = 0
                for j in range(len(self.steps_of_o)):
                    if self.steps_of_o[j] in winPos[i]:
                        count += 1
                if count == 3:
                    self.text.setText('0 победил!')
                    self.end()
                    break

        elif self.x == 1:
            self.sender().setText('X')
            self.sender().setEnabled(False)
            self.steps_of_x.append(numb)
            if len(self.steps_of_x) == 5:
                self.text.setText('Ничья!')
                self.end()

            self.zero = 1
            self.x = 0
            for i in range(len(winPos)):
                count = 0
                for j in range(len(self.steps_of_x)):
                    if self.steps_of_x[j] in winPos[i]:
                        count += 1
                if count == 3:
                    self.text.setText('X победил!')
                    self.end()
                    break

    def end(self):
        for i in range(9):
            if not self.buttons[i].isChecked():
                self.buttons[i].setEnabled(False)
        self.button_start.setText('Заново')
        self.button0.clicked.connect(self.start)
        self.buttonX.clicked.connect(self.start)
        self.steps_of_o.clear()
        self.steps_of_x.clear()
        self.zero = 0
        self.x = 0

    def start(self):
        for i in range(9):
            self.buttons[i].setText('')
            self.buttons[i].setEnabled(True)
        self.button_start.setText('Начать')
        self.steps_of_o.clear()
        self.steps_of_x.clear()
        if self.buttonX.isChecked():
            self.zero = 0
            self.x = 1
        elif self.button0.isChecked():
            self.zero = 1
            self.x = 0
        self.text.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

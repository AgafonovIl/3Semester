import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QLineEdit


class Check(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 120)
        self.setWindowTitle('Морзе')
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.dictionary = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
        }
        y = 0
        x = 0
        for i in range(27):
            if i < 16:
                self.btn = QPushButton('{}'.format(self.alphabet[i]), self)
                self.btn.resize(25, 25)
                self.btn.move(x, y)
                self.btn.clicked.connect(lambda state, num_button=i: self.button_pushed(num_button))
                x += 30
            else:
                if i == 16:
                    x = 0
                    y = 30
                self.btn = QPushButton('{}'.format(self.alphabet[i]), self)
                self.btn.resize(25, 25)
                self.btn.move(x, y)
                self.btn.clicked.connect(lambda state, num_button=i: self.button_pushed(num_button))
                x += 30
        self.name_input = QLineEdit(self)
        self.name_input.resize(475, 25)
        self.name_input.move(0, 60)

    def button_pushed(self, num_button):
        self.name_input.insert(self.dictionary[self.alphabet[num_button].upper()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Check()
    ex.show()
    sys.exit(app.exec_())

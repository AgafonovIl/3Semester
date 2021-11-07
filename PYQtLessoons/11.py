import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 390, 400)
        self.setWindowTitle('Перемешать строки')
        self.btn = QPushButton('Загрузить строки', self)
        self.btn.move(0, 0)
        self.btn.resize(150, 30)
        self.btn.clicked.connect(self.load)
        self.ed = QPlainTextEdit(self)
        self.ed.move(0, 30)
        self.ed.resize(300, 360)

    def load(self):
        with open('lines.txt', encoding='utf-8') as f:
            lines = f.read().split('\n')
            for i in range(0, len(lines), 2):
                self.ed.appendPlainText(lines[i])
            for j in range(1, len(lines), 2):
                self.ed.appendPlainText(lines[j])
            f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

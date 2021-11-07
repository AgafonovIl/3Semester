import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QVBoxLayout, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 370, 300)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.vbox = QVBoxLayout()
        self.ch1 = QCheckBox('Чизбургер', self)
        self.ch2 = QCheckBox('Гамбургер', self)
        self.ch3 = QCheckBox('Кока-кола', self)
        self.ch4 = QCheckBox('Нагетсы', self)

        self.ed = QPlainTextEdit()
        self.btn = QPushButton('Заказать', self)
        self.checkboxes = [self.ch1, self.ch2, self.ch3, self.ch4]

        self.vbox.addWidget(self.ch1)
        self.vbox.addWidget(self.ch2)
        self.vbox.addWidget(self.ch3)
        self.vbox.addWidget(self.ch4)
        self.vbox.addWidget(self.btn)
        self.vbox.addWidget(self.ed)
        self.setLayout(self.vbox)
        self.btn.clicked.connect(self.order)
        self.ed.setEnabled(False)

    def order(self):
        self.ed.clear()
        self.ed.appendPlainText('Ваш заказ:')
        for i in range(len(self.checkboxes)):
            if self.checkboxes[i].isChecked():
                self.ed.appendPlainText(self.checkboxes[i].text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

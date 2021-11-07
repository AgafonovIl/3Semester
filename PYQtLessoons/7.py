import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QLineEdit, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 330)
        self.setWindowTitle('Заказ в Макдональдсе')
        self.menu = ['Чизбургер', 'Гамбургер', 'Кока-кола', 'Нагетсы']
        self.portions = []
        self.checkboxes = []
        x = 10
        y = 0
        for i in range(4):
            self.ch = QCheckBox(self.menu[i], self)
            self.ch.move(x, y)
            self.checkboxes.append(self.ch)
            self.ch.clicked.connect(lambda state, number=i: self.count_of_food(number))
            self.portion = QLineEdit('0', self)
            self.portion.move(x + 90, y)
            self.portion.resize(30, 20)
            self.portion.setEnabled(False)
            self.portions.append(self.portion)
            y += 40

        self.btn = QPushButton('Заказать', self)
        self.btn.move(10, 160)
        self.btn.resize(100, 20)
        self.btn.clicked.connect(self.order)

        self.ed = QPlainTextEdit(self)
        self.ed.setEnabled(False)
        self.ed.move(10, 190)
        self.ed.resize(280, 130)
        self.price = [10, 20, 15, 30]

    def order(self):
        chek = 0
        self.ed.clear()
        self.ed.appendPlainText('Ваш заказ')
        for i in range(len(self.checkboxes)):
            if self.checkboxes[i].isChecked():
                self.ed.appendPlainText(
                    '{}-----{}-----{}'.format(self.checkboxes[i].text(), self.portions[i].text(),
                                              self.price[i] * int(self.portions[i].text())))
            chek += self.price[i] * int(self.portions[i].text())
        self.ed.appendPlainText('Итого: {}'.format(chek))

    def count_of_food(self, number):
        if self.checkboxes[number].isChecked():
            self.portions[number].setEnabled(True)
            self.portions[number].setText('1')
        else:
            self.portions[number].setEnabled(False)
            self.portions[number].setText('0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

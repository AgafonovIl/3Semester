import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtWidgets import QMainWindow, QLineEdit



class Check(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        self.cb1 = QCheckBox('Check_1', self)
        self.cb1.move(20, 20)
        self.cb1.toggle()
        self.cb1.stateChanged.connect(lambda: self.appear_line_edit(self.cb1.isChecked(), self.name_input_1))

        self.cb2 = QCheckBox('Check_2', self)
        self.cb2.move(20, 60)
        self.cb2.toggle()
        self.cb2.stateChanged.connect(lambda: self.appear_line_edit(self.cb2.isChecked(), self.name_input_2))

        self.cb3 = QCheckBox('Check_3', self)
        self.cb3.move(20, 100)
        self.cb3.toggle()
        self.cb3.stateChanged.connect(lambda: self.appear_line_edit(self.cb3.isChecked(), self.name_input_3))

        self.cb4 = QCheckBox('Check_4', self)
        self.cb4.move(20, 140)
        self.cb4.toggle()
        self.cb4.stateChanged.connect(lambda: self.appear_line_edit(self.cb4.isChecked(), self.name_input_4))

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Прятки для виджетов')

        self.name_input_1 = QLineEdit(self)
        self.name_input_1.resize(180, 20)
        self.name_input_1.move(100, 20)

        self.name_input_2 = QLineEdit(self)
        self.name_input_2.resize(180, 20)
        self.name_input_2.move(100, 60)

        self.name_input_3 = QLineEdit(self)
        self.name_input_3.resize(180, 20)
        self.name_input_3.move(100, 100)

        self.name_input_4 = QLineEdit(self)
        self.name_input_4.resize(180, 20)
        self.name_input_4.move(100, 140)



    def appear_line_edit(self, state, linedate):
        if state:
            linedate.show()
        else:
            linedate.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Check()
    ex.show()
    sys.exit(app.exec_())

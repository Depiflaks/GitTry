import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit
from PyQt5.QtWidgets import QWidget, QPushButton, QPlainTextEdit, QComboBox
from PyQt5.QtCore import QRect
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor

import random as r



class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.cur = sqlite3.connect('coffee.sqlite').cursor()
        res = self.cur.execute('''SELECT Название FROM coffee''').fetchall()
        #U = QComboBox

        for i in res:
            self.comboB.addItem(i[0])
        self.b1.clicked.connect(self.GetVal)

    def GetVal(self):
        res = self.cur.execute(f'''SELECT * FROM coffee WHERE Название = '{self.comboB.currentText()}' ''').fetchall()[0]
        self.e1.setText(res[2])
        self.e2.setText(res[3])
        self.pe1.setPlainText(res[4])
        self.e3.setText(str(res[5]))
        self.e4.setText(str(res[6]))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

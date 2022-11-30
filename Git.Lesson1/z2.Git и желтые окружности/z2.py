import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit
from PyQt5.QtWidgets import QWidget, QPushButton, QPlainTextEdit
from PyQt5.QtCore import QRect
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor

import random as r


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCicles(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawCicles(self, qp):
        qp.setBrush(QColor(255, 251, 0))
        qp.setPen(QColor(255, 251, 0))
        for i in range(20):
            D = r.randrange(1, 50)
            Pos = QRect(r.randrange(1, 462), r.randrange(1, 355), D, D)
            qp.drawEllipse(Pos)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit
from PyQt5.QtWidgets import QWidget, QPushButton, QPlainTextEdit
from PyQt5.QtCore import QRect
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import randrange
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(462, 355)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 140, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Жёлтые круги"))
        self.pushButton.setText(_translate("Form", "Рисуй"))


class MainForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            D = randrange(1, 50)
            Col = QColor(randrange(255), randrange(255), randrange(255))
            qp.setBrush(Col)
            qp.setPen(Col)
            Pos = QRect(randrange(1, 462), randrange(1, 355), D, D)
            qp.drawEllipse(Pos)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

from random import randrange as rr
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_for_balls(object):
    def setupUi(self, window_for_balls):
        window_for_balls.setObjectName("window_for_balls")
        window_for_balls.resize(400, 600)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        window_for_balls.setFont(font)
        self.centralwidget = QtWidgets.QWidget(window_for_balls)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 480, 320, 80))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius: 20px;\n"
"    border: 2px solid rgba(255, 255, 255, 255);\n"
"    background-color: rgba(231, 231, 231, 80);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 35px;\n"
"    border: 2px solid rgba(255, 255, 110, 255);\n"
"    background-color: rgba(255, 255, 168, 100);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-radius: 55px;\n"
"    border: 2px solid rgba(255, 255, 90, 255);\n"
"    background-color: rgba(255, 255, 140, 120);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        window_for_balls.setCentralWidget(self.centralwidget)

        self.retranslateUi(window_for_balls)
        QtCore.QMetaObject.connectSlotsByName(window_for_balls)

    def retranslateUi(self, window_for_balls):
        _translate = QtCore.QCoreApplication.translate
        window_for_balls.setWindowTitle(_translate("window_for_balls", "Random Balls?"))
        self.pushButton.setText(_translate("window_for_balls", "Create Random Ball"))


class MyWidget(QtWidgets.QMainWindow, Ui_window_for_balls):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.forbutton)
        self.click = False

    def paintEvent(self, event):
        if self.click:
            self.click = False
            painter = QPainter(self)
            painter.begin(self)
            self.forpaint(painter)
            painter.end()

    def forpaint(self, painter):
        a = QColor(rr(255), rr(255), rr(255))
        painter.setPen(a)
        painter.setBrush(QBrush(a, Qt.SolidPattern))
        a = rr(400)
        painter.drawEllipse(rr(400 - a), rr(400 - a), a, a)

    def forbutton(self):
        self.click = True
        self.repaint()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

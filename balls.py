from random import randrange as rr
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys, traceback


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('balls.ui', self)
        self.pushButton.clicked.connect(self.forbutton)
        self.click = False

    def paintEvent(self, event):
        if self.click:
            self.click = False
            print(0)
            painter = QPainter(self)
            painter.begin(self)
            self.forpaint(painter)
            painter.end()

    def forpaint(self, painter):
        painter.setPen(QColor(255, 255, 0))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        a = rr(400)
        painter.drawEllipse(rr(400 - a), rr(400 - a), a, a)

    def forbutton(self):
        self.click = True
        self.repaint()


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    QMessageBox.critical(None, 'Error', text)
    sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

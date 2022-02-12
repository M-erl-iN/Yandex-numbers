import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from error import log_uncaught_exceptions


sys.excepthook = log_uncaught_exceptions


class Add(QMainWindow):
    def __init__(self, genres, connect, table):
        super().__init__()
        self.table = table
        uic.loadUi('UI/filmadd.ui', self)
        self.con = connect
        for i in genres:
            self.comboBox.addItem(i)
        self.pushButton.clicked.connect(self.add_film)

    def add_film(self):
        try:
            genre = self.comboBox.currentText()
            year = int(self.lineEdit_2.text())
            title = self.lineEdit.text()
            duration = int(self.lineEdit_3.text())
            id = self.con.cursor().execute("""SELECT MAX(id) FROM films""").fetchone()[0] + 1
            list_ = (id, title, year, genre, duration)
            self.con.cursor().execute("""INSERT INTO films (id, title, year, genre, duration) VALUES (?, ?, ?, ?, ?)""", list_)
            self.con.commit()
            self.table.setRowCount(self.tableWidget.rowCount() + 1)
            couns = self.table.rowCount(self.tableWidget.rowCount() + 1)
            for i in range(5):
                self.tableWidget.setItem(i, couns, QTableWidgetItem(str(list_[i])))
        except BaseException:
            pass

    def closeEvent(self, event):
        pass


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/films2.ui', self)
        self.connection = sqlite3.connect("data/films_db.sqlite")
        self.pushButton.clicked.connect(self.new_film)
        self.genres = self.connection.cursor().execute("""SELECT * from genres""").fetchall()
        self.t = """SELECT * FROM films"""
        self.select_data()

    def select_data(self):
        res = self.connection.cursor().execute(self.t).fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def new_film(self):
        genres = [i[1] for i in self.genres]
        self.addfilmapp = QApplication(sys.argv)
        self.exFilm = Add(genres, self.connection, self.tableWidget)
        self.exFilm.show()

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())

import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        super().__init__()
        uic.loadUi('main.ui', self)

        self.table = self.tableWidget
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            'id',
            'type',
            'roast_degree',
            'ground_grains',
            'taste',
            'price',
            'volume'
        ])

        self.pushButton.clicked.connect(self.get_note)

    def get_note(self):
        id = self.lineEdit.text()
        type = self.lineEdit_2.text()
        roast_degree = self.lineEdit_3.text()
        ground_grains = self.lineEdit_4.text()
        taste = self.lineEdit_6.text()
        price = self.lineEdit_7.text()
        volume = self.lineEdit_5.text()

        con = sqlite3.connect('coffee')
        cur = con.cursor()

        result = cur.execute('''SELECT coffee.id, coffee.type, roast_degree.roast_type, ground_grains.ground_grains, taste.taste, coffee.price, coffee.volume
        FROM coffee
        INNER JOIN roast_degree on coffee.roast_degree = roast_degree.id
        INNER JOIN ground_grains on coffee.ground_grains = ground_grains.id
        INNER JOIN taste on coffee.taste = taste.id
        WHERE coffee.id = ? OR coffee.type = ? OR roast_degree.roast_type = ? OR ground_grains.ground_grains = ? OR taste.taste = ? OR coffee.price = ? OR coffee.volume = ?
        ''', (id, type, roast_degree, ground_grains, taste, price, volume)).fetchall()

        print(result)

        self.table.setRowCount(len(result))

        for i in range(len(result)):
            for j in range(7):
                self.table.setItem(i, j, QTableWidgetItem(str(result[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee = MainWindow()
    coffee.show()
    sys.exit(app.exec_())

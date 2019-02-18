# coding:utf8

from PyQt5 import QtWidgets
from class_mainwindow import MainWindow
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

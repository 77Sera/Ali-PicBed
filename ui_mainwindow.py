# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/project/oss-uploader/ui/ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 519)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        self.btn_upload_file = QtWidgets.QPushButton(MainWindow)
        self.btn_upload_file.setGeometry(QtCore.QRect(280, 190, 93, 28))
        self.btn_upload_file.setObjectName("btn_upload_file")
        self.text_url = QtWidgets.QLineEdit(MainWindow)
        self.text_url.setGeometry(QtCore.QRect(70, 310, 451, 31))
        self.text_url.setObjectName("text_url")
        self.btn_copy_url = QtWidgets.QPushButton(MainWindow)
        self.btn_copy_url.setGeometry(QtCore.QRect(530, 310, 51, 31))
        self.btn_copy_url.setObjectName("btn_copy_url")
        self.btn_copy_url_md = QtWidgets.QPushButton(MainWindow)
        self.btn_copy_url_md.setGeometry(QtCore.QRect(590, 310, 51, 31))
        self.btn_copy_url_md.setObjectName("btn_copy_url_md")
        self.label_upload_status = QtWidgets.QLabel(MainWindow)
        self.label_upload_status.setGeometry(QtCore.QRect(410, 190, 101, 31))
        self.label_upload_status.setObjectName("label_upload_status")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ali - Picbed"))
        self.btn_upload_file.setText(_translate("MainWindow", "上传"))
        self.btn_copy_url.setText(_translate("MainWindow", "Copy"))
        self.btn_copy_url_md.setText(_translate("MainWindow", "MD"))
        self.label_upload_status.setText(_translate("MainWindow", "上传进度显示"))


# coding:utf8

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from ui_mainwindow import Ui_MainWindow
from oss_manager import OssManager
from my_utils import *
from pyperclip import copy


class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.label_upload_status.setText("")

        self.om = self.load_om(config_file="default.config")  # 载入OssManager类

        # 按钮 btn_upload_file 绑定 upload_file 函数
        self.btn_upload_file.clicked.connect(self.upload_file)
        # 按钮 btn_copy_url 绑定 copy_url 函数
        self.btn_copy_url.clicked.connect(self.copy_url)
        # 按钮 btn_copy_url_md 绑定 copy_url_md 函数
        self.btn_copy_url_md.clicked.connect(self.copy_url_md)

    def copy_url(self):
        '''
        获取LineEdit中的文本并复制到剪贴板
        '''
        text = self.text_url.text()
        copy(text)

    def copy_url_md(self):
        '''
        获取LineEdit中的文本并以markdown格式复制到剪贴板
        '''
        text = "![]({0})".format(self.text_url.text())
        copy(text)

    def upload_file(self):

        file_path = self.select_file()  # 获取要上传的文件名

        if file_path:
            self.label_upload_status.setText("上传中...")
            try:
                target_path = self.om.upload_file(file_path)
                self.text_url.setText(target_path)
                self.label_upload_status.setText("上传成功!")
            except Exception as e:
                QMessageBox.warning(self,
                                    "ERROR",
                                    "\n\t\tUpload Failed!\t\n\n\tPlease Check Your Config and Run again.\t\t\n\n",
                                    QMessageBox.StandardButtons(QMessageBox.Close))
                self.label_upload_status.setText("")
                print_error(e, other_string="[!] Upload Failed - {}".format(file_path))

    def select_file(self):
        file_path = QFileDialog.getOpenFileName(self, '选择文件')[0]
        return file_path

    def load_om(self, config_file):
        configs = load_config(config_file)

        return OssManager(
            endpoint=configs["endpoint"],
            bucket_domain_name=configs["bucket_domain_name"],
            bucket_name=configs["bucket_name"],
            accesskey_id=configs["accesskey_id"],
            accesskey_secret=configs["accesskey_secret"]
        )
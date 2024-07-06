from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog
from app.mdui import Ui_Dialog
from app.peodialog import PeoDialog
from app.cardialog import CarDialog
import cv2 as cv
from app.video import Video


class MainDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel(self)
        self.setCentralWidget(self.label)
        self.pixmap = QtGui.QPixmap("data/bg.png")
        # 设置QLabel的尺寸
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        # 将背景图片设置为QLabel的内容
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        # self.gate_text = "东"
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #创建成员：两个线程th_1, th_2
        self.th1 = Video('data/vd1.mp4')
        self.th1.send.connect(self.showimg)     # 绑定信号与槽函数
        self.th1.start()

        self.th2 = Video('data/vd2.mp4')
        self.th2.send.connect(self.showimg)     # 绑定信号与槽函数
        self.th2.start()

    def showimg(self, h, w, c, b, th_id):
        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        if th_id == 1:
            # 自动缩放
            width = self.ui.video1.width()
            height = self.ui.video1.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.video1.setPixmap(scale_pix)
        if th_id == 2:
            # 自动缩放
            width = self.ui.video2.width()
            height = self.ui.video2.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.video2.setPixmap(scale_pix)

    #界面跳转
    def car_goin(self):
        self.carFrame = CarDialog()
        #北门 信号发送者是northcar
        if self.sender() == self.ui.northcar:
            self.gate_text = "北"
            self.carFrame.ui.title1.setText(self.gate_text)
            self.carFrame.th1.start()
        #东门 信号发送者是eastcar
        if self.sender() == self.ui.eastcar:
            self.gate_text = "东"
            self.carFrame.ui.title1.setText(self.gate_text)
            self.carFrame.th2.start()

        self.carFrame.show()
        self.close()

    def peo_goin(self):
        self.peoFrame =PeoDialog()
        #北门 信号发送者是northcar
        if self.sender() == self.ui.northpeo:
            self.gate_text = "北"
            self.peoFrame.ui.title1.setText(self.gate_text)
            self.peoFrame.th1.start()
        #东门 信号发送者是eastcar
        if self.sender() == self.ui.eastpeo:
            self.gate_text = "东"
            self.peoFrame.ui.title1.setText(self.gate_text)
            self.peoFrame.th2.start()

        self.peoFrame.show()
        self.close()



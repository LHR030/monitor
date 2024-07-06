from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog

from app.peoui import Ui_Dialog
from app.video_people import Video


class PeoDialog(QtWidgets.QMainWindow):
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
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.th1 = Video('data/vd1.mp4')
        # 绑定信号与槽函数
        self.th1.send.connect(self.showimg)
        self.th2 = Video('data/vd2.mp4')
        # 绑定信号与槽函数
        self.th2.send.connect(self.showimg)

    #视频帧显示
    def showimg(self, h, w, c, b, th_id,num):
        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        #自动缩放
        width = self.ui.video.width()
        height = self.ui.video.height()
        scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
        self.ui.video.setPixmap(scale_pix)
        self.ui.number.setText(str(num))

    #返回上一级界面
    # def return_last(self):
    #     #延迟导入
    #     from app.gatedialog import GateDialog
    #     self.gateFrame = GateDialog()
    #     #这是哪个校门的监控
    #     self.gateFrame.ui.title1.setText(self.gateFrame.gtext)
    #     # 北门
    #     if self.gateFrame.gtext == "北":
    #         #北门视频
    #         self.gateFrame.th1.start()
    #     # 东门
    #     if self.gateFrame.gtext == "东":
    #         #东门视频
    #         self.gateFrame.th2.start()
    #
    #     self.gateFrame.show()
    #     self.close()

    #返回主界面
    def return_home(self):
        # 延迟导入
        from app.maindialog import MainDialog
        self.mainFrame = MainDialog()
        self.mainFrame.show()
        self.close()
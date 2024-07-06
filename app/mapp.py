from PyQt5.QtWidgets import QApplication
from app.maindialog import MainDialog
# from app.gatedialog import GateDialog
# from app.cardialog import CarDialog
# from app.peodialog import PeoDialog
import sys
#如何将界面和想要实现的功能结合起来
#构建子类，在类的内部操作程序和其关联的按钮
class MApp(QApplication):
    def __init__(self):
        super(MApp, self).__init__(sys.argv)
        self.md = MainDialog()
        self.md.show()
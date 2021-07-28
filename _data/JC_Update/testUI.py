__author__ = 'Rong_kang_Xiong'
import sys
import os
sys.path.append(os.path.join(os.getcwd(), "JClib"))  #添加lib
sys.path.append(os.path.join(os.getcwd(), "QtUI"))  #添加UI的路径

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from JCGUI import *
from mainButton import mainButton



if __name__== '__main__':
    pwd = os.getcwd()
    yamlpath = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "meeting_info.yml")
    print("当前路径 = "+pwd)
    print("上级路径 = "+yamlpath)
    #openurl("www.baidu.com")

    app = QApplication(sys.argv)
    MainWindow = mainButton()
    MainWindow.setWindowIcon(QIcon(os.path.join(pwd, "image", "icon", "wenlab.png")))  #添加窗口图标

    MainWindow.show()
    sys.exit(app.exec_())




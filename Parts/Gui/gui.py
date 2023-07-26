import typing
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

from PyQt5.QtWidgets import QWidget

class guiStock(QMainWindow):
    def __init__(self):
        super(guiStock,self).__init__()
        self.setGeometry(0,0,1000,1000)
        self.setWindowTitle("Strategy Analysis")
        self.setWindowIcon(QIcon('strategies/stockicon.png'))
        # self.startGui()
    # def startGui(self):
        

def gui():
    window = QApplication(sys.argv)
    startWindow = guiStock()
    
    startWindow.show()
    sys.exit(window.exec())
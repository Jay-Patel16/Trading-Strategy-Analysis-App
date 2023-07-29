# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RSIGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ScalpingWin import *
from TrendWin import *
from GRWin import *
from gui import *
from RSI import *
from general import *

class Ui_RSIWin(object):
    def openRSI(self):
        RSIWin.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RSIWin()
        self.ui.setupUi(self.window)
        self.window.show()
    def openTrend(self):
        RSIWin.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TrendWin()
        self.ui.setupUi(self.window)
        self.window.show()
    def openScalping(self):
        RSIWin.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ScalpingWin()
        self.ui.setupUi(self.window)
        self.window.show()
    def openGeneral(self):
        RSIWin.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GRWin()
        self.ui.setupUi(self.window)
        self.window.show()
    def openHome(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        RSIWin.close()
    def setupUi(self, RSIWin):
        RSIWin.setObjectName("RSIWin")
        RSIWin.resize(900, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsi-trading-indicator-icon-with-a-phone-vector-41137647.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RSIWin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(RSIWin)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 300, 81, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 80, 671, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 40, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(640, 170, 101, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 300, 113, 22))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(470, 170, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 170, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(990, 260, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 170, 111, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(760, 170, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label.setFont(font)
        self.label.setObjectName("label")
        RSIWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RSIWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuRSI_Indexing = QtWidgets.QMenu(self.menubar)
        self.menuRSI_Indexing.setObjectName("menuRSI_Indexing")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        RSIWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RSIWin)
        self.statusbar.setObjectName("statusbar")
        RSIWin.setStatusBar(self.statusbar)
        self.actionScalping = QtWidgets.QAction(RSIWin)
        self.actionScalping.setObjectName("actionScalping")
        self.actionScalping.triggered.connect(self.openScalping)
        self.actionTrend_Following = QtWidgets.QAction(RSIWin)
        self.actionTrend_Following.setObjectName("actionTrend_Following")
        self.actionTrend_Following.triggered.connect(self.openTrend)
        self.actionGeneral_Recommendation = QtWidgets.QAction(RSIWin)
        self.actionGeneral_Recommendation.setObjectName("actionGeneral_Recommendation")
        self.actionGeneral_Recommendation.triggered.connect(self.openGeneral)
        self.actionRSI_Indexing = QtWidgets.QAction(RSIWin)
        self.actionRSI_Indexing.setObjectName("actionRSI_Indexing")
        self.actionRSI_Indexing.triggered.connect(self.openRSI)
        self.actionHome = QtWidgets.QAction(RSIWin)
        self.actionHome.setObjectName("actionHome")
        self.actionHome.triggered.connect(self.openHome)
        self.menuRSI_Indexing.addAction(self.actionScalping)
        self.menuRSI_Indexing.addAction(self.actionTrend_Following)
        self.menuRSI_Indexing.addAction(self.actionRSI_Indexing)
        self.menuHome.addAction(self.actionGeneral_Recommendation)
        self.menuHome.addAction(self.actionHome)
        self.menubar.addAction(self.menuRSI_Indexing.menuAction())
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(RSIWin)
        QtCore.QMetaObject.connectSlotsByName(RSIWin)

    def retranslateUi(self, RSIWin):
        _translate = QtCore.QCoreApplication.translate
        RSIWin.setWindowTitle(_translate("RSIWin", "RSI Indexing"))
        self.label_3.setText(_translate("RSIWin", "Win Rate"))
        self.label_5.setText(_translate("RSIWin", "RSI Indexing is an idea of using moving average and RSI calculations over \n"
"200 days to decide on if a stock is on an upward or downward trend. \n"
"Leading to an entry or exit of market"))
        self.label_4.setText(_translate("RSIWin", "RSI Indexing"))
        self.label_8.setText(_translate("RSIWin", "End Date"))
        self.lineEdit_3.setPlaceholderText(_translate("RSIWin", "0%"))
        self.pushButton.setText(_translate("RSIWin", "Submit"))
        self.pushButton.clicked.connect(self.RSIOutput)
        self.lineEdit_4.setPlaceholderText(_translate("RSIWin", "5"))
        self.label_7.setText(_translate("RSIWin", "Start Date"))
        self.label.setText(_translate("RSIWin", "Stock Tag"))
        self.menuRSI_Indexing.setTitle(_translate("RSIWin", "Strategies"))
        self.menuHome.setTitle(_translate("RSIWin", "Others"))
        self.actionScalping.setText(_translate("RSIWin", "Scalping"))
        self.actionTrend_Following.setText(_translate("RSIWin", "Trend Following"))
        self.actionGeneral_Recommendation.setText(_translate("RSIWin", "General Recommendation"))
        self.actionRSI_Indexing.setText(_translate("RSIWin", "RSI Indexing"))
        self.actionHome.setText(_translate("RSIWin", "Home"))
    
    def RSIOutput(self):
        stock = self.lineEdit.text()
        startDate = self.dateEdit_2.text()
        endDate = self.dateEdit.text()
        startD, endD = convertDate(startDate,endDate)
        dataRSI = RSI(stock,startD,endD)
        buy,sell = getSignals(dataRSI)
        profitsRSI = profits(buy,sell,dataRSI)
        winRate = getWinRate(profitsRSI)
        self.lineEdit_3.setText(str(winRate) + "%")
        graphRSI(dataRSI,buy,sell)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RSIWin = QtWidgets.QMainWindow()
    ui = Ui_RSIWin()
    ui.setupUi(RSIWin)
    RSIWin.show()
    sys.exit(app.exec_())

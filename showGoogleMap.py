# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'showGoogleMapgBbNPK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 90, 561, 471))
        self.lineEditLongitude = QLineEdit(self.centralwidget)
        self.lineEditLongitude.setObjectName(u"lineEditLongitude")
        self.lineEditLongitude.setGeometry(QRect(50, 10, 421, 20))
        self.lineEditLatitude = QLineEdit(self.centralwidget)
        self.lineEditLatitude.setObjectName(u"lineEditLatitude")
        self.lineEditLatitude.setGeometry(QRect(50, 50, 421, 20))
        self.pushButtonShowMap = QPushButton(self.centralwidget)
        self.pushButtonShowMap.setObjectName(u"pushButtonShowMap")
        self.pushButtonShowMap.setGeometry(QRect(510, 10, 111, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEditLongitude.setPlaceholderText(QCoreApplication.translate("MainWindow", u"longi", None))
        self.lineEditLatitude.setPlaceholderText(QCoreApplication.translate("MainWindow", u"lati", None))
        self.pushButtonShowMap.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


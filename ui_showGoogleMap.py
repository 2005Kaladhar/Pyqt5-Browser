# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'showGoogleMapgtGiPb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(791, 574)
        self.lineEditLatitude = QLineEdit(Dialog)
        self.lineEditLatitude.setObjectName(u"lineEditLatitude")
        self.lineEditLatitude.setGeometry(QRect(90, 50, 421, 20))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 90, 561, 471))
        self.pushButtonShowMap = QPushButton(Dialog)
        self.pushButtonShowMap.setObjectName(u"pushButtonShowMap")
        self.pushButtonShowMap.setGeometry(QRect(550, 10, 111, 41))
        self.lineEditLongitude = QLineEdit(Dialog)
        self.lineEditLongitude.setObjectName(u"lineEditLongitude")
        self.lineEditLongitude.setGeometry(QRect(90, 10, 421, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEditLatitude.setPlaceholderText(QCoreApplication.translate("Dialog", u"lati", None))
        self.pushButtonShowMap.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.lineEditLongitude.setPlaceholderText(QCoreApplication.translate("Dialog", u"longi", None))
    # retranslateUi


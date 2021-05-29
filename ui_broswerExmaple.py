# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'broswerExmaplesKRbED.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.url_box = QLineEdit(self.frame)
        self.url_box.setObjectName(u"url_box")
        self.url_box.setMinimumSize(QSize(0, 33))
        font = QFont()
        font.setPointSize(14)
        self.url_box.setFont(font)
        self.url_box.setStyleSheet(u"QLineEdit{\n"
"	border-radius:7px;\n"
"color: rgb(225, 225, 225);\n"
"	background-color: rgb(76, 76, 76);\n"
"	border-style:inset;\n"
"border-width:1px;\n"
"  \n"
"	border-color: rgb(76, 76, 76);\n"
"	border-bottom-color: rgb(186, 62, 0);\n"
"border-right-color: rgb(231, 91, 22);\n"
"\n"
"}\n"
"QLineEdit::hover{\n"
"	border-bottom-color:rgb(140, 67, 16);\n"
"border-right-color: rgb(140, 67, 16);\n"
"	background-color: rgba(76, 76, 76,200);\n"
"\n"
"	\n"
"\n"
"}")
        self.url_box.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.url_box)

        self.search_button = QPushButton(self.frame)
        self.search_button.setObjectName(u"search_button")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setMinimumSize(QSize(90, 90))
        font1 = QFont()
        font1.setFamily(u"Sitka Small")
        font1.setPointSize(9)
        font1.setUnderline(False)
        self.search_button.setFont(font1)
        self.search_button.setStyleSheet(u"QPushButton{\n"
"	border-radius:45px;\n"
"color: rgb(225, 225, 225);\n"
"	background-color: rgb(76, 76, 76);\n"
"	border-style:inset;\n"
"border-width:1px;\n"
"  \n"
"	border-color: rgb(76, 76, 76);\n"
"	border-bottom-color: rgb(186, 62, 0);\n"
"border-right-color: rgb(231, 91, 22);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	border-bottom-color:rgb(140, 67, 16);\n"
"	border-right-color: rgb(65, 195, 95);\n"
"\n"
"	background-color: rgb(56, 56, 56);\n"
"\n"
"	\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.search_button)


        self.verticalLayout.addWidget(self.frame)

        self.browserWidget = QWebEngineView(self.centralwidget)
        self.browserWidget.setObjectName(u"browserWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.browserWidget.sizePolicy().hasHeightForWidth())
        self.browserWidget.setSizePolicy(sizePolicy1)
        self.browserWidget.setStyleSheet(u"background-color: rgba(0, 0, 0, 200);")

        self.verticalLayout.addWidget(self.browserWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.url_box.setText("")
        self.url_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter URL", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi


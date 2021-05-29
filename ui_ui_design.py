# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_design - CopyzsefIg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(644, 598)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BaseFrame = QFrame(self.centralwidget)
        self.BaseFrame.setObjectName(u"BaseFrame")
        self.BaseFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.BaseFrame.setFrameShape(QFrame.StyledPanel)
        self.BaseFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.BaseFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TitleBar_2 = QFrame(self.BaseFrame)
        self.TitleBar_2.setObjectName(u"TitleBar_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar_2.sizePolicy().hasHeightForWidth())
        self.TitleBar_2.setSizePolicy(sizePolicy)
        self.TitleBar_2.setMinimumSize(QSize(0, 0))
        self.TitleBar_2.setMaximumSize(QSize(16777215, 30))
        self.TitleBar_2.setStyleSheet(u"QFrame{\n"
"\n"
"	border-image:none;\n"
"border-radius:2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 165), stop:1 rgba(0, 0, 0, 165));\n"
"\n"
"}")
        self.TitleBar_2.setFrameShape(QFrame.StyledPanel)
        self.TitleBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.TitleBar_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.util_buttons = QFrame(self.TitleBar_2)
        self.util_buttons.setObjectName(u"util_buttons")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.util_buttons.sizePolicy().hasHeightForWidth())
        self.util_buttons.setSizePolicy(sizePolicy1)
        self.util_buttons.setMinimumSize(QSize(0, 25))
        self.util_buttons.setMaximumSize(QSize(100, 16777215))
        self.util_buttons.setStyleSheet(u"border-image:none;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.util_buttons.setFrameShape(QFrame.StyledPanel)
        self.util_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.util_buttons)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 34, 3)
        self.Minimizebtn = QPushButton(self.util_buttons)
        self.Minimizebtn.setObjectName(u"Minimizebtn")
        sizePolicy1.setHeightForWidth(self.Minimizebtn.sizePolicy().hasHeightForWidth())
        self.Minimizebtn.setSizePolicy(sizePolicy1)
        self.Minimizebtn.setMaximumSize(QSize(14, 14))
        self.Minimizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Minimizebtn)

        self.Maximizebtn = QPushButton(self.util_buttons)
        self.Maximizebtn.setObjectName(u"Maximizebtn")
        sizePolicy1.setHeightForWidth(self.Maximizebtn.sizePolicy().hasHeightForWidth())
        self.Maximizebtn.setSizePolicy(sizePolicy1)
        self.Maximizebtn.setMaximumSize(QSize(14, 14))
        self.Maximizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(85, 170, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Maximizebtn)

        self.CloseButton = QPushButton(self.util_buttons)
        self.CloseButton.setObjectName(u"CloseButton")
        sizePolicy1.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy1)
        self.CloseButton.setMaximumSize(QSize(14, 14))
        self.CloseButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 0, 16);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.CloseButton)


        self.horizontalLayout_2.addWidget(self.util_buttons)

        self.spacerFrame = QFrame(self.TitleBar_2)
        self.spacerFrame.setObjectName(u"spacerFrame")
        self.spacerFrame.setCursor(QCursor(Qt.SizeAllCursor))
        self.spacerFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.spacerFrame.setFrameShape(QFrame.StyledPanel)
        self.spacerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.spacerFrame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.upper_drag = QFrame(self.spacerFrame)
        self.upper_drag.setObjectName(u"upper_drag")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.upper_drag.sizePolicy().hasHeightForWidth())
        self.upper_drag.setSizePolicy(sizePolicy2)
        self.upper_drag.setCursor(QCursor(Qt.SizeAllCursor))
        self.upper_drag.setFrameShape(QFrame.StyledPanel)
        self.upper_drag.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.upper_drag)

        self.SizeGrip_upper_right = QFrame(self.spacerFrame)
        self.SizeGrip_upper_right.setObjectName(u"SizeGrip_upper_right")
        sizePolicy.setHeightForWidth(self.SizeGrip_upper_right.sizePolicy().hasHeightForWidth())
        self.SizeGrip_upper_right.setSizePolicy(sizePolicy)
        self.SizeGrip_upper_right.setMinimumSize(QSize(16, 25))
        self.SizeGrip_upper_right.setCursor(QCursor(Qt.ArrowCursor))
        self.SizeGrip_upper_right.setStyleSheet(u"background-color: rgba(43, 43, 43,10);\n"
"")
        self.SizeGrip_upper_right.setFrameShape(QFrame.StyledPanel)
        self.SizeGrip_upper_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.SizeGrip_upper_right)


        self.horizontalLayout_2.addWidget(self.spacerFrame)


        self.verticalLayout.addWidget(self.TitleBar_2)

        self.stackedWidget = QStackedWidget(self.BaseFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.Page1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.horizontalLayout_5 = QHBoxLayout(self.Page1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Page1_BaseFrae = QFrame(self.Page1)
        self.Page1_BaseFrae.setObjectName(u"Page1_BaseFrae")
        self.Page1_BaseFrae.setStyleSheet(u"background-color: rgb(255, 170, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"background-color: rgb(32, 32, 30);\n"
"\n"
"background-color: rgb(29, 29, 29);")
        self.Page1_BaseFrae.setFrameShape(QFrame.StyledPanel)
        self.Page1_BaseFrae.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Page1_BaseFrae)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 6)
        self.frame_7 = QFrame(self.Page1_BaseFrae)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(89, 47))
        self.frame_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_7, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.Page1_BaseFrae)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(299, 254))
        self.frame_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, 8, 9)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.Box_name = QLineEdit(self.frame_4)
        self.Box_name.setObjectName(u"Box_name")
        self.Box_name.setMinimumSize(QSize(266, 54))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Box_name.setFont(font)
        self.Box_name.setTabletTracking(True)
        self.Box_name.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 115));\n"
"border-radius:11px;\n"
"margin-top:20px;\n"
"text-align:left;\n"
"\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:0.301136, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(27, 109, 0, 135));\n"
"background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 72));\n"
"color: rgb(241, 241, 241);\n"
"}\n"
"")
        self.Box_name.setAlignment(Qt.AlignCenter)
        self.Box_name.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.Box_name, 0, 0, 1, 1)

        self.Box_email = QLineEdit(self.frame_4)
        self.Box_email.setObjectName(u"Box_email")
        self.Box_email.setMinimumSize(QSize(266, 54))
        self.Box_email.setFont(font)
        self.Box_email.setTabletTracking(True)
        self.Box_email.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 115));\n"
"border-radius:11px;\n"
"margin-top:20px;\n"
"text-align:left;\n"
"\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:0.301136, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(27, 109, 0, 135));\n"
"background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 72));\n"
"color: rgb(241, 241, 241);\n"
"}\n"
"")
        self.Box_email.setAlignment(Qt.AlignCenter)
        self.Box_email.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.Box_email, 1, 0, 1, 1)

        self.Box_password = QLineEdit(self.frame_4)
        self.Box_password.setObjectName(u"Box_password")
        self.Box_password.setMinimumSize(QSize(266, 54))
        self.Box_password.setFont(font)
        self.Box_password.setTabletTracking(True)
        self.Box_password.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 115));\n"
"border-radius:11px;\n"
"margin-top:20px;\n"
"text-align:left;\n"
"\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.574, y1:0.301136, x2:0.5, y2:1, stop:0 rgba(0, 93, 21, 0), stop:1 rgba(27, 109, 0, 135));\n"
"background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 72));\n"
"color: rgb(241, 241, 241);\n"
"}\n"
"")
        self.Box_password.setEchoMode(QLineEdit.Password)
        self.Box_password.setAlignment(Qt.AlignCenter)
        self.Box_password.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.Box_password, 2, 0, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 3)

        self.LoginButton = QPushButton(self.Page1_BaseFrae)
        self.LoginButton.setObjectName(u"LoginButton")
        sizePolicy1.setHeightForWidth(self.LoginButton.sizePolicy().hasHeightForWidth())
        self.LoginButton.setSizePolicy(sizePolicy1)
        self.LoginButton.setMinimumSize(QSize(109, 47))
        font1 = QFont()
        font1.setFamily(u"MV Boli")
        font1.setPointSize(14)
        self.LoginButton.setFont(font1)
        self.LoginButton.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"color: rgba(232, 0, 0, 250);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	\n"
"\n"
"border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	alternate-background-color: rgb(0, 0, 0);\n"
"\n"
"border-top-width:10px;\n"
"border-width:1px;\n"
"border-style:  outset;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(48, 48, 48);\n"
"	border-color: rgba(165, 0, 0, 200);\n"
"color: rgba(232, 0, 0, 180);\n"
"	border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.LoginButton, 2, 1, 1, 1)

        self.frame_8 = QFrame(self.Page1_BaseFrae)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(89, 47))
        self.frame_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_8, 2, 2, 1, 1)

        self.frame_2 = QFrame(self.Page1_BaseFrae)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(299, 240))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 17)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(304, 244))
        self.frame_6.setStyleSheet(u"border-image: url(:/newPrefix/ThunderBolt Logo flipped.png);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_6)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 3)


        self.horizontalLayout_8.addLayout(self.gridLayout_2)


        self.horizontalLayout_5.addWidget(self.Page1_BaseFrae)

        self.stackedWidget.addWidget(self.Page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_9 = QHBoxLayout(self.page_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.page2BaseFrame = QFrame(self.page_2)
        self.page2BaseFrame.setObjectName(u"page2BaseFrame")
        self.page2BaseFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.page2BaseFrame.setFrameShape(QFrame.StyledPanel)
        self.page2BaseFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.page2BaseFrame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.page2BaseFrame)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftMenuFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuFrame.setSizePolicy(sizePolicy3)
        self.leftMenuFrame.setMaximumSize(QSize(32, 16777215))
        self.leftMenuFrame.setStyleSheet(u"QFame {\n"
"	border-image: url(:/newPrefix/leftmenu.jpg);\n"
"	background-color: rgb(29, 29, 29);\n"
"border-radius:5px;\n"
"	background-image: url(:/newPrefix/MenuBgm.jfif);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"background-image: url(:/newPrefix/leftmenu.jpg);\n"
"\n"
"}\n"
"")
        self.leftMenuFrame.setFrameShape(QFrame.StyledPanel)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 1)
        self.frame = QFrame(self.leftMenuFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, -1)
        self.Men_button = QPushButton(self.frame)
        self.Men_button.setObjectName(u"Men_button")
        sizePolicy.setHeightForWidth(self.Men_button.sizePolicy().hasHeightForWidth())
        self.Men_button.setSizePolicy(sizePolicy)
        self.Men_button.setMinimumSize(QSize(0, 41))
        font2 = QFont()
        font2.setFamily(u"MS Reference Sans Serif")
        font2.setPointSize(14)
        self.Men_button.setFont(font2)
        self.Men_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(39, 0, 58);\n"
"    border-radius:7px;\n"
"	border-width:1px;\n"
"	border-style:Inset;\n"
"	background-image: url(:/newPrefix/user2.png);\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(163, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(85, 85, 85);\n"
"	background-image: url(:/newPrefix/user2.png);\n"
"	border-width:2px;\n"
"	border-style:Inset;\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(0, 255, 0);\n"
"}")

        self.horizontalLayout_12.addWidget(self.Men_button, 0, Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.frame)

        self.Account = QFrame(self.leftMenuFrame)
        self.Account.setObjectName(u"Account")
        self.Account.setStyleSheet(u"QFrame{\n"
"\n"
"background-color: rgb(200, 142, 27);\n"
"\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"")
        self.Account.setFrameShape(QFrame.StyledPanel)
        self.Account.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Account)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 0, 3, 3)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(13)
        self.Account_button = QPushButton(self.Account)
        self.Account_button.setObjectName(u"Account_button")
        sizePolicy1.setHeightForWidth(self.Account_button.sizePolicy().hasHeightForWidth())
        self.Account_button.setSizePolicy(sizePolicy1)
        self.Account_button.setMinimumSize(QSize(129, 33))
        font3 = QFont()
        font3.setFamily(u"MS Reference Sans Serif")
        font3.setPointSize(11)
        self.Account_button.setFont(font3)
        self.Account_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(29, 29, 29);\n"
"	border-radius:7px;\n"
"	padding-left:20px;\n"
"	border-width:1px;\n"
"	border-style:Inset;\n"
"\n"
"	\n"
"	background-image: url(:/newPrefix/cil-location-pin.png);\n"
"	background-repeat:none;\n"
"	background-position:left;\n"
"	\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(163, 0, 0);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(85, 170, 255);\n"
"	background-image: url(:/newPrefix/resources/icons/cil-user.png);\n"
"	background-repeat:none;\n"
"	background-position:left;\n"
"	border-width:1px;\n"
"	border-style:Inset;\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(0, 255, 0);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.Account_button, 3, 0, 1, 1)

        self.Home_button = QPushButton(self.Account)
        self.Home_button.setObjectName(u"Home_button")
        sizePolicy1.setHeightForWidth(self.Home_button.sizePolicy().hasHeightForWidth())
        self.Home_button.setSizePolicy(sizePolicy1)
        self.Home_button.setMinimumSize(QSize(129, 33))
        self.Home_button.setFont(font3)
        self.Home_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(29, 29, 29);\n"
"border-radius:7px;\n"
"	padding-left:20px;\n"
"	border-width:1px;\n"
"	border-style:Inset;\n"
"	background-image: url(:/newPrefix/cil-home.png);\n"
"	background-repeat:none;\n"
"	background-position:left;\n"
"	\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(163, 0, 0);\n"
"/* This is a commentl*/\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-width:1px;\n"
"	border-style:Inset;\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(0, 255, 0);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.Home_button, 1, 0, 1, 1)

        self.Contact_button = QPushButton(self.Account)
        self.Contact_button.setObjectName(u"Contact_button")
        sizePolicy1.setHeightForWidth(self.Contact_button.sizePolicy().hasHeightForWidth())
        self.Contact_button.setSizePolicy(sizePolicy1)
        self.Contact_button.setMinimumSize(QSize(129, 33))
        self.Contact_button.setFont(font3)
        self.Contact_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(29, 29, 29);\n"
"border-radius:7px;\n"
"	padding-left:20px;\n"
"	border-width:1px;\n"
"	border-style:Inset;\n"
"	background-image: url(:/newPrefix/cil-envelope-closed.png);\n"
"	background-repeat:none;\n"
"	background-position:left;\n"
"	\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(163, 0, 0);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-width:1px;\n"
"	border-style:Inset;\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(0, 255, 0);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.Contact_button, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout_4.addWidget(self.Account)

        self.frame_3 = QFrame(self.leftMenuFrame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(2, -1, 0, 0)
        self.search_progress = QProgressBar(self.frame_3)
        self.search_progress.setObjectName(u"search_progress")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.search_progress.sizePolicy().hasHeightForWidth())
        self.search_progress.setSizePolicy(sizePolicy5)
        self.search_progress.setMaximumSize(QSize(24, 16777215))
        self.search_progress.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	color: rgb(250, 250, 250);\n"
"text-align:top;\n"
"padding-top:5px;\n"
"border-style:inset;\n"
"border-width:1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	border-bottom-color: rgb(255, 85, 0);\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"margin:8px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.534, y1:0, x2:0.551, y2:0.369409, stop:0 rgba(146, 74, 0, 126), stop:1 rgba(255, 129, 0, 219));\n"
"border-radius:3px;\n"
"\n"
"}")
        self.search_progress.setValue(100)
        self.search_progress.setAlignment(Qt.AlignCenter)
        self.search_progress.setOrientation(Qt.Vertical)
        self.search_progress.setInvertedAppearance(False)
        self.search_progress.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_21.addWidget(self.search_progress)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.leftMenuFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(3, 0, 3, 0)
        self.Settings_button = QPushButton(self.frame_5)
        self.Settings_button.setObjectName(u"Settings_button")
        sizePolicy1.setHeightForWidth(self.Settings_button.sizePolicy().hasHeightForWidth())
        self.Settings_button.setSizePolicy(sizePolicy1)
        self.Settings_button.setMinimumSize(QSize(129, 33))
        self.Settings_button.setFont(font3)
        self.Settings_button.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(29, 29, 29);\n"
"	border-radius:7px;\n"
"	padding-left:24px;\n"
"	border-width:1px;\n"
"	border-style:Inset;\n"
"	background-image: url(:/newPrefix/cil-settings.png);\n"
"	background-repeat:None;\n"
"	background-position:left;\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(163, 0, 0);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-width:2px;\n"
"	border-style:Inset;\n"
"	border-color: rgb(29, 29, 29);\n"
"	border-bottom-color: rgb(0, 255, 0);\n"
"\n"
"}")

        self.horizontalLayout_11.addWidget(self.Settings_button)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout_13.addWidget(self.leftMenuFrame)

        self.stackedWidget_2 = QStackedWidget(self.page2BaseFrame)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 33))
        self.stackedWidget_2.setStyleSheet(u"image: url(:/newPrefix/1775592.jpg);")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout_5 = QVBoxLayout(self.Home)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SearchBar_frame = QFrame(self.Home)
        self.SearchBar_frame.setObjectName(u"SearchBar_frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.SearchBar_frame.sizePolicy().hasHeightForWidth())
        self.SearchBar_frame.setSizePolicy(sizePolicy6)
        self.SearchBar_frame.setMinimumSize(QSize(0, 41))
        self.SearchBar_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 0);\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"image:none;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.SearchBar_frame.setFrameShape(QFrame.StyledPanel)
        self.SearchBar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.SearchBar_frame)
        self.horizontalLayout_19.setSpacing(9)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.SearchBar_frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"image:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.597, x2:1, y2:0.625, stop:0 rgba(61, 61, 61, 140), stop:1 rgba(28, 28, 28, 4));\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 3, -1, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.hm_brow_back_btn = QPushButton(self.frame_12)
        self.hm_brow_back_btn.setObjectName(u"hm_brow_back_btn")
        sizePolicy1.setHeightForWidth(self.hm_brow_back_btn.sizePolicy().hasHeightForWidth())
        self.hm_brow_back_btn.setSizePolicy(sizePolicy1)
        self.hm_brow_back_btn.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"Sitka Small")
        font4.setPointSize(9)
        font4.setUnderline(False)
        self.hm_brow_back_btn.setFont(font4)
        self.hm_brow_back_btn.setStyleSheet(u"QPushButton{\n"
"image:none;\n"
"	border-radius:32px;\n"
"\n"
"color: rgb(225, 225, 225);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"padding-top:3px;\n"
"\n"
"	\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hm_brow_back_btn.setIcon(icon)
        self.hm_brow_back_btn.setIconSize(QSize(22, 25))

        self.gridLayout_5.addWidget(self.hm_brow_back_btn, 0, 0, 1, 1)

        self.hm_brow_foward_btn = QPushButton(self.frame_12)
        self.hm_brow_foward_btn.setObjectName(u"hm_brow_foward_btn")
        sizePolicy1.setHeightForWidth(self.hm_brow_foward_btn.sizePolicy().hasHeightForWidth())
        self.hm_brow_foward_btn.setSizePolicy(sizePolicy1)
        self.hm_brow_foward_btn.setMinimumSize(QSize(27, 27))
        self.hm_brow_foward_btn.setFont(font4)
        self.hm_brow_foward_btn.setStyleSheet(u"QPushButton{\n"
"image:none;\n"
"	border-radius:32px;\n"
"color: rgb(225, 225, 225);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"padding-top:3px;\n"
"\n"
"	\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hm_brow_foward_btn.setIcon(icon1)
        self.hm_brow_foward_btn.setIconSize(QSize(22, 25))

        self.gridLayout_5.addWidget(self.hm_brow_foward_btn, 0, 2, 1, 1)

        self.hm_brow_reload_btn = QPushButton(self.frame_12)
        self.hm_brow_reload_btn.setObjectName(u"hm_brow_reload_btn")
        sizePolicy1.setHeightForWidth(self.hm_brow_reload_btn.sizePolicy().hasHeightForWidth())
        self.hm_brow_reload_btn.setSizePolicy(sizePolicy1)
        self.hm_brow_reload_btn.setMinimumSize(QSize(0, 0))
        self.hm_brow_reload_btn.setFont(font4)
        self.hm_brow_reload_btn.setStyleSheet(u"QPushButton{\n"
"image:none;\n"
"	border-radius:32px;\n"
"color: rgb(225, 225, 225);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"padding-top:3px;\n"
"\n"
"	\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hm_brow_reload_btn.setIcon(icon2)
        self.hm_brow_reload_btn.setIconSize(QSize(22, 23))

        self.gridLayout_5.addWidget(self.hm_brow_reload_btn, 0, 1, 1, 1)


        self.horizontalLayout_18.addLayout(self.gridLayout_5)

        self.frame_11 = QFrame(self.frame_12)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(4, 0, 0, 0)
        self.hm_searchBox = QLineEdit(self.frame_11)
        self.hm_searchBox.setObjectName(u"hm_searchBox")
        sizePolicy6.setHeightForWidth(self.hm_searchBox.sizePolicy().hasHeightForWidth())
        self.hm_searchBox.setSizePolicy(sizePolicy6)
        self.hm_searchBox.setMinimumSize(QSize(239, 33))
        font5 = QFont()
        font5.setPointSize(14)
        self.hm_searchBox.setFont(font5)
        self.hm_searchBox.setStyleSheet(u"QLineEdit{\n"
"image:none;\n"
"	border-top-right-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
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
        self.hm_searchBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.hm_searchBox)


        self.horizontalLayout_18.addWidget(self.frame_11)


        self.horizontalLayout_19.addWidget(self.frame_12)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setVerticalSpacing(0)
        self.Home_search_button = QPushButton(self.SearchBar_frame)
        self.Home_search_button.setObjectName(u"Home_search_button")
        sizePolicy1.setHeightForWidth(self.Home_search_button.sizePolicy().hasHeightForWidth())
        self.Home_search_button.setSizePolicy(sizePolicy1)
        self.Home_search_button.setMinimumSize(QSize(27, 27))
        self.Home_search_button.setFont(font4)
        self.Home_search_button.setStyleSheet(u"QPushButton{\n"
"image:none;\n"
"border-radius:10px;\n"
"color: rgb(225, 225, 225);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius:14px;\n"
"\n"
"	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.247788 rgba(253, 174, 65, 214), stop:0.25 rgba(255, 255, 255, 0));\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QPushButton::hover{\n"
"padding-top:3px;\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/cil-paper-plane.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home_search_button.setIcon(icon3)
        self.Home_search_button.setIconSize(QSize(24, 31))

        self.gridLayout_6.addWidget(self.Home_search_button, 0, 0, 1, 1)


        self.horizontalLayout_19.addLayout(self.gridLayout_6)


        self.verticalLayout_5.addWidget(self.SearchBar_frame)

        self.HomeBrowser = QWebEngineView(self.Home)
        self.HomeBrowser.setObjectName(u"HomeBrowser")
        self.HomeBrowser.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 170, 255);\n"
"image:none;\n"
"background-color: qlineargradient(spread:pad, x1:0.432136, y1:0.249, x2:0.5, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 129, 0, 115));\n"
"\n"
"\n"
"\n"
"}")

        self.verticalLayout_5.addWidget(self.HomeBrowser)

        self.stackedWidget_2.addWidget(self.Home)
        self.GoogleMapsPage = QWidget()
        self.GoogleMapsPage.setObjectName(u"GoogleMapsPage")
        self.horizontalLayout_14 = QHBoxLayout(self.GoogleMapsPage)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stacked2ContentBase = QFrame(self.GoogleMapsPage)
        self.stacked2ContentBase.setObjectName(u"stacked2ContentBase")
        self.stacked2ContentBase.setStyleSheet(u"image:none;\n"
"background-color: qlineargradient(spread:pad, x1:0.511364, y1:0, x2:0.522455, y2:1, stop:0 rgba(61, 61, 61, 167), stop:1 rgba(28, 28, 28, 160));")
        self.stacked2ContentBase.setFrameShape(QFrame.StyledPanel)
        self.stacked2ContentBase.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.stacked2ContentBase)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(4, 0, 3, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_9 = QFrame(self.stacked2ContentBase)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy6.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy6)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.Latitude = QLineEdit(self.frame_10)
        self.Latitude.setObjectName(u"Latitude")
        sizePolicy6.setHeightForWidth(self.Latitude.sizePolicy().hasHeightForWidth())
        self.Latitude.setSizePolicy(sizePolicy6)
        self.Latitude.setMinimumSize(QSize(239, 33))
        self.Latitude.setFont(font5)
        self.Latitude.setStyleSheet(u"QLineEdit{\n"
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
        self.Latitude.setInputMethodHints(Qt.ImhDigitsOnly)
        self.Latitude.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.Latitude)

        self.Longitude = QLineEdit(self.frame_10)
        self.Longitude.setObjectName(u"Longitude")
        sizePolicy6.setHeightForWidth(self.Longitude.sizePolicy().hasHeightForWidth())
        self.Longitude.setSizePolicy(sizePolicy6)
        self.Longitude.setMinimumSize(QSize(239, 33))
        self.Longitude.setFont(font5)
        self.Longitude.setStyleSheet(u"QLineEdit{\n"
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
        self.Longitude.setInputMethodHints(Qt.ImhDigitsOnly)
        self.Longitude.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.Longitude)


        self.horizontalLayout_15.addWidget(self.frame_10, 0, Qt.AlignLeft)

        self.searchMap_button = QPushButton(self.frame_9)
        self.searchMap_button.setObjectName(u"searchMap_button")
        sizePolicy1.setHeightForWidth(self.searchMap_button.sizePolicy().hasHeightForWidth())
        self.searchMap_button.setSizePolicy(sizePolicy1)
        self.searchMap_button.setMinimumSize(QSize(65, 65))
        self.searchMap_button.setFont(font4)
        self.searchMap_button.setStyleSheet(u"QPushButton{\n"
"	border-radius:32px;\n"
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
        self.searchMap_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_15.addWidget(self.searchMap_button, 0, Qt.AlignRight)


        self.gridLayout_4.addWidget(self.frame_9, 0, 0, 1, 1)

        self.mapWidget = QWebEngineView(self.stacked2ContentBase)
        self.mapWidget.setObjectName(u"mapWidget")

        self.gridLayout_4.addWidget(self.mapWidget, 1, 0, 1, 1)


        self.horizontalLayout_17.addLayout(self.gridLayout_4)


        self.horizontalLayout_14.addWidget(self.stacked2ContentBase)

        self.stackedWidget_2.addWidget(self.GoogleMapsPage)

        self.horizontalLayout_13.addWidget(self.stackedWidget_2)


        self.horizontalLayout_9.addWidget(self.page2BaseFrame)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.SizeGripFrame = QFrame(self.BaseFrame)
        self.SizeGripFrame.setObjectName(u"SizeGripFrame")
        sizePolicy.setHeightForWidth(self.SizeGripFrame.sizePolicy().hasHeightForWidth())
        self.SizeGripFrame.setSizePolicy(sizePolicy)
        self.SizeGripFrame.setMinimumSize(QSize(0, 11))
        self.SizeGripFrame.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.SizeGripFrame.setFrameShape(QFrame.StyledPanel)
        self.SizeGripFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.SizeGripFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bottom_drag = QFrame(self.SizeGripFrame)
        self.bottom_drag.setObjectName(u"bottom_drag")
        sizePolicy2.setHeightForWidth(self.bottom_drag.sizePolicy().hasHeightForWidth())
        self.bottom_drag.setSizePolicy(sizePolicy2)
        self.bottom_drag.setCursor(QCursor(Qt.SizeAllCursor))
        self.bottom_drag.setFrameShape(QFrame.StyledPanel)
        self.bottom_drag.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.bottom_drag)

        self.SizeGrip_bottom_right = QFrame(self.SizeGripFrame)
        self.SizeGrip_bottom_right.setObjectName(u"SizeGrip_bottom_right")
        sizePolicy.setHeightForWidth(self.SizeGrip_bottom_right.sizePolicy().hasHeightForWidth())
        self.SizeGrip_bottom_right.setSizePolicy(sizePolicy)
        self.SizeGrip_bottom_right.setMinimumSize(QSize(18, 18))
        self.SizeGrip_bottom_right.setCursor(QCursor(Qt.ArrowCursor))
        self.SizeGrip_bottom_right.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.SizeGrip_bottom_right.setFrameShape(QFrame.StyledPanel)
        self.SizeGrip_bottom_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.SizeGrip_bottom_right)


        self.verticalLayout_2.addWidget(self.SizeGripFrame)


        self.horizontalLayout.addWidget(self.BaseFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Box_name, self.Box_email)
        QWidget.setTabOrder(self.Box_email, self.Box_password)
        QWidget.setTabOrder(self.Box_password, self.LoginButton)
        QWidget.setTabOrder(self.LoginButton, self.CloseButton)
        QWidget.setTabOrder(self.CloseButton, self.Maximizebtn)
        QWidget.setTabOrder(self.Maximizebtn, self.Minimizebtn)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.Minimizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.Maximizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Maximizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.CloseButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CloseButton.setText("")
#if QT_CONFIG(tooltip)
        self.Box_name.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#9d0000;\">Enter Your Name</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Box_name.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter Your Name</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Box_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Name", None))
#if QT_CONFIG(tooltip)
        self.Box_email.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#9d0000;\">Enter Your Name</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Box_email.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter Your Name</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Box_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
#if QT_CONFIG(tooltip)
        self.Box_password.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#9d0000;\">Enter Your Name</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Box_password.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter Your Name</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Box_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
#if QT_CONFIG(tooltip)
        self.LoginButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#00b400;\">Login</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
#if QT_CONFIG(shortcut)
        self.LoginButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.Men_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Expand Menu</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Men_button.setText(QCoreApplication.translate("MainWindow", u"\u2630 ", None))
#if QT_CONFIG(tooltip)
        self.Account_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Account</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Account_button.setText(QCoreApplication.translate("MainWindow", u"Maps", None))
#if QT_CONFIG(tooltip)
        self.Home_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Home</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Home_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.Contact_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Mail</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Contact_button.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.search_progress.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
#if QT_CONFIG(tooltip)
        self.Settings_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.hm_brow_back_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Back</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hm_brow_back_btn.setText("")
#if QT_CONFIG(tooltip)
        self.hm_brow_foward_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Forward</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hm_brow_foward_btn.setText("")
#if QT_CONFIG(tooltip)
        self.hm_brow_reload_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Reload</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hm_brow_reload_btn.setText("")
#if QT_CONFIG(tooltip)
        self.hm_searchBox.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Search Bar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hm_searchBox.setText("")
        self.hm_searchBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
#if QT_CONFIG(tooltip)
        self.Home_search_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Search</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Home_search_button.setText("")
        self.Latitude.setText("")
        self.Latitude.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.Longitude.setText("")
        self.Longitude.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.searchMap_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi


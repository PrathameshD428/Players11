# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scores.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Dialog_3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 599)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 9, 341, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.match_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.match_1.setAlignment(QtCore.Qt.AlignCenter)
        self.match_1.setObjectName("match_1")
        self.verticalLayout.addWidget(self.match_1)
        self.match_1_link = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.match_1_link.setTextFormat(QtCore.Qt.RichText)
        self.match_1_link.setAlignment(QtCore.Qt.AlignCenter)
        self.match_1_link.setOpenExternalLinks(True)
        self.match_1_link.setObjectName("match_1_link")
        self.verticalLayout.addWidget(self.match_1_link)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.match_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.match_2.setAlignment(QtCore.Qt.AlignCenter)
        self.match_2.setObjectName("match_2")
        self.verticalLayout.addWidget(self.match_2)
        self.match_2_link = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.match_2_link.setTextFormat(QtCore.Qt.RichText)
        self.match_2_link.setAlignment(QtCore.Qt.AlignCenter)
        self.match_2_link.setOpenExternalLinks(True)
        self.match_2_link.setObjectName("match_2_link")
        self.verticalLayout.addWidget(self.match_2_link)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.match_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.match_3.setAlignment(QtCore.Qt.AlignCenter)
        self.match_3.setObjectName("match_3")
        self.verticalLayout.addWidget(self.match_3)
        self.match_3_link = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.match_3_link.setTextFormat(QtCore.Qt.RichText)
        self.match_3_link.setAlignment(QtCore.Qt.AlignCenter)
        self.match_3_link.setOpenExternalLinks(True)
        self.match_3_link.setObjectName("match_3_link")
        self.verticalLayout.addWidget(self.match_3_link)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.match_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.match_4.setAlignment(QtCore.Qt.AlignCenter)
        self.match_4.setObjectName("match_4")
        self.verticalLayout.addWidget(self.match_4)
        self.match_4_link = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.match_4_link.setTextFormat(QtCore.Qt.RichText)
        self.match_4_link.setAlignment(QtCore.Qt.AlignCenter)
        self.match_4_link.setOpenExternalLinks(True)
        self.match_4_link.setObjectName("match_4_link")
        self.verticalLayout.addWidget(self.match_4_link)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(120, 10, 20, 581))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(464, 10, 16, 581))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(130, 575, 341, 31))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Scores"))
        self.match_1.setPixmap(QPixmap("images/ind_aus.jpg"))
        self.match_1_link.setText(_translate("Dialog", "<a href=\"https://www.cricbuzz.com/live-cricket-scorecard/20250/ind-vs-aus-match-14-icc-cricket-world-cup-2019\">India vs Australia</a>"))
        self.match_2.setPixmap(QPixmap("images/ind_eng.jpg"))
        self.match_2_link.setText(_translate("Dialog", "<a href=\"https://www.cricbuzz.com/live-cricket-scorecard/20274/eng-vs-ind-match-38-icc-cricket-world-cup-2019\">India vs England</a>"))
        self.match_3.setPixmap(QPixmap("images/ind_rsa.jpg"))
        self.match_3_link.setText(_translate("Dialog", "<a href=\"https://www.cricbuzz.com/live-cricket-scorecard/20244/rsa-vs-ind-match-8-icc-cricket-world-cup-2019\">India vs South Africa</a>"))
        self.match_4.setPixmap(QPixmap("images/ind_nz.jpg"))
        self.match_4_link.setText(_translate("Dialog", "<a href=\"https://www.cricbuzz.com/live-cricket-scorecard/20282/ind-vs-nz-1st-semi-final-1-v-4-icc-cricket-world-cup-2019\">India vs New Zealand</a>"))
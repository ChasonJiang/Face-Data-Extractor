# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExtractorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Extractor(object):
    def setupUi(self, Extractor):
        Extractor.setObjectName("Extractor")
        Extractor.resize(550, 620)
        self.verticalLayout = QtWidgets.QVBoxLayout(Extractor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Extractor)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LogBox = QtWidgets.QTextBrowser(self.groupBox)
        self.LogBox.setStyleSheet("#LogBox{\n"
"background-color:rgba(0, 0, 0,200);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.LogBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LogBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LogBox.setLineWidth(0)
        self.LogBox.setObjectName("LogBox")
        self.verticalLayout_3.addWidget(self.LogBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Extractor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.openBtn = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openBtn.sizePolicy().hasHeightForWidth())
        self.openBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AniMe Matrix - MB_EN")
        font.setPointSize(20)
        self.openBtn.setFont(font)
        self.openBtn.setObjectName("openBtn")
        self.verticalLayout_2.addWidget(self.openBtn)
        self.templateBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.templateBtn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.templateBtn.sizePolicy().hasHeightForWidth())
        self.templateBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AniMe Matrix - MB_EN")
        font.setPointSize(20)
        self.templateBtn.setFont(font)
        self.templateBtn.setObjectName("templateBtn")
        self.verticalLayout_2.addWidget(self.templateBtn)
        self.extractBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.extractBtn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extractBtn.sizePolicy().hasHeightForWidth())
        self.extractBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("AniMe Matrix - MB_EN")
        font.setPointSize(20)
        self.extractBtn.setFont(font)
        self.extractBtn.setObjectName("extractBtn")
        self.verticalLayout_2.addWidget(self.extractBtn)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Extractor)
        QtCore.QMetaObject.connectSlotsByName(Extractor)

    def retranslateUi(self, Extractor):
        _translate = QtCore.QCoreApplication.translate
        Extractor.setWindowTitle(_translate("Extractor", "Extractor"))
        self.groupBox.setTitle(_translate("Extractor", "日志"))
        self.openBtn.setText(_translate("Extractor", "选择图片"))
        self.templateBtn.setText(_translate("Extractor", "选择人物卡模板[可选]"))
        self.extractBtn.setText(_translate("Extractor", "提取"))
        

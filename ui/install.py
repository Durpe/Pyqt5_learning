# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'install.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 350)
        MainWindow.setMinimumSize(QtCore.QSize(500, 350))
        MainWindow.setMaximumSize(QtCore.QSize(500, 350))
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.title_info = QtWidgets.QLabel(self.widget)
        self.title_info.setGeometry(QtCore.QRect(10, 10, 165, 16))
        self.title_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.title_info.setObjectName("title_info")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 33, 591, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.layoutWidget1 = QtWidgets.QWidget(self.widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 60, 481, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zw_check = QtWidgets.QCheckBox(self.layoutWidget1)
        self.zw_check.setMinimumSize(QtCore.QSize(50, 0))
        self.zw_check.setObjectName("zw_check")
        self.horizontalLayout.addWidget(self.zw_check)
        self.ZW_txtbox = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ZW_txtbox.setObjectName("ZW_txtbox")
        self.horizontalLayout.addWidget(self.ZW_txtbox)
        self.zw_selectfile = QtWidgets.QPushButton(self.layoutWidget1)
        self.zw_selectfile.setObjectName("zw_selectfile")
        self.horizontalLayout.addWidget(self.zw_selectfile)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.creo_check = QtWidgets.QCheckBox(self.layoutWidget1)
        self.creo_check.setMinimumSize(QtCore.QSize(50, 0))
        self.creo_check.setObjectName("creo_check")
        self.horizontalLayout_2.addWidget(self.creo_check)
        self.creo_txtbox = QtWidgets.QLineEdit(self.layoutWidget1)
        self.creo_txtbox.setObjectName("creo_txtbox")
        self.horizontalLayout_2.addWidget(self.creo_txtbox)
        self.creo_selectfile = QtWidgets.QPushButton(self.layoutWidget1)
        self.creo_selectfile.setObjectName("creo_selectfile")
        self.horizontalLayout_2.addWidget(self.creo_selectfile)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.layoutWidget2 = QtWidgets.QWidget(self.widget)
        self.layoutWidget2.setGeometry(QtCore.QRect(-10, 330, 591, 21))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_2 = QtWidgets.QFrame(self.layoutWidget2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.layoutWidget3 = QtWidgets.QWidget(self.widget)
        self.layoutWidget3.setGeometry(QtCore.QRect(150, 260, 209, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.confirm = QtWidgets.QPushButton(self.layoutWidget3)
        self.confirm.setObjectName("confirm")
        self.horizontalLayout_3.addWidget(self.confirm)
        self.cancel = QtWidgets.QPushButton(self.layoutWidget3)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_3.addWidget(self.cancel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "请选择软件安装目录"))
        self.title_info.setText(_translate("MainWindow", "请选择软件的安装目录："))
        self.zw_check.setText(_translate("MainWindow", "中望："))
        self.zw_selectfile.setText(_translate("MainWindow", "选择路径"))
        self.creo_check.setText(_translate("MainWindow", "Creo:"))
        self.creo_selectfile.setText(_translate("MainWindow", "选择路径"))
        self.confirm.setText(_translate("MainWindow", "确认"))
        self.cancel.setText(_translate("MainWindow", "取消"))



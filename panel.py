# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(70, 130, 141, 28))
        self.btn1.setObjectName("btn1")
        self.tbl1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl1.setGeometry(QtCore.QRect(280, 40, 471, 271))
        self.tbl1.setRowCount(30)
        self.tbl1.setColumnCount(3)
        self.tbl1.setObjectName("tbl1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(610, 320, 141, 28))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(450, 320, 141, 28))
        self.btn3.setObjectName("btn3")
        self.cmb2 = QtWidgets.QComboBox(self.centralwidget)
        self.cmb2.setGeometry(QtCore.QRect(610, 10, 137, 22))
        self.cmb2.setObjectName("cmb2")
        self.cmb2.addItem("")
        self.cmb2.addItem("")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 30, 139, 82))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lne1 = QtWidgets.QLineEdit(self.widget)
        self.lne1.setObjectName("lne1")
        self.verticalLayout.addWidget(self.lne1)
        self.lne2 = QtWidgets.QLineEdit(self.widget)
        self.lne2.setObjectName("lne2")
        self.verticalLayout.addWidget(self.lne2)
        self.cmb1 = QtWidgets.QComboBox(self.widget)
        self.cmb1.setObjectName("cmb1")
        self.cmb1.addItem("")
        self.cmb1.setItemText(0, "")
        self.cmb1.addItem("")
        self.cmb1.addItem("")
        self.verticalLayout.addWidget(self.cmb1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 30, 37, 81))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textlabel1 = QtWidgets.QLabel(self.widget1)
        self.textlabel1.setObjectName("textlabel1")
        self.verticalLayout_2.addWidget(self.textlabel1)
        self.textlabel2 = QtWidgets.QLabel(self.widget1)
        self.textlabel2.setObjectName("textlabel2")
        self.verticalLayout_2.addWidget(self.textlabel2)
        self.textlabel3 = QtWidgets.QLabel(self.widget1)
        self.textlabel3.setObjectName("textlabel3")
        self.verticalLayout_2.addWidget(self.textlabel3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "İsim Veritabanı"))
        self.btn1.setText(_translate("MainWindow", "Ekle"))
        self.btn2.setText(_translate("MainWindow", "Listele"))
        self.btn3.setText(_translate("MainWindow", "Sil"))
        self.cmb2.setItemText(0, _translate("MainWindow", "Kusha Engineering"))
        self.cmb2.setItemText(1, _translate("MainWindow", "Farsop"))
        self.cmb1.setItemText(1, _translate("MainWindow", "Kusha Engineering"))
        self.cmb1.setItemText(2, _translate("MainWindow", "Farsop"))
        self.textlabel1.setText(_translate("MainWindow", "Ad"))
        self.textlabel2.setText(_translate("MainWindow", "Soyad"))
        self.textlabel3.setText(_translate("MainWindow", "Şirket"))

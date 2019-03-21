# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vlados/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Trajectory_plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Trajectory_plot_btn.setGeometry(QtCore.QRect(620, 10, 161, 41))
        self.Trajectory_plot_btn.setObjectName("Trajectory_plot_btn")
        self.Moving_plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Moving_plot_btn.setGeometry(QtCore.QRect(620, 60, 161, 41))
        self.Moving_plot_btn.setObjectName("Moving_plot_btn")
        self.Velosity_plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Velosity_plot_btn.setGeometry(QtCore.QRect(620, 110, 161, 41))
        self.Velosity_plot_btn.setObjectName("Velosity_plot_btn")
        self.Axeleration_plot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Axeleration_plot_btn.setGeometry(QtCore.QRect(620, 160, 161, 41))
        self.Axeleration_plot_btn.setObjectName("Axeleration_plot_btn")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(620, 240, 117, 22))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(620, 210, 117, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.Close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Close_btn.setGeometry(QtCore.QRect(620, 560, 161, 51))
        self.Close_btn.setObjectName("Close_btn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 600, 600))
        self.widget.setObjectName("widget")
        self.Trajectory_plot_btn.raise_()
        self.Moving_plot_btn.raise_()
        self.Velosity_plot_btn.raise_()
        self.Axeleration_plot_btn.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.Close_btn.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Trajectory_plot_btn.setText(_translate("MainWindow", "Manipulator moving"))
        self.Moving_plot_btn.setText(_translate("MainWindow", "Q(t)"))
        self.Velosity_plot_btn.setText(_translate("MainWindow", "Q\'(t)"))
        self.Axeleration_plot_btn.setText(_translate("MainWindow", "Q\'\'(t)"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton"))
        self.Close_btn.setText(_translate("MainWindow", "Close"))


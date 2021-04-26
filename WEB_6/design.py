# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(730, 490)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(0, 70, 571, 411))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 30, 261, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 111, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(410, 10, 111, 18))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 30, 211, 32))
        self.lineEdit_2.setMaxLength(1000000)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(340, 30, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Frame)
        self.radioButton_2.setGeometry(QtCore.QRect(580, 80, 129, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Frame)
        self.radioButton_3.setGeometry(QtCore.QRect(580, 140, 129, 22))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Frame)
        self.radioButton_4.setGeometry(QtCore.QRect(580, 110, 129, 22))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 30, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(Frame)
        self.checkBox.setGeometry(QtCore.QRect(570, 10, 151, 22))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "TextLabel"))
        self.label_2.setText(_translate("Frame", "Введите запрос"))
        self.label_3.setText(_translate("Frame", "Полный аддрес"))
        self.pushButton.setText(_translate("Frame", "Сброс"))
        self.radioButton_2.setText(_translate("Frame", "Спутник"))
        self.radioButton_3.setText(_translate("Frame", "Гибрид"))
        self.radioButton_4.setText(_translate("Frame", "Карта"))
        self.pushButton_2.setText(_translate("Frame", "Поиск"))
        self.checkBox.setText(_translate("Frame", "Подключить индекс"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiNodeHead.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 540)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 130, 51, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 150, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 170, 51, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 281, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listView_2 = QtWidgets.QListView(self.gridLayoutWidget)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout_2.addWidget(self.listView_2, 2, 0, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(330, 0, 281, 351))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 0, 1, 2)
        self.listView_3 = QtWidgets.QListView(self.gridLayoutWidget_2)
        self.listView_3.setObjectName("listView_3")
        self.gridLayout_3.addWidget(self.listView_3, 2, 0, 1, 2)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 349, 611, 159))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.listView = QtWidgets.QListView(self.gridLayoutWidget_3)
        self.listView.setObjectName("listView")
        self.gridLayout_4.addWidget(self.listView, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArquivo = QtWidgets.QMenu(self.menuBar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menuBar)
        self.novoNode = QtWidgets.QAction(MainWindow)
        self.novoNode.setObjectName("novoNode")
        self.actionSair_2 = QtWidgets.QAction(MainWindow)
        self.actionSair_2.setObjectName("actionSair_2")
        self.actionNovo_Node = QtWidgets.QAction(MainWindow)
        self.actionNovo_Node.setObjectName("actionNovo_Node")
        self.actionRemove_Node = QtWidgets.QAction(MainWindow)
        self.actionRemove_Node.setObjectName("actinRemove_Node")
        self.actionFechar = QtWidgets.QAction(MainWindow)
        self.actionFechar.setObjectName("actionFechar")
        self.menuArquivo.addAction(self.actionNovo_Node)
        self.menuArquivo.addAction(self.actionRemove_Node)
        self.menuArquivo.addAction(self.actionFechar)
        self.menuBar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        self.actionFechar.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", ">>"))
        self.pushButton_2.setText(_translate("MainWindow", "<<"))
        self.pushButton_3.setText(_translate("MainWindow", "Iniciar"))
        self.lineEdit_2.setText(_translate(
            "MainWindow", "Servidores Disponiveis"))
        self.lineEdit_3.setText(_translate(
            "MainWindow", "Servidores Para uso"))
        self.lineEdit.setText(_translate("MainWindow", "Fluxo"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.novoNode.setText(_translate("MainWindow", "Novo node"))
        self.actionSair_2.setText(_translate("MainWindow", "Sair"))
        self.actionNovo_Node.setText(_translate("MainWindow", "Novo Node"))
        self.actionRemove_Node.setText(
            _translate("MainWindow", "Remover Node"))
        self.actionFechar.setText(_translate("MainWindow", "Fechar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

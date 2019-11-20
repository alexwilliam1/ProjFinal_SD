# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClienteInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_cliente(object):
    def setupUi(self, Dialog_cliente):
        Dialog_cliente.setObjectName("Dialog_cliente")
        Dialog_cliente.resize(633, 479)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog_cliente)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 40, 291, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_Status = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_Status.setReadOnly(True)
        self.textEdit_Status.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit_Status.setObjectName("textEdit_Status")
        self.gridLayout.addWidget(self.textEdit_Status, 0, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog_cliente)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 239, 291, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_Resposta = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_Resposta.setReadOnly(True)
        self.textEdit_Resposta.setObjectName("textEdit_Resposta")
        self.verticalLayout.addWidget(self.textEdit_Resposta)
        self.label = QtWidgets.QLabel(Dialog_cliente)
        self.label.setGeometry(QtCore.QRect(90, 210, 181, 23))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_cliente)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 41, 23))
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog_cliente)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 420, 281, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Fechar = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Fechar.setObjectName("pushButton_Fechar")
        self.horizontalLayout.addWidget(self.pushButton_Fechar)
        self.pushButton_AbrirArq = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_AbrirArq.setObjectName("pushButton_AbrirArq")
        self.horizontalLayout.addWidget(self.pushButton_AbrirArq)
        self.pushButton_Enviar = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Enviar.setObjectName("pushButton_Enviar")
        self.horizontalLayout.addWidget(self.pushButton_Enviar)
        self.textEdit_memoria = QtWidgets.QTextEdit(Dialog_cliente)
        self.textEdit_memoria.setReadOnly(True)
        self.textEdit_memoria.setGeometry(QtCore.QRect(490, 90, 104, 41))
        self.textEdit_memoria.setObjectName("textEdit_memoria")
        self.textEdit_cpu = QtWidgets.QTextEdit(Dialog_cliente)
        self.textEdit_cpu.setReadOnly(True)
        self.textEdit_cpu.setGeometry(QtCore.QRect(490, 190, 104, 41))
        self.textEdit_cpu.setObjectName("textEdit_cpu")
        self.textEdit_ValorPg = QtWidgets.QTextEdit(Dialog_cliente)
        self.textEdit_ValorPg.setReadOnly(True)
        self.textEdit_ValorPg.setGeometry(QtCore.QRect(490, 280, 104, 41))
        self.textEdit_ValorPg.setObjectName("textEdit_ValorPg")
        self.label_3 = QtWidgets.QLabel(Dialog_cliente)
        self.label_3.setGeometry(QtCore.QRect(360, 100, 121, 23))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog_cliente)
        self.label_4.setGeometry(QtCore.QRect(410, 200, 71, 23))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog_cliente)
        self.label_5.setGeometry(QtCore.QRect(380, 290, 101, 23))
        self.label_5.setObjectName("label_5")
        self.textEdit_cpu.raise_()
        self.gridLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.layoutWidget.raise_()
        self.textEdit_memoria.raise_()
        self.textEdit_ValorPg.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(Dialog_cliente)
        QtCore.QMetaObject.connectSlotsByName(Dialog_cliente)

    def retranslateUi(self, Dialog_cliente):
        _translate = QtCore.QCoreApplication.translate
        Dialog_cliente.setWindowTitle(_translate("Dialog_cliente", "Cliente"))
        self.label.setText(_translate(
            "Dialog_cliente", "Palavras erradas encontradas"))
        self.label_2.setText(_translate("Dialog_cliente", "Status"))
        self.pushButton_Fechar.setText(_translate("Dialog_cliente", "Fechar"))
        self.pushButton_AbrirArq.setText(
            _translate("Dialog_cliente", "Abrir Arquivo"))
        self.pushButton_Enviar.setText(_translate("Dialog_cliente", "Enviar"))
        self.label_3.setText(_translate(
            "Dialog_cliente", "Memória consumida:"))
        self.label_4.setText(_translate("Dialog_cliente", "CPU usada:"))
        self.label_5.setText(_translate(
            "Dialog_cliente", "Valor a ser pago: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_cliente = QtWidgets.QDialog()
    ui = Ui_Dialog_cliente()
    ui.setupUi(Dialog_cliente)
    Dialog_cliente.show()
    sys.exit(app.exec_())

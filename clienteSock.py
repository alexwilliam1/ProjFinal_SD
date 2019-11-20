import socket
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5 import QtCore, QtWidgets
from IFsGraphics.ClienteIF import Ui_Dialog_cliente
from cryptography.fernet import Fernet

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog_cliente):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.conexao()
        self.message = []
        # self.readText()
        self.enviar_msg()
        self.abrir_arq()
        self.pushButton_Fechar.clicked.connect(self.closeEvent)

    def conexao(self):
        while True:
            try:
                head_address = ('10.180.53.88', 10000)
                print('connecting to {} port {}'.format(*head_address))
                self.textEdit_Status.append(
                    'Maquina cliente conectada ao ip {}/{}'.format(*head_address))
                sock.connect(head_address)

                break
            except Exception as e:
                print("ERRO: ", e)
            break

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            return fileName

    def abrir_arq(self):
        self.pushButton_AbrirArq.clicked.connect(self.readText)

    def readText(self):
        fileName = self.openFileNameDialog()
        self.textEdit_Status.append("Lendo arquivo: "+str(fileName))

        arq = open(fileName, 'r')

        self.message = arq.read()

        # for lines in text:
        #    self.message = lines.split('\n')
        #    print(self.message[0])

        self.textEdit_Status.append(
            "Arquivo lido com sucesso e pronto para ser enviado!")

        # return conteudo

    def enviar_msg(self):
        self.pushButton_Enviar.clicked.connect(self.envia)

    def envia(self):
        try:
            #message = readText()
            # Send data
            #message = 'This is the message.  It will be repeated.'

            print('sending {!r}'.format(self.message))
            self.textEdit_Status.append('Enviando texto!')
            key = "ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=".encode()
            cipher_suite = Fernet(key)
            cipher_text = cipher_suite.encrypt(self.message.encode("utf-8"))

            size = str(len(self.message)).encode()
            sock.send(size)
            #resp = sock.recv(1024)

            sock.send(cipher_text)

            # Look for the response
            #amount_received = 0
            #amount_expected = len(self.message)
            received = False
            while not received:

                data = sock.recv(4*len(self.message))
                print("received data")
                if data:
                    dt = data.decode("utf-8")
                    #amount_received += len(data)
                    print('received {!r}'.format(dt))
                    self.textEdit_Resposta.append('Recebido ' + dt)
                    received = True

        finally:
            print('closing socket')
            sock.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

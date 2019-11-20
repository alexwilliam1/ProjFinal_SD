import socket
import sys
from spellchecker import SpellChecker
from cryptography.fernet import Fernet
from Servers.Node import Node
import threading
import psutil
import os
from IFsGraphics.NodeHeadUI import Ui_MainWindow
from IFsGraphics.NovoNodeUI import NovoNodeUI
import json
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class NovoNode(QtWidgets.QDialog, NovoNodeUI):
    def __init__(self, out, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.out = out
        self.pushButton_2.clicked.connect(self.reject)
        self.pushButton.clicked.connect(self.create)
    
    def getListView(self):
        
        model = self.out.listView_2.model()
        servers = []
        for i in range(model.rowCount()):
            servers.append(model.item(i).text())
        return servers
        

    def create(self):

        self.out.nodeId += 1
        nid = "machine_"+str(self.out.nodeId)

        with open('nodes.txt','a') as json_file:
            pass

        if (os.path.getsize("nodes.txt") > 0):
            with open('nodes.txt', 'r') as json_file:
                data = json.load(json_file)
                id = len(data['node'])
                nid = "machine_"+str(id+1)

      
        status = "ativo"
        ram = int(self.lineEdit_3.text())
        cpu = 1
        ip = self.lineEdit.text()
        port = int(self.lineEdit_2.text())
        key = "ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg="
        self.out.node = Node(nid, status, ram, cpu, ip, port, key)
        self.out.nodes.append(self.out.node)
       

        node = {}
        node['node'] = []
        node['node'].append({
            'id': nid,
            'status': "ativo",
            'ip': ip,
            'port': port,
            'key': key,
            'ram': ram
        })

        if (os.path.getsize("nodes.txt") > 0):
            with open('nodes.txt', 'r') as json_file:
                data = json.load(json_file)
                data['node'].append({
                    'id': nid,
                    'status': "ativo",
                    'ip': ip,
                    'port': port,
                    'key': key,
                    'ram': ram
                })
            with open('nodes.txt', 'w') as outfile:
                json.dump(data, outfile)

                   
        
        else:
            with open('nodes.txt', 'w') as outfile:
                json.dump(node, outfile)

       
        sv = self.getListView()
        maquina = "IP: "+ip+'\nPorta: '+str(port)+'\nStatus: '+status
        sv.append(maquina)
        
        model = QtGui.QStandardItemModel()
        self.out.listView_2.setModel(model)
        for x in sv:
            item = QtGui.QStandardItem(x)
            model.appendRow(item) 
        self.out.fluxo('Node adicionado')

    

class NodeHead(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, key, port,*args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
       
        self.setupUi(self) 
        self.key = key
        self.server_address = ('', port)
        self.nodes = []
        self.nodeId = 0
        self.count = 0
        self.wrongWords = []
        self.threadList = []
        self._want_to_close = False
        self.sk = None
        self.menuBar.addAction
        self.actionNovo_Node.triggered.connect(self.newNodeUI)
        self.fluxo('Iniciando NodeHead...')
        self.readServers()
       
    def fluxo(self,msg):
        model = self.listView.model()
        fluxo = []
        if model:
            for i in range(model.rowCount()):
                fluxo.append(model.item(i).text())

        fluxo.append(msg)
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in fluxo:
            item = QtGui.QStandardItem(i)
            model.appendRow(item) 

    def readServers(self):
        self.fluxo('carregando lista de nodes ')
        with open('nodes.txt','a') as json_file:
            pass
       
           
        if (os.path.getsize("nodes.txt") > 0):
            model = QtGui.QStandardItemModel()
            self.listView_2.setModel(model)
            with open('nodes.txt', 'r') as json_file:
                data = json.load(json_file)
                for p in data['node']:
                  
                    ip = "IP: " + p['ip']
                    porta = "\nPorta: "+ str(p['port'])
                    status = "\nStatus: " + p['status']
                    i = ip+porta+status
                    item = QtGui.QStandardItem(i)
                    model.appendRow(item) 

                    self.node = Node(p['id'],  p['status'],  p['ram'], 1,  p['ip'],  p['port'],  p['key'])
                    self.nodes.append(self.node)
                    

                  

    def newNodeUI(self):
        n = NovoNode(self)
        n.exec_()
      
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Você deseja realmente sair?", QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self._want_to_close = True
            self.sk.close()
            event.accept()
        else:
            event.ignore()
        

    def decryptData(self, data, key):
        self.cipher_suite = Fernet(self.key)
        self.des = self.cipher_suite.decrypt(data)
        return self.des

    def encryptData(self, data, key):
        cipher_suite = Fernet(key.encode())
        en = cipher_suite.encrypt(data)
        return en

    def headConnection(self):
       
         # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk =self.sock
                # Bind the socket to the port
        print('starting up on {} port {}'.format(*self.server_address))
        try:
            self.fluxo('starting up on {} port {}'.format(*self.server_address))
        except Exception:
            pass
        self.sock.bind(self.server_address)
        # Listen for incoming connections
        self.sock.listen(2)
       
        while True:
            # Wait for a connection
            print('waiting for a connection')
            try:
                self.fluxo('waiting for a connection')
            except Exception:
                pass
            try:
                self.connection, self.client_address = self.sock.accept()
                try:
                    self.fluxo('connection from '+str(self.client_address))
                except Exception:
                    pass
                try:
                    print('connection from', self.client_address)
                    try:
                        self.fluxo('connection from '+str(self.client_address))
                    except Exception:
                        pass
                    # Receive the data in small chunks and retransmit it
                    while True:
                        try:
                          
                            size = self.connection.recv(64)
                        #print('received {!r}'.format(data))
                            #self.connection.sendall("OK".encode())
                            print("received size",size.decode('utf-8'))
                            self.data = self.connection.recv(4*int(size.decode('utf-8')))
                            print("len data")
                            if self.data:
                                self.des = self.decryptData(self.data, self.key)
                                print('sending data back to the node cliente')
                                try:
                                    self.fluxo('sending data back to the node cliente')
                                except Exception:
                                    pass
                                self.nodeConnection(self.des, self.connection)
                                break
                                                
                        except (KeyboardInterrupt):
                            break
                except (KeyboardInterrupt):
                    break

                finally:
                    # Clean up the connection
                    self.connection.close()
            except Exception:
                break

    def quebraTexto(self, msg, qtd):
        msg = msg.decode('utf-8')
        auxiliar = msg.split()
        print("quebtando texto")
        n = qtd
        textoQuebrado = []
        len_l = len(auxiliar)
        for i in range(n):
            start = int(i * len_l / n)
            end = int((i + 1) * len_l / n)
            textoQuebrado.append(auxiliar[start:end])
        print(textoQuebrado)
        textoFinal = ''
        textPronto = []
      
        for i in textoQuebrado:
            t=""
            for c in i:
                t += c + " "
            textPronto.append(t)
        
        
        print(textPronto)
        return textPronto                

    def threadNode(self, conn, data):
        
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        address = (conn.getIp(), conn.getPort())
       
        try:
            print('connecting to Server on {} port {}'.format(*address))
            sk.connect(address)
            cipher_text = self.encryptData(data, conn.getKey())
            size = len(self.data)
            tam = str(size)+": "
            sk.send(tam.encode())
            sk.send(cipher_text)
            
            print("send data sucefull", address)
            
            th=True
                    
            while th:
                try:
                    
                    size = sk.recv(4)
                    print("received size",size.decode('utf-8'))
                    resp = sk.recv(4*int(size.decode('utf-8')))
                    print("received data")
                    #print('received {!r}'.format(data))
                    if resp:
                        print("accept data node client")
                        words = self.decryptData(resp, conn.getKey())
                        print(words)
                        #self.connection.sendall(words)
                        self.wrongWords.append(words.decode('utf-8'))
                        th = False
                        sk.close()
                        self.count += 1
                        break
                        
                except Exception as e:
                    print("Error 03", e)
                    break
        except Exception as e:
            print("Error 02", e)
        
        print("Node finalizado: ", conn.getId())

    def nodeConnection(self, data, connection):

        nser = len(self.nodes)
        print(nser)
        textDiv = self.quebraTexto(data,nser)
       
        n=0

        if not self.nodes:
            self.readServers()
       
        for conn in self.nodes:
            t = threading.Thread(target = self.threadNode, args = (conn, textDiv[n].encode()))
            self.threadList.append(t)
            n += 1

        for t in self.threadList:
            t.start()

        while True:
            if self.count == len(self.threadList):
                print("processamento completo")
                self.fluxo('processamento completo')
                aux = ""
                for x in self.wrongWords:
                    aux += x
                connection.sendall(aux.encode())
                break
        for t in self.threadList:
            t = None
        self.threadList.clear()
        self.count = 0


    def createNodes(self):
        self.nodeId += 1
        nid = "machine_"+str(self.nodeId)
        status = "ativo"
        ram = 512
        cpu = 1
        ip = "192.168.0.106"
        port = 10001
        key = "ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg="
        self.node = Node(nid, status, ram, cpu, ip, port, key)
        self.nodes.append(self.node)

        '''self.nodeId += 1
        nid = "machine_"+str(self.nodeId)
        status = "ativo"
        ram = 512
        cpu = 1
        ip = "192.168.0.106"
        port = 10002
        key = "ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg="
        nd = Node(nid, status, ram, cpu, ip, port, key)
        self.nodes.append(nd)'''


if __name__ == "__main__":
    keyCliente = "ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=".encode()
    port = 10000
    app = QtWidgets.QApplication([])
    window = NodeHead(keyCliente, port)
    t = threading.Thread(target = window.headConnection, args = ())
    t.start()
    window.show()
    app.exec_()

    
  
    
   
   
   
    # limit process memory to 50 MB 
  

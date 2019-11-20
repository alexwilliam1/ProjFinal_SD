import socket
import sys
from spellchecker import SpellChecker
from cryptography.fernet import Fernet
from Node import Node
import threading
import psutil
import os
import math




class Server2:

    def __init__(self, key, port):
        self.key = key
        self.server_address =  ('', port)
        self.warning = False
        self.used = 0
        self.memInit = 0
        self.p = None
        self.cpu = 0
      

    
    def limitResources(self,memory):
        self.warning=False
        p = psutil.Process(os.getpid())
        used = p.memory_info().rss
        self.memInit = used
        self.p =  p
        self.p.cpu_percent(interval=0.1) 
        threshold = memory * math.pow(10,6)#7 mbs
        reserved = threshold * 0.1 #reserva de 1% estatica
        threshold += used
      
        print("init: ",used, "max: ", threshold)
       

        while True:
            try:
                if(used+reserved <= threshold):
                    if(self.used < used):
                        self.used = used
                    used =  p.memory_info().rss
                else:
                    self.warning = True
                    self.used = used
                    
                    print("warning threshold",used,threshold)
                    break
            except:
                print("An error ocurred")
        
        print("memory used in bytes:", used - self.memInit )
    
    def decryptData(self,data):
        self.cipher_suite = Fernet(self.key)
        self.des = self.cipher_suite.decrypt(data)
        return self.des

    def encryptData(self, data):
        cipher_suite = Fernet(self.key)
        en = cipher_suite.encrypt(data)
        return en

    def getResources(self):
        res =  (self.used-self.memInit) / math.pow(10,6)
        
        return "Memory used: " +str(res) + " mbs\nCPU used: "  + str(self.cpu) +"%"
      


    def serverConnection(self):
         # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        print('starting up on {} port {}'.format(*self.server_address))
        self.sock.bind(self.server_address)
        # Listen for incoming connections
        self.sock.listen(2)
        
        while True:
            # Wait for a connection
            print('waiting for a connection')
            
            self.connection, self.client_address = self.sock.accept()
            try:
                print('connection from', self.client_address)
               
                # Receive the data in small chunks and retransmit it
                while True: 
                    try:
                        size = self.connection.recv(64)
                        buff = size.decode().split(":")
                        tam = int(buff[0])
                        print("received size",tam)
                        self.data = self.connection.recv(4*tam)
                        print("len data")
                    #print('received {!r}'.format(data))
                        if self.data:
                            self.des = self.decryptData(self.data)
                            print("decoded")
                            self.wr = self.showWrongWords(self.des)
                            self.wr += "\n"+self.getResources()
                            self.resp = self.wr.encode('utf-8')
                            print('sending data back to the client')
                            size = str(len(self.wr))
                            self.connection.send(size.encode())
                            self.connection.send(self.encryptData(self.resp))
                            break
                        else:
                            print('no data from', self.client_address)
                            break
                    except (KeyboardInterrupt):
                        break
                    
            
            except (KeyboardInterrupt):
                break

            finally:
                # Clean up the connection
                self.connection.close()

    # get Wrong Words
    def showWrongWords(self,param):
        self.spell = SpellChecker()
        self.param = param.decode("utf-8")
        self.wrong = ""  
        if(not self.warning):
            self.data = self.param.split(". ") #separando as frases
            self.words = []

        if(not self.warning):
            for d in self.data: #limpando os dados e montando lista de palavras
                if(not self.warning):
                    self.lista = d.split(" ")
                    for l in self.lista:
                        print(l)
                        if(not self.warning):
                            self.words.append(l)
                        else:
                            break
                else:
                    break
              
        if(not self.warning):
            self.misspelled = self.spell.unknown(self.words) #pegando palavras desconhecidas
            for word in self.misspelled:
                if(not self.warning):
                    print("Unkown: " +word)
                    self.wrong += word + " " #montando string com palavras erradas
                else:
                    par = "\n[Memoria Excedida] O texto foi processado parcialmente!\n"
                    self.wrong = par + self.wrong
                    
                    break
        if(self.wrong ==""):
            self.wrong = "\n[Memoria Excedida] Não foi possivel processar o texto"

        self.cpu = self.p.cpu_percent(interval=None)
        return self.wrong


if __name__ == "__main__":
    keyCliente = "ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=".encode()
    port = 10002
    n = Server2(keyCliente, port)

    try:
        t = threading.Thread(target = n.limitResources, args = (500,))#memory 40 mbs
        t.start()
       
      
    finally:
        print("iniciando servidor")
        n.serverConnection()
   
   
    
    
  

   

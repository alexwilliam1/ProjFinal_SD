

class Node:
    def __init__(self, id,status, memory, cpu, ip,port, key):
        self.id = id
        self.ip = ip
        self.port = port
        self.status = status
        self.maxMemory = memory
        self.maxCPU = cpu
        self.count = 0
        self.key = key
        self.spent = []

    def setIp(self, ip):
        self.ip = ip

    def getIp(self):
        return self.ip
    
    def setPort(self,port):
        self.port = port

    def getPort(self):
        return self.port

    def setKey(self, key):
        self.key = key
    
    def getKey(self):
        return self.key

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setMaxMemory(self,memory):
        self.maxMemory = memory

    def getMaxMemory(self):
        return self.maxMemory
    
    def setmaxCPU(self,cpu):
        self.maxCPU = cpu

    def getMaxCPU(self):
        return self.maxMemory

    def setStatus(self,status):
        self.status = status

    def getStatus(self):
        return self.status
        
    def setSpent(self,memory,cpu, valor):
        self.count += 1
        th = {"process": "Task: "+str(self.count),
                "memory": memory,
                "cpu": cpu,
                "spent": valor }
        self.spent.append(th)
    def getSpent(self):
        return self.spent






        
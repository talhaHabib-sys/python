import socket
ip=socket.gethostbyname(socket.gethostname())
for p in  range(65535):
    try:
        serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serv.bind((ip,p))
    except:
        print('{open} port:',p)
    serv.close()
                      
            

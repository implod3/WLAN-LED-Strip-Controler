import socket
import binascii

class controler:
    
    def __init__(self):
    
        self.colors = {
                        1: b'71230fa3',
                        2: b'71240fa4',
                        3: b'6125070f9c',
                        4: b'31ff880d00000fd4'
                    }
    
    def control(self, ip, port=5577):
        
        chg = input('1: on\n2: off\n3: Switch color\n4: soft yellow tone\n')
        
        chg = int(chg)
        
        if chg <= 0 or chg > len(self.colors):
            print("Wrong input")
            return 0
        
        message = binascii.unhexlify(self.colors[chg])
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(message)
        s.close()

c = controler()
c.control('192.168.1.100')
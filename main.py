import socket
import binascii

ip = '192.168.1.100'
port = 5577
buffer_size = 1024
on = b'71230fa3'
off = b'71240fa4'
switchcolor = b'6125070f9c'

ch = input('1: on\n2: off\n3: Swithc color\n')

if ch == '1':
    message = binascii.unhexlify(on)
elif ch == '2':
    message = binascii.unhexlify(off)
elif ch == '3':
    message = binascii.unhexlify(switchcolor)
else:
    print("Error")
    exit()

print(message)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(message)
s.close()
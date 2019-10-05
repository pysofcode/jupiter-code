import socket		# Simple  Pytho Client

T_PORT = 6001
TCP_IP = '127.0.0.1'
BUF_SIZE = 1024


# create a socket object name 'k'
c = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
c.connect((TCP_IP, T_PORT))
c.send(b"Hello John")
data = c.recv(BUF_SIZE)
print('Received back', repr(data))
c.close

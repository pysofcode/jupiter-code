import socket	# Simple Network Program Using Python

T_PORT = 6001
TCP_IP = '127.0.0.1'
BUF_SIZE = 1024

# create a socket object name 'c'
c = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
c.bind((TCP_IP, T_PORT))
c.listen(1)
con, addr = c.accept()
print ('Connection Address is: ' , addr)

while True :
    data = con.recv(BUF_SIZE)
    if not data: 
        break
    print ("Received data", data)
    con.send(b"OK, I am here.")

con.close()

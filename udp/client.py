
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('localhost', 8001)
import time
while True:
	time.sleep(2)
	msg = input('>>')
	sock.sendto(msg.encode(), addr)
	#print sock.recv(1024)
sock.close()
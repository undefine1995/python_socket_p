
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8001))

while True:
	data,address = sock.recvfrom(2048)
	if not data:
		print('no message')
		break
	print('received:%s from %s' % (data, address))

sock.close()
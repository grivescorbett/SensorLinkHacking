import socket
from struct import *
import time
import signal
import sys

def base10ToBase127(x):
	bytes = [0,0,0]
	while x >= 127**2:
		x-=127**2
		bytes[0] = bytes[0] + 1
	while x  >= 127:
		x-=127
		bytes[1] = bytes[1] + 1
	bytes[2] = x

	return pack('BBB',bytes[0],bytes[1],bytes[2])

def appendSensorNumber(s, num):
	return pack('cccB',s[0],s[1],s[2],0x80+num)

if __name__ == '__main__':
	TCP_IP = '0.0.0.0'
	TCP_PORT = 1341

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)

	conn, addr = s.accept()

	def signal_handler(signal, frame):
		conn.close()
		sys.exit()
	signal.signal(signal.SIGINT, signal_handler)

	print 'Connection address:', addr
	x = 0
	while 1:
		# userInput = raw_input('Enter Winch Value ')
		winchPacket = appendSensorNumber(base10ToBase127(x),1)
		conn.send(winchPacket)
		x += 1
		x = x % 50
		time.sleep(.5)
	conn.close()
#!/usr/bin/python2.7
#Scans all defined ports in range function. Shows open ones. Needs target ip as argument.

import socket,sys

host = sys.argv[1]

port_list = range(1,65535)

for port in port_list:
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		if sock.connect_ex((host,port)) == 0:
			print" [+] Port {0} is OPEN".format(port)
	except socket.error:
		print "ERROR !"

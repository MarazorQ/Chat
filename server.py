#!/usr/bin/env python3

import socket, time


quit = False
host = socket.gethostbyname(socket.gethostname())#input
print(host)




clients = []

while True:
	try:
		port =  int(input('Vvedite port: '))
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s.bind((host,port))
		break
	except OSError:
		print("port zanyat , poprobuy eshe))")

print("[ Server Started ]")

while not quit:
	try:
		data, addr = s.recvfrom(1024)#Блокирует программу и ждет ответа

		if addr not in clients:
			clients.append(addr)

		itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

		print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
		print(data.decode("utf-8"))

		for client in clients:
			if addr != client:
				s.sendto(data,client)
	except:	
		print("\n[ Server Stopped ]")
		s.close()
		quit = True

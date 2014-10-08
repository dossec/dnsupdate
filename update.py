import socket
import string
import fileinput
import os


def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('www.gmail.com', 0))
    return s.getsockname()[0]


def updateIP(IP):
	fout = open("output.dat", "w")
	for line in fileinput.input("script.txt"):
		#print line
		line = string.replace(line, "SERVER_NEW_IP", IP)
		#print line
		fout.write(line)

	fout.close()

	os.system("nsupdate -k Ktest.domain.name.key -v output.dat")
	os.system("dig @ns.domain.name test.domain.name")


    
IP =  getNetworkIp()

ipdata = open("ip.dat", "r")
line = ipdata.read()
ipdata.close()

print IP
print line

if IP != line:
	print "IP is different"
	ipdata = open("ip.dat","w")
	ipdata.write(str(IP))
	ipdata.close()
	updateIP(IP)
	
else:
	print "IP is the same"

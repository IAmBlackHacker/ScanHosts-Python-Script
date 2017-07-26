import os
import sys
import threading
help="""---------------- HOST SCAN ---------------
	python get_hosts.py [options]
	options -s startip
	options -e endip
	EX . python get_hosts.py -s 10.1.1.0 -e 10.1.1.225
	"""
if len(sys.argv)!=5:
	print(help)
	sys.exit(0)

def ping(ip):
	if not os.system('ping '+ip+' >'+ip):
		print(ip+' is alive!')
	os.system('del '+ip)
startip=list(map(int,sys.argv[sys.argv.index('-s')+1].strip().split('.')))
endip=list(map(int,sys.argv[sys.argv.index('-e')+1].strip().split('.')))
while startip != endip:
	ip='.'.join(map(str,startip))
	threading.Thread(target=ping,args=(ip,)).start()
	startip[3]+=1
	if startip[3]%256==0:
		startip[3]=0
		if (startip[2]+1)%256==0:
			startip[2]=0
			if (startip[1]+1)%256==0:
				startip[1]=0
				if (startip[0]+1)%256==0:
					startip[0]=0
					
				else:
					startip[0]+=1
			else:
				startip[1]+=1
		else:
			startip[2]+=1
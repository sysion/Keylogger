import os

kfile=os.path.join(os.path.dirname(os.path.abspath(__file__)),'.kfile')			# ok
#kfile=os.path.join(os.getcwd(),'.kfile')                                   # ok

class KeyLogger:
	def captureKey(self):
		with open(kfile,'a') as f:
			while True:
				ckey=input()
				f.write(ckey+'\n')
				#print(ckey)

def logfile():
	if not os.path.exists(kfile):
		with open(kfile, 'w+'): pass    # create a new file if not exists

def klog():
	kl=KeyLogger()
	kl.captureKey()

if __name__=='__main__':
	logfile()
	klog()

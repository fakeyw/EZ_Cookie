import base64 as b64

class cipher(object):
	def __init__(self,enc,dec):
		self.enc = enc
		self.dec = dec

def str2b64(string): #str -> str
	return b64.b64encode(string.encode('utf-8')).decode('utf-8')
		
def b642str(base64):  
	return b64.b64decode(base64.encode('utf-8').decode('utf-8'))
	
base64 = cipher(str2b64,b642str)
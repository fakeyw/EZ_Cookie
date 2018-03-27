from datetime import datetime
from builtin_crypto import base64
import builtin_crypto as cipher

'''
fields : (list)
ttl : (int) time to live (s) / False
crypto : (list) [enc,dec] / None / cipher.rsa[aes...]
'''
class cookier(object):
	def __init__(self,fields,TTL=1800,crypto=None):
		self.fields = fields
		self.TTL = TTL
		if crypto == None:
			self.crypto = False
		else:
			self.crypto = True
			self.enc = crypto[0]
			self.dec = crypto[1]
			
	def get(self,TTL=None,**kw): #flex ttl
		cookie_str = []
		for i in self.fields:
			cookie_str.append(base64.enc(kw[i]))
		#add a timestamp
		if TTL == None:
			TTL = self.TTL
		time = datetime.now().timestamp()
		if TTL == False:
			time += 100000000 #
		else:
			time = time - self.TTL + TTL 
		cookie_str.append(base64.enc(str(time)))
		cookie = '-'.join(cookie_str)
		if self.crypto :
			cookie = self.enc(cookie)
		return cookie
		
	def check(self,cookie): #None means tle, Exception may means Unknown cookie
		info = dict()
		if self.crypto:
			cookie = self.dec(cookie)
		l = cookie.split('-')
		tle = False
		if self.TTL != False:
			time = float(base64.dec(l[-1]))
			tle = self.tle_check(time)
			
		if tle == False:
			for k,v in zip(self.fields,l[:-1]):
				info[k] = base64.dec(v)
			return info
		else:
			return None

	def set_TTL(self,TTL):
		self.TTL = TTL
		
	def tle_check(self,timestamp):
		if datetime.now().timestamp()-timestamp > self.TTL:
			return True
		else:
			return False
		
	
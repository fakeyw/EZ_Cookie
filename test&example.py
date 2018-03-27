from Cookier import cookier
import time
fields = ['name','uuid']
MyCookie = cookier(fields,TTL=1000)
c = MyCookie.get(TTL=5,name='Tick',uuid='S7NZ89')
print(c)	
print(MyCookie.check(c))
time.sleep(6)
print(MyCookie.check(c))
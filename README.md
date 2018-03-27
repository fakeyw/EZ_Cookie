**Init a handler**

```python
from Cookier import cookier,cipher
'''cookier(fields, [TTL=1800,crypto=None])'''
MyCookie = cookier(['name','uuid'],ttl=1000,crypto=[cipher.base64.enc,cipher.base64.dec])
```

fields : list type like ['name','uuid'] 

ttl : (int) time to live (s) / (bool) False (infinite)

crypto : list type like [enc_func,dec_func]

---

**Get cookie**

```python
'''get(TTL=None,**kw)'''
c = MyCookie.get(TTL=5,name='Tick',uuid='S7NZ89')
```

TTL can be changed flexably.

If 'TTL' is `None` , it'll not change and use value in `init` process.

If 'TTL' is `False `  , it'll have a long time to live. 

---

**Check cookie**

```python
info = MyCookie.check(cookie_str)
name = info['name']
```

This func will return `None`  if cookie tle.

When cookie can't be parse, an `Exception ` will be raised.

---

**Other**

```python
MyCookie.set_TTL(500)
```

Just change setting of TTL 
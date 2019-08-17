Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:22:17) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:\Dados\Miguel\PucCoisaDeFazer\erro1.py =============
>>> notNull([])
>>> notNull([None])
'nullitem'
>>> notNull([None])
'nullitem'
>>> 
>>> notNull()

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    notNull()
TypeError: notNull() takes exactly 1 argument (0 given)
>>> notNull(None)
'nullarray'
>>> 

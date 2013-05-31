#!/usr/bin/env python2

s = b'hello'
print repr(s), type(s) # bytestring, OK
s = s.decode('utf8')
print repr(s), type(s) # Unicode string, OK
s = s.decode('utf8') # should be type error
print repr(s), type(s) # Wat
s = s.decode('utf8') # Wat
s = s.decode('utf8') # Wat
s = s.decode('utf8') # Wat
s = s.decode('utf8') # Wat
s = s.decode('utf8') # Wat
s = s.decode('utf8') # Wat
print repr(s), type(s) # WAT

# -*- coding: utf-8 -*-
# python suck8.py
# python suck8.py | less

import sys

print 'sys.getdefaultencoding():', sys.getdefaultencoding()
print 'sys.stdout.encoding:', sys.stdout.encoding

# Hack-ish?!
if sys.stdout.encoding is None:
    sys.stdout.write(u'Python \xbb Sücks!\n'.encode('utf-8'))
else:
    sys.stdout.write(u'Python \xbb Sücks!\n')

sys.stdout.flush()


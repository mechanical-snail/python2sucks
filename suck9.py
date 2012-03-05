# -*- coding: utf-8 -*-
# python suck9.py
# python suck9.py | less
# LC_CTYPE='ISO8859-1' python suck9.py
# LC_CTYPE='ISO8859-1' python suck9.py | less
# LC_CTYPE='UTF8' python suck9.py
# LC_CTYPE='UTF8' python suck9.py | less

import sys
import locale

print 'sys.getdefaultencoding():', sys.getdefaultencoding()
print 'sys.stdout.encoding:', sys.stdout.encoding

_, enc = locale.getdefaultlocale()
print 'locale.getdefaultlocale():', enc

sys.stdout.write(u'Python \xbb Sücks!\n'.encode(enc))
sys.stdout.flush()


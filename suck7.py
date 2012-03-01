# -*- coding: utf-8 -*-
# What the Fax?
# python suck7.py | less
# python suck7.py > somefile

import sys

print 'sys.stdout.encoding:', sys.stdout.encoding
print 'sys.stderr.encoding:', sys.stderr.encoding

sys.stderr.write(u'ERR: Python \xbb Sücks!\n')
sys.stderr.flush()

sys.stdout.write(u'OUT: Python \xbb Sücks!\n')
sys.stdout.flush()


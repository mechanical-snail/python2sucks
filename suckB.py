#!/usr/bin/env python2

# Shows up in "narrow builds" of Python, which were used in Python 2 on Windows

# N.B. Python 3.0 through 3.2 inclusive also have this problem (http://stackoverflow.com/questions/14790708/do-unicode-strings-in-python-3-still-depend-on-narrow-wide-builds)

# See, one character
s = u'\U0001f4a9'
print len(s) # may print 2

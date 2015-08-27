import os
import sys
from crashBase import crashBase

class sysrqc(crashBase):
    def __init__(self):
        crashBase.__init__(self)
    def crash(self):
        print 'sysrqc'
        sys.stdout = open('/proc/sysrq-trigger')
        print 'c'
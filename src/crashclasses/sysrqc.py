import os
from crashBase import crashBase

class sysrqc(crashBase):
    def __init__(self):
        crashBase.__init__(self)
    def crash(self):
        print 'sysrqc'
        os.system('echo c > /proc/sysrq-trigger')

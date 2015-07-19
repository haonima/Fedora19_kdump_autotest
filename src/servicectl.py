#!/usr/bin/env python

import commands
import time
from exception import *

class serviceCtl:
    def __init__(self,service):
        self.service = service
    
    def start(self):
        cmd='systemctl start ' + self.service +'.service'
        status = commands.getstatusoutput(cmd)[0]
        if status!=0:
            raise commandFailException(cmd, status)
        
    def restart(self):
        cmd='systemctl restart ' + self.service +'.service'
        print 'restarting service %s ...'%self.service
        time.sleep(10)
        status = commands.getstatusoutput(cmd)[0]
        if status!=0:
            raise commandFailException(cmd, status)        
        
    def stop(self):
        cmd = 'systemctl stop ' + self.service +'.service'
        status = commands.getstatusoutput(cmd)[0]
        if status!=0:
            raise commandFailException(cmd, status) 
    
    def enable(self):
        cmd = 'systemctl enable ' + self.service +'.service'
        status = commands.getstatusoutput(cmd)[0]
        if status!=0:
            print status
            raise commandFailException(cmd, status) 
    def disable(self):    
        cmd = 'systemctl disable ' + self.service +'.service'
        status = commands.getstatusoutput(cmd)[0]
        if status!=0:
            raise commandFailException(cmd, status)                      
        
    def test(self):
        cmd = 'systemctl status %s.service '%self.service
        print commands.getstatusoutput(cmd)[1]
        
if __name__ == '__main__':
    try:
        s=serviceCtl('sshd')
        s.enable()
        s.test()
        s.disable()
        s.test()
        s.stop()
        s.test()
        s.start()
        s.enable()
        s.test()
    except commandFailException,e:
        print e.msg
        
    
    
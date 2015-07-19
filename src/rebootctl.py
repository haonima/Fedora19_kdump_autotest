#!/usr/bin/env python
import os
import time
import commands
import servicectl
from envpara import *


def detect():
    step = len(os.walk(PWD+'tmp').next()[1])
    return step 

def mark():
    os.mkdir(PWD+'tmp/'+str(time.time()))

def unmark():
    os.chdir(PWD+'tmp')
    os.rmdir(os.walk(PWD+'tmp').next()[1][0])
    
def unmarkall():
    os.chdir(PWD+'tmp')
    for i in os.walk(PWD+'tmp').next()[1]:
        os.rmdir(i)

def reboot(st):
    #ftest.service should be set to enabled
    #systemctl enable ftest.service 
    #system reboot    
    if st==1:
        mark()
        
    s=servicectl.serviceCtl('ftest')
    s.enable()
    print 'rebooting...'
    
    os.system('reboot')    

def test():
    print detect()
    print 'marking...'
    mark()
    print detect()
    print 'unmarking...'
    unmark()
    print detect()
    print 'marking 3'
    mark()
    mark()
    mark()
    print 'unmarking 1'
    unmark()
    print detect()
    print 'unmarking all'
    print detect()    

if __name__=='__main__':
    print detect()    
    print detect()
    print detect()
    
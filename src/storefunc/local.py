#!/usr/bin/env python
import sys
sys.path.append('..')
import conf
import commands
from exception import *
from envpara import PWD

def local():
    c = conf.conf()
    path = c.getStorePath()
    getFile(path)
   
def copyVmcore(path):
    cmd = 'ls -l '+ path + " |grep d[r-][w-][x-]|sort -n |tail -1|awk '{print $9}'"
    status = commands.getstatusoutput(cmd)
    if status[0] != 0:
        raise commandFailException(cmd,status[0])
    cmd = 'cp ' + path + '/' + status[1] + '/vmcore ' + PWD + 'results/vmcores/vmcore'
    status = commands.getstatusoutput(cmd)
    if status[0] !=0:
        raise commandFailException(cmd,status[0])
    print 'done'
    

def getFile(path):
    copyVmcore(path)
    
def test():
    path = '/home/haoshaoting/k1'
    copyVmcore(path)
    
if __name__ == '__main__':
    try:
        test()
    except commandFailException,e:
        print e.msg
    
    
    
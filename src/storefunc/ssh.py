#!/usr/bin/env python
import commands
import sys
sys.path.append('..')
from exception import *
import conf
from envpara import *
import time

def ssh():
    print 'testing remote server....'
    while 1:
        status = commands.getstatusoutput('systemctl status sshd.service')
        time.sleep(3)
        if status[0]==0:
            break
        
    con=conf.conf()
    ip=con.getStoreStyle()[1]
    path=con.getStorePath()
    getRemoteFile(ip, path)

def nettest(ip):
    cmd = 'ssh '+ip+' ls'
    status = commands.getstatusoutput(cmd)[0]
    if status!=0:
        raise commandFailException(cmd,status)
    else:
        print 'remote server available...'

def copyVmcore(ip,remotedir):
    cmd1= "ssh "+ ip + " ls -l " + remotedir + " |grep d[r-][w-][x-]|sort -n |tail -1|awk '{print $9}'"
    op = commands.getstatusoutput(cmd1)
    if op[0] !=0:
        raise commandFailException(cmd1,op[0])
    cmd = "scp "+ ip + ":" + remotedir +"/" + op[1] + "/vmcore.flat " + PWD + "results/vmcores/vmcore"
    print 'copying vmcore....'
    status = commands.getstatusoutput(cmd)[0]
    if status!=0:
        raise commandFailException(cmd,status)
    print 'done'

def getRemoteFile(ip,remotedir):
    nettest(ip)
    copyVmcore(ip,remotedir)
      
def test():
    nettest('root@10.33.28.9')
    copyVmcore('root@10.33.28.9','/kda')
        
if __name__=='__main__':
    try:
        test()        
    except commandFailException,e:
        print e.msg
import commands
import os
import sys
sys.path.append('..')
from exception import *
import conf
from envpara import *

def nfs():
    print 'testing remote server...'
    con=conf.conf()
    ip=con.getStoreStyle()[1]
    path=con.getStorePath()
    #nettest(ip)
    getRemoteFile(ip,path)
    
def mountnfs(ip,remotedir):
    #nettest(ip)
    print 'mounting remote nfs...'
    
    cmd='mkdir -p /mnt/ftest'
    if not os.path.exists('/mnt/ftest'):
        status=commands.getstatusoutput(cmd)
        if status[0]!=0:
            raise commandFailException(cmd,status)       
    
    cmd = 'mount -t nfs '+ip +' /mnt/ftest'
    status = commands.getstatusoutput(cmd)[0]
    if status!=0:
        raise commandFailException(cmd,status)
    
    cmd = 'mkdir -p /mnt/ftest' + remotedir
    status = commands.getstatusoutput(cmd)[0]
    if status!=0:
        raise commandFailException(cmd,status)    
    
    print 'nfs mount done'
    
def nettest(ip):
    print 'testing remote server...'
    cmd = 'showmount -e ' + ip
    status = commands.getstatusoutput(cmd)
    if status[0] == 0:
        print 'remote server available....'
    else:
        print status[1]
        raise remoteServerException(ip)
    
def copyVmcore(remote):
    cmd = 'cp '+ remote + ' '+PWD+'results/vmcores/vmcore'
    print 'copying remote vmcore from '+ remote
    status = commands.getstatusoutput(cmd)
    if status[0]!=0:
        raise commandFailException(cmd,status[0])
    print 'copy done'
    

def getRemoteFile(ip,remotedir):
    '''
    used to get back the file stored in nfs server
    '''
    print 'retrieving remote server...'
     
    c=conf.conf()
    sto=c.getStorePath()
    
    mountnfs(ip, remotedir)
    
    cmd="ls -l /mnt/ftest/"+sto+"|grep d[r-][w-][x-] |sort -n |tail -1|awk '{print $9}'"
    status=commands.getstatusoutput(cmd)
    if status[0]!=0:
        raise commandFailException(cmd,status)        
    remVmcore = '/mnt/ftest/'+sto+'/'+status[1]+'/vmcore'    
    copyVmcore(remVmcore)    
    print 'get remote file done'
    
    
def test():
    print 'testing remote server...'
    con=conf.conf()
    ip=con.getStoreStyle()[1]
    path=con.getStorePath()
    print ip
    print path
    nettest(ip)
    getRemoteFile(ip,path)
    
        
    
if __name__ == '__main__':
    try:
        test()
    except remoteServerException,e:
        print e.msg
       
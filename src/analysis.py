#!/usr/bin/env python 
'''
This file analysis the vmcore, which use crash command to do that. Users need to
write their commands in ftest.conf.d/cmds.conf to get the output in log directory
'''

'''
1st, pull back the vmcore from remote server
2nd, analysis the vmcore with vmlinux
'''

import commands
import exception
import os
import re

from storefunc import *
from conf import conf
from exception import *
from envpara import *

class analysis:
    def __init__(self,vmlinux):
        self.__vmcore = PWD+'results/vmcores/vmcore'
        self.__vmlinux = vmlinux
        
    def analysis(self):
        #cmd = 'crash -i %sftest.conf.d/cmds.conf %s %s >%sresults/logs/basic.log '%(PWD,self.__vmcore,self.__vmlinux,PWD)
        cmd = 'crash -i %sftest.conf.d/cmds.conf %s %s >/tmp/basic.log '%(PWD,self.__vmcore,self.__vmlinux)
        status = commands.getstatusoutput(cmd)[0]
        if status!=0:
            raise commandFailException(cmd,status)
        
    def log_wash(self):
        fin=open('/tmp/basic.log','r')
        fout=open(PWD+'results/logs/basic.log','w')
        c = fin.read()
        c1=fout.write(c[c.find('KERNEL:'):c.find('crash> exit')])
        fin.close()
        fout.close()
            
        r = re.compile('.+\.ftestlog')
        for i in os.listdir('/tmp/'):
            if r.match(i):
                fin=open('/tmp/'+i,'r')
                fout=open(PWD+'results/logs/'+i,'w')
                a=fin.readlines()
                b=''.join(a[1:])
                fout.write(b)
                fin.close()
                fout.close()
    
def get_vmcore(storestyle):
    d={'nfs':nfs.nfs,'ssh':ssh.ssh,'local':local.local}
    v = d.get(storestyle[0])
    v()
    
def test():
    c=conf()
    a=analysis(c.getVmlinux())
    get_vmcore(c.getStoreStyle()[0])
   # vmcore='/var/crash/127.0.0.1-2014.07.13-18\:23\:21/vmcore'
   # vmlinux='/usr/lib/debug/lib/modules/3.9.5-301.fc19.i686.PAE/vmlinux'
   
    vmlinux = c.getVmlinux()
    an = analysis(vmlinux)
    an.analysis()
    an.log_wash()

if __name__=='__main__':
    test()
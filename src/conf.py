#!/usr/bin/python
import re
import time
import os
from envpara import *

class conf:
    __crash_style=''
    def kdumpConf(self):
        kconf=re.compile('^raw.+|^ext4.+|^nfs.+|^ssh.+|^blacklist.+|^core_collector.+|^kdump_post.+'
                     '|^kdump_pre.+|^extra_bins.+|^extra_modules.+|^default.+|^force_rebuild.+')
        fconf1=re.compile('^crash_style.+')
        fconf2=re.compile('^vmlinux.+')
        storepath=str(time.time())
        with open(PWD+'ftest.conf.d/ftest.conf','r') as f1:
            with open('/etc/kdump.conf','w') as f2:
                for i in f1:
                    if kconf.match(i):
                        f2.writelines(kconf.match(i).group()+'\n')
                    if fconf1.match(i):
                        self.__crash_style=fconf1.match(i).group()
                    if fconf2.match(i):
                        self.__vmlinux=fconf2.match(i).group()
                f2.writelines('path /'+storepath+'\n')
        
        print '"kdump.conf" configure complete!'
            
    def getCrashStyle(self):
        return self.__crash_style.replace('crash_style','').replace(' ','')
    
    def getStoreStyle(self):
        with open('/etc/kdump.conf','r') as f:
            ssh=re.compile('^ssh.+')
            nfs=re.compile('^nfs.+')
            for i in f:
                if ssh.match(i):
                    return 'ssh',ssh.match(i).group().replace('ssh','',1).replace(' ','')
                elif nfs.match(i):
                    return 'nfs',nfs.match(i).group().replace('nfs','',1).replace(' ','')
                else:
                    return 'local',''
    
    def getVmlinux(self):
        with open(PWD+'ftest.conf.d/ftest.conf','r') as f:
            p=re.compile('^vmlinux.+')
            for i in f:
                if p.match(i):
                    return p.match(i).group().replace('vmlinux','',1).replace(' ','')
        
    def getStorePath(self):
        with open('/etc/kdump.conf','r') as f:
            p=re.compile('^path.+')
            for i in f:
                if p.match(i):
                    return p.match(i).group().replace('path','').replace(' ','')
            
        
                
def test():
    c=conf()
    c.kdumpConf()
    print 'getCrashStyle....'
    print c.getCrashStyle()
    print 'getStorePath....'
    print c.getStorePath()
    print 'getvmlinux'
    print c.getVmlinux()
    print 'get storestyle'
    print c.getStoreStyle()    

if __name__ =='__main__':
    test()
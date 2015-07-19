#!/usr/bin/python
import commands
from exception import *
import rebootctl
from platform import release

class env:
    def detectSoftware(self):
        if 'PAE' in release():
            softnecelist = ('kernel-PAE-debuginfo',)
        else:
            softnecelist = ('kernel-debuginfo',)
        softoptlist = ('kexec-tools','crash')
        for i in softnecelist:
            print 'Testing '+i+' ...'
            if i in commands.getstatusoutput('rpm -qa '+ i)[1]:
                print 'done'
            else:
                raise notInstallException(i)
        for i in softoptlist:
            print 'Testing '+i+' ...'
            if i in commands.getstatusoutput('rpm -qa '+ i)[1]:
                print 'done'
            else:
                print 'warning: '+ i +' not installed'    
        print 'software detected done'
                
    def detectCmdline(self):
        print 'Testing the parameters in grub2...'
        cmdfile='/proc/cmdline'
        fcmdline = open(cmdfile,'r')
        with open(cmdfile,'r') as fcmdline:
            if 'crashkernel=' in fcmdline.read():
                print 'cmdline correct'
                return 0
            else:
                print 'parameter "crashkernel" not in cmdline, adding...'
        fr= open('/etc/default/grub','r')
        fw = open('/tmp/grub','w')
        for i in fr:
            if 'GRUB_CMDLINE_LINUX' in i:
                if 'crashkernel=' not in i:
                    print 'adding /"crashkernel/"...'
                    i=i.rstrip()[:-1]+' crashkernel=128M'+i.rstrip()[-1:]+'\n'
            fw.write(i)
        fr.close()
        fw.close()    
        commands.getstatusoutput('mv -f /tmp/grub /etc/default/grub')
        if commands.getstatusoutput('grub2-mkconfig -o /boot/grub2/grub.cfg ')[0] == 0:
            print 'done'    
        return 1
     
    
       
if __name__ == '__main__':
    try:
        en=env()
        print en.detectCmdline()
        en.detectSoftware()
        if en.needreboot==1:
            print 'reboot'
    except notInstallException ,e:
        print e.msg
        exit()
    except cmdlineEeception,e:
        print e.msg
        exit()
    except Exception,e:
        print e
        exit()

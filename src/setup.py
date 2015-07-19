#!/usr/bin/python
# -*- coding: utf8 -*-
import commands
import os
import exception

def installservice():
    #将服务脚本放到/usr/lib/systemd/system/ftest.service
    if commands.getstatusoutput('yes|cp service/ftest.service /usr/lib/systemd/system/ftest.service')[0]!=0:
        raise setupException
    if commands.getstatusoutput('yes|cp service/ftestctl /usr/bin/ftestctl')[0]!=0:
        raise setupException
    print 'service done'
    
def installpro():
    #移动所有文件
    if not os.path.exists('/usr/local/ftest'):
        if commands.getstatusoutput('mkdir -p /usr/local/ftest/')[0]!=0:
            raise setupException

    if commands.getstatusoutput('cp -r * /usr/local/ftest/')[0]!=0:
        raise setupException
    
    if commands.getstatusoutput('yes|cp ftest /usr/bin/ftest')[0]!=0:
        raise setupException
    if commands.getstatusoutput('mkdir -p /usr/local/ftest/tmp')[0]!=0:
        raise setupException
    
    print 'program done'

def permission():
    #为ftest.py赋予chmod +x权限
    if commands.getstatusoutput('chmod +x /usr/local/ftest/ftest')[0]!=0:
        raise setupException
    if commands.getstatusoutput('chmod +x /usr/bin/ftest')[0]!=0:
        raise setupException
    if commands.getstatusoutput('chmod +x /usr/bin/ftestctl')[0]!=0:
        raise setupException
    print 'permission done'



if __name__ == '__main__':
    try:
        installservice()
        installpro()
        permission()
        print 'setup successful'
    except setupException,e :
        print e.msg

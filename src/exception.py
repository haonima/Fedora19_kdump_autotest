#class that if the necessary software is not installed
class notInstallException(Exception):
    def __init__(self,soft):
        self.msg = soft + ' is not installed, please install it first, exiting...'

#class that move or new the conf file failed
class conffileException(Exception):
    def __init__(self,op):
        self.msg = op + ' failed, exiting...'

#class that remote server not available
class remoteServerException(Exception):
    def __init__(self,ip):
        self.msg = 'remote server '+ip+' is not available, exiting...'

#class that command start fail
class commandFailException(Exception):
    def __init__(self, cmd ,status):
        self.msg = 'command \n\"' + cmd + '\"\nfailed, error code '+ str(status)

#class that setup error
class setupException(Exception):
    msg = ''
    def __init__(self):
        self.msg = 'setup error'

#class that cmdline error
class cmdlineEeception(Exception):
    msg=''
    def __init__(self):
        self.msg = 'the cmdline is not correct for this testing'

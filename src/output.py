#!/usr/bin/env python 
import sys
from envpara import SERIAL

def serial_print(string):
    sys.stdout=open(SERIAL,'w')
    print '\n'+'*'*20+'\n'+string+'\n'+'*'*20
    
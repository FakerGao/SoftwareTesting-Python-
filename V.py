# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import re
class V(object):

    def getFunc(self,code,line):
        count=0
        func=''
        for i in range(int(line),len(code)+1):
            count=count+code[i-1].count('{')
            count=count-code[i-1].count('}')
            if count or i==int(line):
                func=func+' '+code[i-1]
            else:
                end=i
                break
        return func

    def VG(self,func):
        com=0
        #短路情况时，没出现一个||环形复杂度则+1
        p=re.compile(r'(if|elseif)\s*\(\S+?\)')
        for m in p.finditer(func):
            com=com+m.group().count('||')+1
        p=re.compile(r'while\s*\(\S+?\)')
        for n in p.finditer(func):
            str=n.group().strip()
            str=str.strip('while()')
            if not str.isdigit():
                com=com+1
        com=com+func.count('for')
        com=com+func.count('case')
        return com+1
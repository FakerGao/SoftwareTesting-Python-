# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import re
class CheckName(object):
        #查找所有的类名
    def CheckClass(self,code):   #\bclass\s+([\w\d_]+)\s*
        templist=[]
        number=[]
        classlist=[]
        p=re.compile(r'\bclass\s+([\w\d_]+)\s*')
        for i in range(len(code)):
            for m in p.finditer(code[i]):
                templist.append(m.group())
                if m:
                    number.append(i+1)
        for j in range(len(templist)):
            line=[]
            print templist[j]
            temp=re.split(' ',templist[j])
            while ''in temp:
                temp.remove('')
            if temp[1][:3].isupper() and temp[1][3:].islower():
                correct= u"√"
                suggestion=""
            else:
                correct=u"×"
                suggestion=temp[1][:3].upper()+temp[1][3:].lower()
            line.append("Class")
            line.append("")
            line.append(temp[1])
            line.append(str(number[j]))
            line.append(correct)
            line.append(suggestion)
            classlist.append(line)
        return classlist

        #查找所有的函数名
    def CheckFun(self,code):#\b(void|int|float|char|string|double|boolean|short|long|byte)\s+.+(\();
        templist=[]
        number=[]
        FunList=[]
        typename=''
        typename=self.TypeDef(code)
        p=re.compile(r'\b(void|public|String|ArrayList|int|float|char|string|double|boolean|short|long|byte{0})\s+\S+((\()|\s+(\())'.format(typename))
        for i in range(len(code)):
            for m in p.finditer(code[i]):
                templist.append(m.group())
                if m:
                    number.append(i+1)
        for j in range(len(templist)):
            temp=re.split(' |\n',templist[j][:-1])
            line=[]
            line.append("Function")
            line.append(temp[0])
            line.append(temp[1])
            line.append(str(number[j]))
            check=re.match(r'\bF_\S+\b',temp[1])
            if check or temp[1]=='main':
                correct= u"√"
                suggestion=""
            else:
                correct=u"×"
                suggestion="F_"+temp[1].lower()
            line.append(correct)
            line.append(suggestion)
            FunList.append(line)
        return FunList


        #查找所有的变量名
    def CheckVar(self,code):#\b(void|int|float|char|string|double|boolean|short|long|byte)((\s+.+?;)|(\s+.+))
        templist=[]
        number=[]
        varlist=[]
        typename=''
        typename=self.TypeDef(code)
        p=re.compile(r'(\b(int|float|char|string|double|boolean|short|long|byte{0})\s+.+?;)|(\((int|float|char|string|double|boolean|short|long|byte{0})\s+[a-zA-z_0-9=]+)|(,(int|float|char|string|double|boolean|short|long|byte{0})\s+.+?)'.format(typename))
        for i in range(len(code)):
            for m in p.finditer(code[i]):
                s=m.group()
                s=s.strip(',(')
                templist.append(s)
                if m:
                    number.append(i+1)
        for j in range(len(templist)):
            temp=re.split(' |,|;',templist[j])
            while '' in temp:
                temp.remove('')
            for m in range(1, len(temp)):
                line=[]
                if '=' in temp[m]:
                    index=temp[m].find('=',0)
                    temp[m]=temp[m][:index]
                    #if temp[m].isalnum():
                line.append("Variable")
                line.append(temp[0])
                line.append(temp[m])
                line.append(str(number[j]))
                check=re.match(r'\b[a-z][A-Z_]+\b',temp[m])
                if check or len(temp[m])==1:
                    correct=u"√"
                    suggestion=""
                else:
                    correct=u"×"
                    suggestion=temp[m][:1].lower()+temp[m][1:].upper()
                line.append(correct)
                line.append(suggestion)
                varlist.append(line)
        return varlist
    def TypeDef(self,code):
        tdlist=[]
        typename=''
        p=re.compile(r'typedef\s+[a-zA-Z0-9_,]+;')
        for i in range(len(code)):
            for m in p.finditer(code[i]):
                s=m.group()
                s=s.strip(';')
                tdlist=re.split(r',| ',s)
                while '' in tdlist:
                    tdlist.remove('')
                while 'typedef' in tdlist:
                    tdlist.remove('typedef')
                for i in range(len(tdlist)):
                    typename=typename+'|'+tdlist[i]
        return typename
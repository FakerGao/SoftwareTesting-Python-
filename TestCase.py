# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import re
import itertools

class TestCase(object):
    #生成决策表
    def create(self,condition):
        each=re.split('\|\||\&\&|\(|\)',condition)
        while '' in each:
            each.remove('')
        result=[]
        var=[]
        correct=[]
        error=[]
        rco=condition
        rer=condition
        for i in range(len(each)):
            if '==' in each[i]:
                var.append(re.split('==',each[i])[0])
                correct.append(int(re.split('==',each[i])[1]))
                error.append(int(re.split('==',each[i])[1])+1)
            elif '!=' in each[i]:
                var.append(re.split('!=',each[i])[0])
                correct.append(int(re.split('!=',each[i])[1])+1)
                error.append(int(re.split('!=',each[i])[1]))
            elif '!' in each[i]:
                var.append(each[i].strip('!'))
                correct.append(0)
                error.append(1)
                rer=re.sub('!',' not ',rer)
                rco=re.sub('!',' not ',rco)
            elif '>=' in each[i]:
                var.append(re.split('>=',each[i])[0])
                correct.append(int(re.split('>=',each[i])[1]))
                error.append(int(re.split('>=',each[i])[1])-1)
            elif '<=' in each[i]:
                var.append(re.split('<=',each[i])[0])
                correct.append(int(re.split('<=',each[i])[1]))
                error.append(int(re.split('<=',each[i])[1])+1)
            elif '>' in each[i]:
                var.append(re.split('>',each[i])[0])
                correct.append(int(re.split('>',each[i])[1])+1)
                error.append(int(re.split('>',each[i])[1]))
            elif '<' in each[i]:
                var.append(re.split('<',each[i])[0])
                correct.append(int(re.split('<',each[i])[1])-1)
                error.append(int(re.split('<',each[i])[1]))
            else:
                var.append(each[i])
                correct.append(1)
                error.append(0)
            rco=re.sub(r'\b{0}\b'.format(var[i]),str(correct[i]),rco)
            rer=re.sub(r'\b{0}\b'.format(var[i]),str(error[i]),rer)
        var.append(condition)
        rco=re.sub('\|\|',' or ',rco)
        rco=re.sub('\&\&',' and ',rco)
        rer=re.sub('\|\|',' or ',rer)
        rer=re.sub('\&\&',' and ',rer)
        correct.append(eval(rco))
        error.append(eval(rer))
        result.append(var)
        result.append(correct)
        result.append(error)
        return result
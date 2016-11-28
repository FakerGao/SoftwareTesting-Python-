# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import re
import itertools

class DecisionTable(object):
    #生成决策表
    def create(self,condition):
        each=re.split('\|\||\&\&|\(|\)',condition)
        while '' in each:
            each.remove('')
        result=[]
        result.append(each)
        for i in itertools.product('01',repeat=len(each)):
            temp=condition
            templist=[]
            for j in range(len(each)):
                temp=re.sub(r'\b{0}\b'.format(each[j]),i[j],temp)
                templist.append(i[j])
            temp=re.sub('\|\|',' or ',temp)
            temp=re.sub('\&\&',' and ',temp)
            templist.append(str(eval(temp)))
            result.append(templist)
        return result

    #优化决策表
    def optimize(self,list):
        r=[]
        w=[]
        for i in range(1,len(list)):
            if list[i][-1]=='1':
                r.append(list[i][-1])
            if lsit[i][-1]=='0':
                w.append(lsit[i][-1])

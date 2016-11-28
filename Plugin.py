# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import re
class Plugin(object):
    #code为read()方法读取的文件
    def Handle(self,code):#((if|while|for)\s*\([a-zA-Z0-9_\|\&\[\]\(\);+\-*/=<>]+\)\s*([a-zA-Z0-9\|\&\[\]\(\)+\-*/=]+);)
        templist=[]
        copylist=[]
        count=0
        p=re.compile(r'((if|while|for)\s*\([a-zA-Z0-9_\|\&\[\]\(\);+\-*/=<>\s]+\)\s*([a-zA-Z0-9\|\&\[\]\(\)+\-*/=]+);)|(else\s+[a-zA-Z0-9+\-*/_\(\)=]+;)')
        for m in p.finditer(code):
            templist.append(m.group())
            copylist.append(m.group())
        for i in range(len(templist)):
            templist[i]=templist[i]+'}'
            if 'else' in templist[i]:
                templist[i]=re.sub(r'\belse\b','else{',templist[i])
            else:
                for j in range(len(templist[i])):
                    if templist[i][j]=='(':
                        count=count+1
                    elif templist[i][j]==')':
                        count=count-1
                        if count==0:
                            templist[i]=templist[i][:j+1]+'{'+templist[i][j+2:]
                        break
            code=code.replace(copylist[i],templist[i])
        return code
    def Plug(self,var,type,code):
        pluglist=[]
        code=self.Handle(code)
        if(type=="int"):
            tp="%d"
        elif(type=="float" or type=="double"):
            tp="%f"
        elif(type=="char"):
            tp="%c"
        elif(type=="string"):
            tp="%s"
        elif(type=="long"):
            tp="%ld"
        exp="(({|}|;)\s*"+var+"(\+|\-).=[\s\S]+?;)|("+var+"\+\+;)|(\+\+"+var+";)|(\-\-"+var+";)|("+var+"\-\-;)|([a-zA-Z0-9]+\("+var+"\);)"
        p=re.compile(exp)
        for m in p.finditer(code):
            pluglist.append(m.group())
        for i in range(len(pluglist)):
            plug='{0}printf("{1} Plugin-Node {2}:{3}\\n",{2});'.format(pluglist[i],str(i+1),var,tp)
            #pluglist[i]+'printf("'+var+':'+tp+'\n",'+var+');'
            code=code.replace(pluglist[i],plug)
        return code
    def Save(self,ctext,path):
        opath=path[::-1]
        for i in range(len(opath)):
            if opath[i]=='.':
                temp=opath[0:i]+'.gulp_'+opath[i+1:]
                break
        filename=temp[::-1]
        output = open(filename, 'w+')
        output.write(str(ctext))
        output.close()

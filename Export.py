# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import xlwt
class Export(object):
    def Export(self,filename,UItable,sheet):

        savefile=str(filename).decode("utf8")
        #创建excel
        wb=xlwt.Workbook()
        #添加sheet表
        ws=wb.add_sheet(sheet)
        # 遍历Table插值
        for i in range(UItable.rowCount()):
            for j in range(UItable.columnCount()):
                # 当原表格内容为空时要处理
                if UItable.item(i,j)==None:
                    ws.write(i, j," ")
                else:
                    ws.write(i, j,str(UItable.item(i,j).text()).decode("utf8"))
        wb.save(savefile)
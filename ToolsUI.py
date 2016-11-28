# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python\PythonApplication\untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import re
from CheckName import CheckName
from V import V
from Plugin import Plugin
from DecisionTable import DecisionTable
from TestCase import TestCase
from Export import Export
#from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import xlwt
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(539, 434)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/Wrench_tool_32px_1194098_easyicon.net.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.path_1 = QtGui.QLineEdit(self.tab)
        self.path_1.setObjectName(_fromUtf8("path_1"))
        self.horizontalLayout_3.addWidget(self.path_1)
        self.open_1 = QtGui.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/open_16px_1154738_easyicon.net.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_1.setIcon(icon1)
        self.open_1.setObjectName(_fromUtf8("open_1"))
        self.horizontalLayout_3.addWidget(self.open_1)
        self.start_1 = QtGui.QPushButton(self.tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/Start_16px_1178731_easyicon.net.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_1.setIcon(icon2)
        self.start_1.setObjectName(_fromUtf8("start_1"))
        self.horizontalLayout_3.addWidget(self.start_1)
        self.replace_1 = QtGui.QPushButton(self.tab)
        iconr = QtGui.QIcon()
        iconr.addPixmap(QtGui.QPixmap(_fromUtf8("img/replace_16px_534846_easyicon.net.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.replace_1.setIcon(iconr)
        self.replace_1.setObjectName(_fromUtf8("replace_1"))
        self.horizontalLayout_3.addWidget(self.replace_1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.code_1 = QtGui.QTextEdit(self.tab)
        self.code_1.setObjectName(_fromUtf8("code_1"))
        self.horizontalLayout_4.addWidget(self.code_1)
        self.result_1 = QtGui.QTableWidget(self.tab)
        self.result_1.setObjectName(_fromUtf8("result_1"))
        self.result_1.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)  #整行选中的方式
        self.result_1.setColumnCount(6)
        self.result_1.setAlternatingRowColors(True)
        self.horizontalLayout_4.addWidget(self.result_1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.export_code=QtGui.QPushButton(self.tab)
        icone=QtGui.QIcon()
        icone.addPixmap(QtGui.QPixmap(_fromUtf8("img/save_floppy_16px_1187937_easyicon.net.png")),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_code.setIcon(icone)
        self.export_code.setObjectName(_fromUtf8("export_code"))
        self.horizontalLayout_5.addWidget(self.export_code)
        self.export_1 = QtGui.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("img/export_outline_16px_1158606_easyicon.net.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_1.setIcon(icon3)
        self.export_1.setObjectName(_fromUtf8("export_1"))
        self.horizontalLayout_5.addWidget(self.export_1)
        self.close_1 = QtGui.QPushButton(self.tab)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("img/x_close_16px_1194532_easyicon.net.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_1.setIcon(icon4)
        self.close_1.setObjectName(_fromUtf8("close_1"))
        self.horizontalLayout_5.addWidget(self.close_1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.path_2 = QtGui.QLineEdit(self.tab_2)
        self.path_2.setObjectName(_fromUtf8("path_2"))
        self.horizontalLayout_7.addWidget(self.path_2)
        self.open_2 = QtGui.QPushButton(self.tab_2)
        self.open_2.setIcon(icon1)
        self.open_2.setObjectName(_fromUtf8("open_2"))
        self.horizontalLayout_7.addWidget(self.open_2)
        self.start_2 = QtGui.QPushButton(self.tab_2)
        self.start_2.setIcon(icon2)
        self.start_2.setObjectName(_fromUtf8("start_2"))
        self.horizontalLayout_7.addWidget(self.start_2)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.code_2 = QtGui.QTextEdit(self.tab_2)
        self.code_2.setObjectName(_fromUtf8("code_2"))
        self.horizontalLayout_8.addWidget(self.code_2)
        self.result_2 = QtGui.QTableWidget(self.tab_2)
        self.result_2.setObjectName(_fromUtf8("result_2"))
        self.result_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)  #整行选中的方式
        self.result_2.setColumnCount(5)
        self.result_2.setAlternatingRowColors(True)
        self.horizontalLayout_8.addWidget(self.result_2)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.export_2 = QtGui.QPushButton(self.tab_2)
        self.export_2.setIcon(icon3)
        self.export_2.setObjectName(_fromUtf8("export_2"))
        self.horizontalLayout_9.addWidget(self.export_2)
        self.close_2 = QtGui.QPushButton(self.tab_2)
        self.close_2.setIcon(icon4)
        self.close_2.setObjectName(_fromUtf8("close_2"))
        self.horizontalLayout_9.addWidget(self.close_2)
        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.path_3 = QtGui.QLineEdit(self.tab_3)
        self.path_3.setObjectName(_fromUtf8("path_3"))
        self.horizontalLayout.addWidget(self.path_3)
        self.open_3 = QtGui.QPushButton(self.tab_3)
        self.open_3.setIcon(icon1)
        self.open_3.setObjectName(_fromUtf8("open_3"))
        self.horizontalLayout.addWidget(self.open_3)
        self.search = QtGui.QPushButton(self.tab_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("img/search_16px_1197039_easyicon.net.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon5)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout.addWidget(self.search)
        self.start_3 = QtGui.QPushButton(self.tab_3)
        self.start_3.setIcon(icon2)
        self.start_3.setObjectName(_fromUtf8("start_3"))
        self.horizontalLayout.addWidget(self.start_3)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.code_3 = QtGui.QTextEdit(self.tab_3)
        self.code_3.setObjectName(_fromUtf8("code_3"))
        self.horizontalLayout_16.addWidget(self.code_3)
        self.result_3 = QtGui.QTableWidget(self.tab_3)
        self.result_3.setObjectName(_fromUtf8("result_3"))
        self.result_3.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)  #整行选中的方式
        self.result_3.setColumnCount(4)
        self.result_3.setAlternatingRowColors(True)
        self.horizontalLayout_16.addWidget(self.result_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_16, 1, 0, 1, 1)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.export_3 = QtGui.QPushButton(self.tab_3)
        self.export_3.setIcon(icon3)
        self.export_3.setObjectName(_fromUtf8("export_3"))
        self.horizontalLayout_17.addWidget(self.export_3)
        iconex = QtGui.QIcon()
        iconex.addPixmap(QtGui.QPixmap(_fromUtf8("img/Execute_16px_1064493_easyicon.net.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exe_1 = QtGui.QPushButton(self.tab_3)
        self.exe_1.setIcon(iconex)
        self.exe_1.setObjectName(_fromUtf8("exe_1"))
        self.horizontalLayout_17.addWidget(self.exe_1)
        self.close_3 = QtGui.QPushButton(self.tab_3)
        self.close_3.setIcon(icon4)
        self.close_3.setObjectName(_fromUtf8("close_3"))
        self.horizontalLayout_17.addWidget(self.close_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_18.addWidget(self.label_6)
        self.condition_1 = QtGui.QLineEdit(self.tab_4)
        self.condition_1.setObjectName(_fromUtf8("condition_1"))
        self.horizontalLayout_18.addWidget(self.condition_1)
        self.start_4 = QtGui.QPushButton(self.tab_4)
        self.start_4.setIcon(icon2)
        self.start_4.setObjectName(_fromUtf8("start_4"))
        self.horizontalLayout_18.addWidget(self.start_4)
        #self.optimize_1 = QtGui.QPushButton(self.tab_4)
        #icon5 = QtGui.QIcon()
        #icon5.addPixmap(QtGui.QPixmap(_fromUtf8("img/start_favorite_16px_1187948_easyicon.net.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.optimize_1.setIcon(icon5)
        #self.optimize_1.setObjectName(_fromUtf8("optimize_1"))
       # self.horizontalLayout_18.addWidget(self.optimize_1)
        self.gridLayout_4.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.table_1 = QtGui.QTableWidget(self.tab_4)
        self.table_1.setObjectName(_fromUtf8("table_1"))
        self.horizontalLayout_19.addWidget(self.table_1)
        self.gridLayout_4.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        #self.table_2 = QtGui.QTableWidget(self.tab_4)
        #self.table_2.setObjectName(_fromUtf8("table_2"))
        #self.table_2.setColumnCount(0)
        #self.table_2.setRowCount(0)
        #self.horizontalLayout_20.addWidget(self.table_2)
        #self.gridLayout_4.addLayout(self.horizontalLayout_20, 2, 0, 1, 1)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.export_4 = QtGui.QPushButton(self.tab_4)
        self.export_4.setIcon(icon3)
        self.export_4.setObjectName(_fromUtf8("export_4"))
        self.horizontalLayout_21.addWidget(self.export_4)
        self.close_6 = QtGui.QPushButton(self.tab_4)
        self.close_6.setIcon(icon4)
        self.close_6.setObjectName(_fromUtf8("close_6"))
        self.horizontalLayout_21.addWidget(self.close_6)
        self.gridLayout_4.addLayout(self.horizontalLayout_21, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_7 = QtGui.QLabel(self.tab_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_22.addWidget(self.label_7)
        self.condition_2 = QtGui.QLineEdit(self.tab_5)
        self.condition_2.setObjectName(_fromUtf8("condition_2"))
        self.horizontalLayout_22.addWidget(self.condition_2)
        self.start_5 = QtGui.QPushButton(self.tab_5)
        self.start_5.setIcon(icon2)
        self.start_5.setObjectName(_fromUtf8("start_5"))
        self.horizontalLayout_22.addWidget(self.start_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.table_3 = QtGui.QTableWidget(self.tab_5)
        self.table_3.setObjectName(_fromUtf8("table_3"))
        self.horizontalLayout_23.addWidget(self.table_3)
        self.gridLayout_5.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.export_5 = QtGui.QPushButton(self.tab_5)
        self.export_5.setIcon(icon3)
        self.export_5.setObjectName(_fromUtf8("export_5"))
        self.horizontalLayout_24.addWidget(self.export_5)
        self.close_5 = QtGui.QPushButton(self.tab_5)
        self.close_5.setIcon(icon4)
        self.close_5.setObjectName(_fromUtf8("close_5"))
        self.horizontalLayout_24.addWidget(self.close_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_24, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.open_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openfile)
        QtCore.QObject.connect(self.start_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.started)
        QtCore.QObject.connect(self.replace_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Rep)
        QtCore.QObject.connect(self.export_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.export)
        QtCore.QObject.connect(self.export_code, QtCore.SIGNAL(_fromUtf8("clicked()")), self.exportcode1)
        QtCore.QObject.connect(self.close_1, QtCore.SIGNAL(_fromUtf8("clicked()")),self.close)
        QtCore.QObject.connect(self.open_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openfile2)
        QtCore.QObject.connect(self.start_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calculate)
        QtCore.QObject.connect(self.export_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.export2)
        QtCore.QObject.connect(self.close_2, QtCore.SIGNAL(_fromUtf8("clicked()")),self.close)
        QtCore.QObject.connect(self.open_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openfile3)
        QtCore.QObject.connect(self.search, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchvar)
        QtCore.QObject.connect(self.start_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plugin)
        QtCore.QObject.connect(self.export_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.exportcode)
        QtCore.QObject.connect(self.exe_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.execute)
        QtCore.QObject.connect(self.close_3, QtCore.SIGNAL(_fromUtf8("clicked()")),self.close)
        QtCore.QObject.connect(self.start_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.createtable)
        QtCore.QObject.connect(self.export_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.export4)
        QtCore.QObject.connect(self.close_6, QtCore.SIGNAL(_fromUtf8("clicked()")),self.close)
        QtCore.QObject.connect(self.start_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.testcase)
        QtCore.QObject.connect(self.export_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.export5)
        QtCore.QObject.connect(self.close_5, QtCore.SIGNAL(_fromUtf8("clicked()")),self.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "测试工具", None))
        self.label.setText(_translate("MainWindow", "选择文件", None))
        self.open_1.setText(_translate("MainWindow", "打开..", None))
        self.start_1.setText(_translate("MainWindow", "检测", None))
        self.replace_1.setText(_translate("MainWindow", "替换所有", None))
        self.export_code.setText(_translate("MainWindow", "保存代码", None))
        self.export_1.setText(_translate("MainWindow", "导出结果", None))
        self.close_1.setText(_translate("MainWindow", "关闭", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "命名规则检测", None))
        self.label_2.setText(_translate("MainWindow", "选择文件", None))
        self.open_2.setText(_translate("MainWindow", "打开..", None))
        self.start_2.setText(_translate("MainWindow", "计算", None))
        self.export_2.setText(_translate("MainWindow", "导出结果", None))
        self.close_2.setText(_translate("MainWindow", "关闭", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "环形复杂度", None))
        self.label_5.setText(_translate("MainWindow", "选择文件", None))
        self.open_3.setText(_translate("MainWindow", "打开..", None))
        self.search.setText(_translate("MainWindow", "查找变量", None))
        self.start_3.setText(_translate("MainWindow", "插装", None))
        self.export_3.setText(_translate("MainWindow", "保存", None))
        self.exe_1.setText(_translate("MainWindow", "执行", None))
        self.close_3.setText(_translate("MainWindow", "关闭", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "程序插装", None))
        self.label_6.setText(_translate("MainWindow", "判定条件", None))
        self.start_4.setText(_translate("MainWindow", "生成", None))
        #self.optimize_1.setText(_translate("MainWindow", "优化", None))
        self.export_4.setText(_translate("MainWindow", "导出到Excel", None))
        self.close_6.setText(_translate("MainWindow", "关闭", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "决策表生成", None))
        self.label_7.setText(_translate("MainWindow", "判定条件", None))
        self.start_5.setText(_translate("MainWindow", "生成", None))
        self.export_5.setText(_translate("MainWindow", "导出到Excel", None))
        self.close_5.setText(_translate("MainWindow", "关闭", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "测试用例生成", None))
    '''
    检查命名规则部分
    '''

    def openfile(self):
        self.replace_1.setText(_translate("MainWindow", "替换所有", None))
        s=QFileDialog.getOpenFileName(self,"Open file dialog","/","Java File(*.java);;C++ File(*.cpp);;C++ Head File(*.h);;All File(*.*)")
        self.path_1.setText(self.tr(str(s)))
        print(s)
        f=open(s,'r')
        global code
        code = f.readlines()
        f.close
        global showtext
        showtext=''
        for i in range(len(code)):
            showtext=showtext+code[i]
        self.code_1.setText(unicode(showtext, 'GBK', 'ignore'))
        f.close
    def started(self):
        self.result_1.clear()
        self.result_1.setHorizontalHeaderLabels(["ObjectModel","Type","Name","Location","Correct","Suggestion"])
        global showlist
        showlist=[]
        colortext=''
        for i in range(len(code)):
            colortext=showtext+code[i]
        che=CheckName()
        showlist.extend(che.CheckClass(code))
        showlist.extend(che.CheckFun(code))
        showlist.extend(che.CheckVar(code))
        self.result_1.setRowCount(len(showlist))
        for i in range(len(showlist)):
            '''
            if showlist[i][-1]!='':
                colortext=re.sub(r'\b{0}\b'.format(showlist[i][2]),"<html><font color=red>"+showlist[i][2]+"</font></html>",colortext)
            else:
                colortext=re.sub(r'\b{0}\b'.format(showlist[i][2]),'<font color=green>'+showlist[i][2]+'</font>',colortext)
                '''
            for j in range(0,6):
                self.result_1.setItem(i, j, QtGui.QTableWidgetItem(showlist[i][j]))
        #self.code_1.setText(self.tr(colortext))
        print type(self.tr(colortext))
    flag=0
    def Rep(self):
        showtext=''
        for i in range(len(code)):
            showtext=showtext+code[i]
        if Ui_MainWindow.flag==0:
            Ui_MainWindow.flag=1
            for i in range(len(showlist)):
                if showlist[i][-1]!='':
                    if showlist[i][0]=='Class':
                        showtext=re.sub(r'\b{0}\b'.format(showlist[i][2]),showlist[i][-1],showtext)
                    if showlist[i][0]=='Function':
                        showtext=re.sub(r'\b{0}\b'.format(showlist[i][2]),showlist[i][-1],showtext)
                    if showlist[i][0]=='Variable':
                        showtext=re.sub(r'\b{0}\b'.format(showlist[i][2]),showlist[i][-1],showtext)
            self.replace_1.setText(_translate("MainWindow", "撤销", None))
        else:
            Ui_MainWindow.flag=0
            for i in range(len(showlist)):
                if showlist[i][-1]!='':
                    if showlist[i][0]=='Class':
                        showtext=re.sub(r'\b{0}\b'.format(showlist[i][-1]),showlist[i][2],showtext)
                    if showlist[i][0]=='Function':
                        showtext=re.sub(r'\b{0}\b'.format(showlist[i][-1]),showlist[i][2],showtext)
                    if showlist[i][0]=='Variable':
                        showtext=re.sub(r'\b{0}\b'.format(showlist[i][-1]),showlist[i][2],showtext)
            self.replace_1.setText(_translate("MainWindow", "替换所有", None))
        self.code_1.setText(unicode(showtext, 'GBK', 'ignore'))
    def exportcode1(self):
        filename = QFileDialog.getSaveFileName(self,self.tr("保存到"),self.tr('New File'),self.tr('Java File(*.java);;C++ File(*.cpp);;C++ Head File(*.h);;C File(*.c)'))
        savefile=str(filename).decode("utf8")
        try:
            output = open(savefile, 'w+')
            output.write(str(self.code_1.toPlainText()))
            output.close()
            QMessageBox.information(self,"Messgae:",
                                    self.tr("保存成功!"))
        except Exception,e:
            QMessageBox.information(self,"Messgae:",
                                    self.tr("保存失败!"))
    def export(self):
        head='The Rule detection of '+re.split('/',self.path_1.text())[-1]
        filename = QFileDialog.getSaveFileName(self,self.tr("保存到"),self.tr('New Microsoft Excel File.xls'),self.tr('Excel File(*.xls)'))
        savefile=str(filename).decode("utf8")
        #创建excel
        wb=xlwt.Workbook()
        #添加sheet表
        ws=wb.add_sheet(u'命名规则检测')
        font1=xlwt.Font()
        style1=xlwt.XFStyle()
        font1.name='Times New Roman'
        font1.bold=True
        font1.colour_index=2
        font1.height=0xF0
        style1.font=font1
        ws.write_merge(0, 0,0,5,str(head).decode("gbk"),style1)
        pattern=xlwt.Pattern()
        style=xlwt.XFStyle()
        pattern.pattern=pattern.SOLID_PATTERN
        pattern.pattern_fore_colour=3
        style.pattern=pattern
        ws.write(1, 0,str('ObjectModel').decode("utf8"),style)
        ws.write(1, 1,str('Type').decode("utf8"),style)
        ws.write(1, 2,str('Name').decode("utf8"),style)
        ws.write(1, 3,str('Location').decode("utf8"),style)
        ws.write(1, 4,str('Correct').decode("utf8"),style)
        ws.write(1, 5,str('Suggestion').decode("utf8"),style)
        # 遍历Table插值
        for i in range(2,self.result_1.rowCount()+2):
            for j in range(self.result_1.columnCount()):
                # 当原表格内容为空时要处理
                if self.result_1.item(i-2,j)==None:
                    ws.write(i, j," ")
                else:
                    ws.write(i, j,str(self.result_1.item(i-2,j).text()).decode("utf8"))
        wb.save(savefile)


    '''
    计算环形复杂度
    '''
    def openfile2(self):
        s=QFileDialog.getOpenFileName(self,"Open file dialog","/","C File(*.c);;Head File(*.h);;Java File(*.java);;All File(*.*)")
        self.path_2.setText(self.tr(str(s)))
        print(s)
        f=open(s,'r')
        global text
        text=f.readlines()
        f.close()
        showtext=''
        for i in range(len(text)):
            showtext=showtext+text[i]
        self.code_2.setText(unicode(showtext, 'GBK', 'ignore'))
        f.close
    #计算环形复杂度
    #按行读取文件
    def calculate(self):
        self.result_2.clear()
        self.result_2.setHorizontalHeaderLabels(["ObjectModel","Type","Name","Location","V(G)"])
        showlist=[]
        che=CheckName()
        v=V()
        showlist.extend(che.CheckFun(text))
        self.result_2.setRowCount(len(showlist))
        for i in range(len(showlist)):
            for j in range(0,4):
                self.result_2.setItem(i, j, QtGui.QTableWidgetItem(showlist[i][j]))
            func=v.getFunc(text,showlist[i][3])
            vg=str(v.VG(func))
            self.result_2.setItem(i,4, QtGui.QTableWidgetItem(vg))
    def export2(self):
        head="The Founctions' Ring Complexities of "+re.split('/',self.path_2.text())[-1]
        filename = QFileDialog.getSaveFileName(self,self.tr("保存到"),self.tr('New Microsoft Excel File.xls'),self.tr('Excel File(*.xls)'))
        savefile=str(filename).decode("utf8")
        #创建excel
        wb=xlwt.Workbook()
        #添加sheet表
        ws=wb.add_sheet(u'环形复杂度')
        font1=xlwt.Font()
        style1=xlwt.XFStyle()
        font1.name='Times New Roman'
        font1.bold=True
        font1.colour_index=2
        font1.height=0xF0
        style1.font=font1
        ws.write_merge(0, 0,0,4,str(head).decode("gbk"),style1)
        pattern=xlwt.Pattern()
        style=xlwt.XFStyle()
        pattern.pattern=pattern.SOLID_PATTERN
        pattern.pattern_fore_colour=3
        style.pattern=pattern
        ws.write(1, 0,str('ObjectModel').decode("utf8"),style)
        ws.write(1, 1,str('Type').decode("utf8"),style)
        ws.write(1, 2,str('Name').decode("utf8"),style)
        ws.write(1, 3,str('Location').decode("utf8"),style)
        ws.write(1, 4,str('V(G)').decode("utf8"),style)
        # 遍历Table插值
        for i in range(2,self.result_2.rowCount()+2):
            for j in range(self.result_2.columnCount()):
                # 当原表格内容为空时要处理
                if self.result_2.item(i-2,j)==None:
                    ws.write(i, j," ")
                else:
                    ws.write(i, j,str(self.result_2.item(i-2,j).text()).decode("utf8"))
        wb.save(savefile)
    '''
        插装
    '''
    def openfile3(self):
        s=QFileDialog.getOpenFileName(self,"Open file dialog","/","C File(*.c);;Head File(*.h);;Java File(*.java);;All File(*.*)")
        self.path_3.setText(self.tr(str(s)))
        print(s)
        f=open(s,'r')
        global codelist
        f=open(s,'r')
        codelist=f.readlines()
        f.close()
        global code3
        code3=''
        for i in range(len(codelist)):
            code3=code3+codelist[i]
        self.code_3.setText(unicode(code3, 'GBK', 'ignore'))
        f.close

    #查找变量
    def searchvar(self):
        self.result_3.clear()
        self.result_3.setHorizontalHeaderLabels(["ObjectModel","Type","Name","Location"])
        global vlist
        vlist=[]
        che=CheckName()
        vlist.extend(che.CheckVar(codelist))
        self.result_3.setRowCount(len(vlist))
        for i in range(len(vlist)):
            for j in range(0,4):
                self.result_3.setItem(i, j, QtGui.QTableWidgetItem(vlist[i][j]))
    #对变量进行插装
    #读取文件结果以string格式存放
    def plugin(self):
        self.result_3.setFocusPolicy(QtCore.Qt.NoFocus)
        row=self.result_3.currentRow()
        var=vlist[row][2]
        vartype=vlist[row][1]
        pl=Plugin()
        global text
        text=pl.Plug(var,vartype,code3)
        self.code_3.setText(unicode(text, 'GBK', 'ignore'))
    #保存插装结果
    def exportcode(self):
        try:
            p=Plugin()
            path=self.path_3.text()
            p.Save(text,path)
            QMessageBox.information(self,"Messgae:",
                                    self.tr("保存成功!"))
        except Exception,e:
            QMessageBox.information(self,"Messgae:",
                                    self.tr("保存失败!"))
    #执行插装结果
    def execute(self):
        for i in range(len(self.path_3.text()[::-1])):
            if self.path_3.text()[::-1][i]=='.':
                temp=self.path_3.text()[::-1][0:i]+'.gulp_'+self.path_3.text()[::-1][i+1:]
                exe='exe.gulp_'+str(self.path_3.text())[::-1][i+1:]
                break
        filename=temp[::-1]
        exe=re.split(r'/',exe[::-1])[-1]
        if(os.path.exists(exe)):
            os.remove(exe)
        os.system(r"gcc {0} -o {1}".format(filename,exe))
        os.startfile(exe)

    '''
    生成决策表
    '''
    def createtable(self):
        dt=DecisionTable()
        condition=str(self.condition_1.text())
        result=dt.create(condition)
        self.table_1.setColumnCount(len(result)+1)
        self.table_1.setRowCount(len(result[1])+1)
        #self.model = QtGui.QStandardItemModel(self.table_1)
        #self.model.setRowCount(len(result[0])+1)
        #self.model.setColumnCount(len(result)+1)
        self.table_1.setSpan(0,0,len(result[1])-1,1)
        self.table_1.setSpan(len(result[1])-1,0,2,1)
        self.table_1.setItem(0,0,QtGui.QTableWidgetItem(_fromUtf8('条件')))
        self.table_1.setItem(len(result[1])-1,0,QtGui.QTableWidgetItem(_fromUtf8('动作')))
        self.table_1.setColumnWidth(0,40)
        self.table_1.setColumnWidth(1,50)
        for i in range(len(result[1])-1):
            self.table_1.setItem(i,1,QtGui.QTableWidgetItem(_fromUtf8(result[0][i])))
            for j in  range(2,len(result)+1):
                self.table_1.setColumnWidth(j,30)
                if result[j-1][i]=='0':
                    self.table_1.setItem(i,j,QtGui.QTableWidgetItem(_fromUtf8('N')))
                if result[j-1][i]=='1':
                    self.table_1.setItem(i,j,QtGui.QTableWidgetItem(_fromUtf8('Y')))
        for m in range(1,len(result)):
                if result[m][-1]=='1':
                    self.table_1.setItem(len(result[1])-1,m+1,QtGui.QTableWidgetItem(_fromUtf8(u'√')))
                if result[m][-1]=='0':
                    self.table_1.setItem(len(result[1]),m+1,QtGui.QTableWidgetItem(_fromUtf8(u'√')))
        self.table_1.setItem(len(result[1])-1,1,QtGui.QTableWidgetItem(_fromUtf8(u'执行')))
        print len(result[1])
        self.table_1.setItem(len(result[1]),1,QtGui.QTableWidgetItem(_fromUtf8(u'不执行')))
    def export4(self):
        head='The Decision Table of '+self.condition_1.text()
        filename = QFileDialog.getSaveFileName(self,self.tr("保存到"),self.tr('New Microsoft Excel File.xls'),self.tr('Excel File(*.xls)'))
        savefile=str(filename).decode("utf8")
        #创建excel
        wb=xlwt.Workbook()
        #添加sheet表
        ws=wb.add_sheet(u'决策表')
        font1=xlwt.Font()
        style1=xlwt.XFStyle()
        font1.name='Times New Roman'
        font1.bold=True
        font1.colour_index=2
        font1.height=0xF0
        style1.font=font1
        ws.write_merge(0, 0,0,self.table_1.columnCount()-1,str(head).decode("gbk"),style1)
        # 遍历Table插值
        for i in range(1,self.table_1.rowCount()+1):
            for j in range(self.table_1.columnCount()):
                # 当原表格内容为空时要处理
                if self.table_1.item(i-1,j)==None:
                    ws.write(i, j," ")
                else:
                    ws.write(i, j,str(self.table_1.item(i-1,j).text()).decode("utf8"))
        wb.save(savefile)
    '''
    生成测试用例
    '''
    def testcase(self):
        tc=TestCase()
        condition=str(self.condition_2.text())
        result=tc.create(condition)
        self.table_3.setColumnCount(len(result[0]))
        self.table_3.setRowCount(len(result))
        for i in range(len(result)):
            for j in  range(len(result[0])-1):
                self.table_3.setItem(i,j,QtGui.QTableWidgetItem(str(result[i][j])))
        for m in range(len(result)):
            if result[m][-1]==0:
                self.table_3.setItem(m,len(result[0])-1,QtGui.QTableWidgetItem(_fromUtf8('N')))
            elif result[m][-1]==1:
                self.table_3.setItem(m,len(result[0])-1,QtGui.QTableWidgetItem(_fromUtf8('Y')))
            else:
                self.table_3.setItem(m,len(result[0])-1,QtGui.QTableWidgetItem(str(result[m][-1])))
    def export5(self):
        head='The Testing Case Based on Conditional Decision Combination Cover of '+self.condition_2.text()
        filename = QFileDialog.getSaveFileName(self,self.tr("保存到"),self.tr('New Microsoft Excel File.xls'),self.tr('Excel File(*.xls)'))
        savefile=str(filename).decode("utf8")
        #创建excel
        wb=xlwt.Workbook()
        #添加sheet表
        ws=wb.add_sheet(u'测试用例')
        font1=xlwt.Font()
        style1=xlwt.XFStyle()
        font1.name='Times New Roman'
        font1.bold=True
        font1.colour_index=2
        font1.height=0xF0
        style1.font=font1
        ws.write_merge(0, 0,0,self.table_3.columnCount()-1,str(head).decode("gbk"),style1)
        # 遍历Table插值
        for i in range(1,self.table_3.rowCount()+1):
            for j in range(self.table_3.columnCount()):
                # 当原表格内容为空时要处理
                if self.table_3.item(i-1,j)==None:
                    ws.write(i, j," ")
                else:
                    ws.write(i, j,str(self.table_3.item(i-1,j).text()).decode("utf8"))
        wb.save(savefile)
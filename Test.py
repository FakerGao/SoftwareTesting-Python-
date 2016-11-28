from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import ToolsUI

class TestWindow(QMainWindow,ToolsUI.Ui_MainWindow):
      def __init__(self,parent=None):
            super(TestWindow,self).__init__(parent)
            self.setupUi(self)

app=QApplication(sys.argv)
a=TestWindow()
a.show()
app.exec_()
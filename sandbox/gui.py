from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QMainWindow):
   def __init__(self, parent = None):
      super().__init__(parent)
      
      layout = QHBoxLayout()
      bar = self.menuBar()
      file = bar.addMenu("File")
      file.addAction("New")
      file.addAction("save")
      file.addAction("quit")
		
      self.items = QDockWidget("Dockable", self)
      self.listWidget = QListWidget()
      self.listWidget.addItem("item1")
      self.listWidget.addItem("item2")
      self.listWidget.addItem("item3")
		
      self.items.setWidget(self.listWidget)
      self.items.setFloating(False)
      self.setCentralWidget(QTextEdit())
      self.addDockWidget(Qt.RightDockWidgetArea, self.items)
      self.setLayout(layout)
      self.setWindowTitle("Dock demo")
		
def main():
   app = QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()

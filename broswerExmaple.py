from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import QWebEngineView

from ui_broswerExmaple import Ui_MainWindow as mainScreen
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainScreen()
        self.ui.setupUi(self)
        
        self.ui.browserWidget.setUrl(QUrl('https://google.com'))
        
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication()
    window = App()
    sys.exit(app.exec_())
    
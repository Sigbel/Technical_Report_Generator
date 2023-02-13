import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from interface.main_window import *

class Main_Page(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_page = Main_Page()
    main_page.show()
    app.exec_()
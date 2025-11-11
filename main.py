import sys
from PyQt5.QtWidgets import (QApplication,QVBoxLayout,QHBoxLayout,QWidget,QPushButton,QLineEdit,QLabel,QTableWidget,QTableWidgetItem,QMessageBox)
from PyQt5.QtGui import QPalette , QFont , QColor


class InvoiceManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Invoice")  #the app title
        self.setgeometry(300,200,800,500) #app size

        palette = QPalette()
        palette.setColor(QPalette.Window,QColor("#D3DAD9")) #app color
        self.setPalette(palette)

        layout = QVBoxLayout(self)
        input_layout = QHBoxLayout(self) #Layout is used to size or manage the widgets
        total_layout = QHBoxLayout(self)



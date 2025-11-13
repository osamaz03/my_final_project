import sys
from PyQt5.QtWidgets import (QApplication,QVBoxLayout,QHBoxLayout,QWidget,QPushButton,QLineEdit,QLabel,QTableWidget,QTableWidgetItem,QMessageBox)
from PyQt5.QtGui import QPalette , QFont , QColor


class InvoiceManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Invoice")  #the app title
        self.setGeometry(300,200,800,500) #app size

        palette = QPalette()
        palette.setColor(QPalette.Window,QColor("#D3DAD9")) #app color
        self.setPalette(palette)

        layout = QVBoxLayout(self)
        input_layout = QHBoxLayout(self) #Layout is used to size or manage the widgets
        total_layout = QHBoxLayout(self)


        #the input for product name , price and quantity
        self.product_name = QLineEdit()
        self.product_name.setPlaceholderText("P.Name")
        self.product_name.setFont(QFont("San Francisco",14))
        input_layout.addWidget(self.product_name)

        self.product_price = QLineEdit()
        self.product_price.setPlaceholderText("P.Price")
        self.product_price.setFont(QFont("San Francisco",14))
        input_layout.addWidget(self.product_price)

        self.product_quantity = QLineEdit()
        self.product_quantity.setPlaceholderText("P.Quantity")
        self.product_quantity.setFont(QFont("San Francisco",14))
        input_layout.addWidget(self.product_quantity)



# to run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = InvoiceManager()
    w.show()
    sys.exit(app.exec_())



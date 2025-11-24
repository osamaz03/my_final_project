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

        self.add_btn = QPushButton("Add")
        self.add_btn.clicked.connect(self.add)
        self.add_btn.setFont(QFont("San Francisco",14))
        input_layout.addWidget(self.add_btn)


        # the information table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Product Name" ,"Product Price","Product Quantity" ,"Total"])
        layout.addWidget(self.table)

        #the total text label and the total button
        self.total_label = QLabel("The Total: ")
        self.total_label.setFont(QFont("San Francisco",14))
        total_layout.addWidget(self.total_label)

        self.total_btn = QPushButton("Total")
        self.total_btn.clicked.connect(self.total)
        self.total_btn.setFont(QFont("San Francisco",14))
        total_layout.addWidget(self.total_btn)

        self.delete_btn = QPushButton("Delete")
        self.delete_btn.setFont(QFont("San Francisco",14))
        self.delete_btn.clicked.connect(self.delete)
        input_layout.addWidget(self.delete_btn)

        #adding the other layout to the main one
        layout.addLayout(input_layout)
        layout.addLayout(total_layout)
        self.setLayout(layout)


    def add(self):
        name = self.product_name.text()
        price = self.product_price.text()
        qty = self.product_quantity.text()


        # if the user did not fill in all fields show error
        if not name or not price or not qty:
            QMessageBox.warning(self,"Error","Please fill in all fields")
            return

        #error handling
        try:
            price = float(price)
            qty = int(qty)
            total = price * qty
        except ValueError:
            QMessageBox.warning(self,"Error","Please add a valid number")
        except Exception as e:
            QMessageBox.warning(self,"Error",f"Error: {e}")



        row = self.table.rowCount() #creating the row
        self.table.insertRow(row) # applying the row in the table

        # adding the item to the table
        self.table.setItem(row,0,QTableWidgetItem(name))
        self.table.setItem(row,1,QTableWidgetItem(f"{price:.2f}"))
        self.table.setItem(row,2,QTableWidgetItem(str(qty)))
        self.table.setItem(row,3,QTableWidgetItem(f"{total:.2f}"))


        #to clear the input
        self.product_name.clear()
        self.product_price.clear()
        self.product_quantity.clear()


    def total(self):
        sum_total = 0

        for i in range(self.table.rowCount()):
            try:
                sum_total += float(self.table.item(i,3).text())
            except Exception as e:
                QMessageBox.warning(self,"Error",f" Error {e}")
                return

        self.total_label.setText(f"The Total:{sum_total} Euro")

    def delete(self):
        row = self.table.currentRow()

        if row != -1:
            self.table.removeRow(row)
        else:
            QMessageBox.warning(self,"Error","Please select a row")






# to run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = InvoiceManager()
    w.show()
    sys.exit(app.exec_())



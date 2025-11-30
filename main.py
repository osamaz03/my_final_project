import sys
import csv
import os
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
        self.product_name.setStyleSheet("""
                QLineEdit {
                    background: #FFFFFF;
                    border-radius: 10px;
                    padding: 10px;
                    border: 2px solid #D3DAD9;
                }
            """)

        self.product_price = QLineEdit()
        self.product_price.setPlaceholderText("P.Price")
        self.product_price.setFont(QFont("San Francisco",14))
        input_layout.addWidget(self.product_price)
        self.product_price.setStyleSheet("""
                QLineEdit {
                    background: #FFFFFF;
                    border-radius: 10px;
                    padding: 10px;
                    border: 2px solid #D3DAD9;
                }
            """)

        self.product_quantity = QLineEdit()
        self.product_quantity.setPlaceholderText("P.Quantity")
        self.product_quantity.setFont(QFont("San Francisco",14))
        input_layout.addWidget(self.product_quantity)
        self.product_quantity.setStyleSheet("""
                QLineEdit {
                    background: #FFFFFF;
                    border-radius: 10px;
                    padding: 10px;
                    border: 2px solid #D3DAD9;
                }
            """)

        self.add_btn = QPushButton("Add")
        self.add_btn.clicked.connect(self.add)
        self.add_btn.setFont(QFont("San Francisco",14))
        input_layout.addWidget(self.add_btn)
        self.add_btn.setStyleSheet("""
                QPushButton {
                    background-color: #715A5A;
                    color: white;
                    border-radius: 10px;
                    padding: 10px 24px;
                }
                QPushButton:hover {
                    background-color: #44444E;
                }
            """)

        # the information table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Product Name" ,"Product Price","Product Quantity" ,"Total"])
        self.table.resizeColumnsToContents()
        layout.addWidget(self.table)
        self.table.setStyleSheet("""
                QTableWidget {
                    background: #FFFFFF;
                    border-radius: 12px;
                    font-size: 15px;
                    color: #395B64;
                    gridline-color: #D3DAD9;
                }
                QHeaderView::section {
                    background: #F5F7FA;
                    color: #395B64;
                    font-weight: bold;
                    border-radius: 8px;
                    padding: 6px;
                }
            """)

        #the total text label and the total button
        self.total_label = QLabel("The Total: ")
        self.total_label.setFont(QFont("San Francisco",14))
        total_layout.addWidget(self.total_label)
        self.total_label.setStyleSheet("""
                QLabel {
                    background: #E7E7E7;
                    border-radius: 10px;
                    padding: 10px 20px;
                    color: #4F8A8B;
                    border: 2px solid #D3DAD9;
                }
            """)

        self.total_btn = QPushButton("Total")
        self.total_btn.clicked.connect(self.total)
        self.total_btn.setFont(QFont("San Francisco",14))
        total_layout.addWidget(self.total_btn)
        self.total_btn.setStyleSheet("""
                QPushButton {
                    background-color: #715A5A;
                    color: white;
                    border-radius: 10px;
                    padding: 10px 24px;
                }
                QPushButton:hover {
                    background-color: #44444E;
                }
            """)

        self.delete_btn = QPushButton("Delete")
        self.delete_btn.setFont(QFont("San Francisco",14))
        self.delete_btn.clicked.connect(self.delete)
        input_layout.addWidget(self.delete_btn)
        self.delete_btn.setStyleSheet("""
                QPushButton {
                    background-color: #715A5A;
                    color: white;
                    border-radius: 10px;
                    padding: 10px 24px;
                }
                QPushButton:hover {
                    background-color: #44444E;
                }
            """)

        #adding the other layout to the main one
        layout.addLayout(input_layout)
        layout.addLayout(total_layout)
        self.setLayout(layout)
        self.load_file()


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

        if price < 0 or qty < 0:
            QMessageBox.warning(self,"Error","The number must be greater then Zero")
            return



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
        self.save_file()


    def total(self):
        sum_total = 0 # to collect the total


        # adding the total from the column number 3
        for i in range(self.table.rowCount()):
            try:
                sum_total += float(self.table.item(i,3).text())
            except Exception as e:
                QMessageBox.warning(self,"Error",f" Error {e}")
                return

        self.total_label.setText(f"The Total:{sum_total} Euro") #apply the total in the label

    def delete(self):
        row = self.table.currentRow()

        #if there is a selected row
        if row != -1:
            self.table.removeRow(row)
        else:
            QMessageBox.warning(self,"Error","Please select a row")
        self.save_file()


    # save the app data in a file
    def save_file(self):
        rows = self.table.rowCount()
        cols = self.table.columnCount()

        with open("invoice.txt","w",newline="",encoding="utf-8") as f:
            writer = csv.writer(f)

            for row in range(rows):
                row_data = []
                for col in range(cols):
                    items = self.table.item(row,col)
                    if items:
                        row_data.append(items.text())
                writer.writerow(row_data)


    # load the file
    def load_file(self):
        if not os.path.exists("invoice.txt"):
            return

        self.table.setRowCount(0)

        with open("invoice.txt","r",encoding="utf-8") as f:
            reader = csv.reader(f)

            for row_v in reader:
                row_index = self.table.rowCount()
                self.table.insertRow(row_index)                #from line 252 to 256 AI helped me
                for c,values in enumerate(row_v):
                    self.table.setItem(row_index,c,QTableWidgetItem(values))







# to run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = InvoiceManager()
    w.show()
    sys.exit(app.exec_())



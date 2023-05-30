from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QColor, QBrush
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
app = QApplication([])
window = QMainWindow()

table_widget = QTableWidget()
window.setCentralWidget(table_widget)

# Create a QTableWidgetItem
item = QTableWidgetItem("Hello")

# Set the background color to red
red_color = QColor(255, 0, 0)
brush = QBrush(red_color)
item.setBackground(brush)

# Add the item to the table widget
table_widget.setItem(0, 0, item)

window.show()
app.exec()

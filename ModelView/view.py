import sys

import view as v
from model import  CustomModel
from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QLabel, QComboBox, QGridLayout, QPushButton, QWidget, QTableView, QListView
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lab 4")
        self.setGeometry(300, 300, 350, 100)
        self.resize(600, 600)
        tableView = QTableView()
        model = CustomModel()
        tableView.setModel(model)
        tableView.show()
        listView = QListView()
        listView.setModel(model)
        listView.show()

        layout = QGridLayout()

        views = QComboBox()
        views.addItems(["One", "Two", "Three"])
        layout.addWidget(QLabel('A list of views'), 0, 0)
        layout.addWidget(views, 0, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(listView)

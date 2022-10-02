import sys

from model import Rectangle
from model import  CustomModel
from PyQt5 import Qt
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QLabel, QComboBox, QGridLayout, QPushButton, QWidget, QTableView, QListView, QTreeView
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lab 4")
        self.setGeometry(300, 300, 350, 100)
        self.resize(600, 600)
        myrects = []
        for i in range(16):
            myrects.append(Rectangle(i, i, i * 16, i * 16))
        model = CustomModel(myrects)

        tableView = QTableView()
        tableView.setModel(model)
        tableView.adjustSize()

        listView = QListView()
        listView.setModel(model)

        treeView = QTreeView()
        treeView.setModel(model)

        layout = QGridLayout()
        views = QComboBox()
        views.addItems(["One", "Two", "Three"])
        layout.addWidget(tableView, 0, 0)
        layout.addWidget(listView, 0, 1)
        layout.addWidget(treeView, 0, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

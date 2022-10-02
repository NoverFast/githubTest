import sys

from model import Rectangle
from model import  CustomModel
from PyQt5 import Qt
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QLabel, QComboBox, QGridLayout, QPushButton, QWidget, QTableView, QListView, QTreeView, QLineEdit, \
    QSpinBox, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.myrects = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Lab 4")
        self.setGeometry(100, 50, 300, 300)
        self.resize(800, 800)
        #listWidget = QListWidget(self)
        for i in range(16):
            self.myrects.append(Rectangle(i, i, i * 16, i * 16))
        model = CustomModel(self.myrects)
        tableView = QTableView()
        tableView.setModel(model)
        
        listView = QListView()
        listView.setModel(model)

        treeView = QTreeView()
        treeView.setModel(model)
        layout2 = QGridLayout()
        layout = QGridLayout()
        views = QComboBox()
        layout.addWidget(tableView, 0, 0)
        layout.addWidget(listView, 0, 1)
        layout.addWidget(treeView, 0, 2)
        layout2.addLayout(layout, 0, 0)
        btn = QPushButton("Add Rectangle")
        btn.clicked.connect(self.addRectangle)
        layout2.addWidget(btn, 1, 1)
        self.width = QSpinBox()
        self.height = QSpinBox()
        layout2.addWidget(self.width, 2, 1)
        layout2.addWidget(self.height, 3, 1)
        layout2.addWidget(QLabel("Add Rectangle: "), 1, 0)
        layout2.addWidget(QLabel("Width: "), 2, 0)
        layout2.addWidget(QLabel("Height: "), 3, 0)
        widget = QWidget()
        widget.setLayout(layout2)
        self.setCentralWidget(widget)
    def addRectangle(self):
        print("a")
        QListWidgetItem(Rectangle(1, 1, self.width.value(), self.height.value()), self.listWidget)
        print("b")
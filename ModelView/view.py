import sys

from model import Rectangle
from model import  CustomModel
from PyQt5 import Qt
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QLabel, QComboBox, QGridLayout, QPushButton, QWidget, QTableView, QListView, QTreeView, QLineEdit, \
    QSpinBox, QListWidget, QListWidgetItem, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initData()
        self.initMV()
        self.initUI()

    def initData(self):
        self.myrects = []
        for i in range(16):
            self.myrects.append(Rectangle(i, i, i * 16, i * 16))

    def initMV(self):
        #   моя модель с прямоугольниками
        self.model = CustomModel(self.myrects)
        # и её разные отображения в окне программы
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        self.listView = QListView()
        self.listView.setModel(self.model)

        self.treeView = QTreeView()
        self.treeView.setModel(self.model)

    def initUI(self):
        self.setWindowTitle("Lab 4")
        self.setGeometry(100, 50, 300, 300)
        self.resize(800, 800)

        layout2 = QGridLayout()
        layout3 = QVBoxLayout()

        layout = QGridLayout()
        layout.addWidget(self.tableView, 0, 0)
        layout.addWidget(self.listView, 0, 1)
        layout.addWidget(self.treeView, 0, 2)
        layout2.addLayout(layout, 0, 0)

        layout3.addWidget(QLabel("Add Rectangle: "))
        btn = QPushButton("Add Rectangle")
        btn.clicked.connect(self.addRectangle)
        layout3.addWidget(btn)
        self.width = QSpinBox()
        self.height = QSpinBox()
        layout3.addWidget(QLabel("Width: "))
        layout3.addWidget(self.width)
        layout3.addWidget(QLabel("Height: "))
        layout3.addWidget(self.height)
        layout3.addWidget(QLabel("Print info: "))
        infoBtn = QPushButton("Info")
        infoBtn.clicked.connect(self.printInformation)
        layout3.addWidget(infoBtn)
        layout3.addWidget(QLabel("Item's index: "))
        self.indexSB = QSpinBox()
        layout3.addWidget(self.indexSB)
        layout2.addLayout(layout3, 0, 1)
        widget = QWidget()
        widget.setLayout(layout2)
        self.setCentralWidget(widget)

    def printInformation(self):
        getIndex = self.model.index(self.indexSB.value() ,0, QModelIndex())
        value = self.model.data(getIndex, Qt.DisplayRole)
        print(f"Rectangle area: {value}")

    def addRectangle(self):
        print("a")
        QListWidgetItem(Rectangle(1, 1, self.width.value(), self.height.value()), self.listWidget)
        print("b")
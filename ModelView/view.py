import sys

from model import Rectangle
from model import RectangleModel
from PyQt5 import Qt
from PyQt5.QtCore import Qt, QModelIndex, QItemSelectionModel
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QLabel, QComboBox, QGridLayout, QPushButton, QWidget, QTableView, QListView, QTreeView, QLineEdit, \
    QSpinBox, QListWidget, QListWidgetItem, QVBoxLayout

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
        self.model = RectangleModel(self.myrects)
        # и её разные отображения в окне программы
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        self.listView = QListView()
        self.listView.setModel(self.model)

        self.treeView = QTreeView()
        self.treeView.setModel(self.model)

        self.listView.setSelectionModel(self.tableView.selectionModel())
        self.treeView.setSelectionModel(self.tableView.selectionModel())

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

        layout3.addWidget(QLabel("Replace Rectangle: "))
        replaceBtn = QPushButton("Replace Rectangle")
        replaceBtn.clicked.connect(self.replaceRectangle)
        layout3.addWidget(replaceBtn)
        insertBtn = QPushButton("Insert Rectangle")
        insertBtn.clicked.connect(self.insertRectangle)
        layout3.addWidget(QLabel("Insert Rectangle: "))
        layout3.addWidget(insertBtn)
        removeBtn = QPushButton("Remove Rectangle")
        removeBtn.clicked.connect(self.deleteRectangle)
        layout3.addWidget(QLabel("Remove Rectangle: "))
        layout3.addWidget(removeBtn)
        layout3.addWidget(QLabel("x: "))
        self.x = QSpinBox()
        layout3.addWidget(self.x)
        self.y = QSpinBox()
        layout3.addWidget(QLabel("y: "))
        layout3.addWidget(self.y)
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

    def replaceRectangle(self):
        getIndex = self.model.index(self.indexSB.value(), 0, QModelIndex())
        value = Rectangle(self.x.value(), self.y.value(), self.width.value(), self.height.value())
        self.model.setData(getIndex, value, Qt.EditRole)
    def insertRectangle(self):
        val = self.indexSB.value()
        self.model.insertRow(val)
    def deleteRectangle(self):
        self.model.removeRow(self.indexSB.value())
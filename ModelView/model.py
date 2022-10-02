from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont

class Rectangle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Information(self):
        return f"Rectangle has the following parameters: X: {self.x} Y: {self.y} " \
               f"Width: {self.width} Height: {self.height}"
    def Area(self):
        return self.x * self.y
    def draw(self):
        qp = QPainter()
        qp.drawRect(self.x, self.y)
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def GetWidth(self):
        return self.width
    def GetHeight(self):
        return self.height

class CustomModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def rowCount(self, parent=None):
        return 8

    def columnCount(self, parent=None):
        return 8

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        col = index.column()
        # generate a log message when this method gets called
        #for i in len(range(row)):
            #for j in len(range(col)):
        rect = Rectangle(5, 5, 10, 10)
        print(f"row {row}, col{col}, role {role}")

        if role == Qt.DisplayRole:
            if row == 0 and col == 1:
                return "<--left"
            if row == 1 and col == 1:
                return "right-->"
            return rect.Information()

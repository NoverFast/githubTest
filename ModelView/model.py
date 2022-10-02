from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtGui import QPainter

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
        self.data = []
        for i in range(16):
            self.data.append(Rectangle(i, i, 5 * i, 10 * i))
            print(self.data[i].Information())

    def rowCount(self, count, parent=None):
        return 4

    def columnCount(self, parent=None):
        return 4

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        col = index.column()
        # generate a log message when this method gets called
        print(f"row {row}, col{col}, role {role}")

        if role == Qt.DisplayRole:
            return f"{self.data[index.row()].Information()}"

from PyQt5.QtCore import QAbstractItemModel, Qt, QAbstractListModel, QModelIndex
from PyQt5.QtGui import QPainter, QBrush
from random import choice

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
        return self.width * self.height
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def GetWidth(self):
        return self.width
    def GetHeight(self):
        return self.height

class RectangleModel(QAbstractListModel):
    def __init__(self, rects, parent=None):
        super().__init__(parent)
        self._rects = rects

    def rowCount(self, parent=None):
        return len(self._rects)

    def columnCount(self, parent=None):
        return len(self._rects)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return f"{self._rects[row].Area()}"
        elif role == Qt.BackgroundRole:
            if row % 3 == 0:
                return QBrush(Qt.cyan)

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self._rects[index.row()] = value
            self.dataChanged.emit(index, index, {role})
            return True
        return False

    def insertRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()):
        val = row
        obj = Rectangle(val, val, val * 16, val * 16)
        """Inserts a number of rows into the model at the specified position."""
        self.beginInsertRows(QModelIndex(), row, row + count - 1)
        for row in range(count):
            self._rects.append(obj)
        self.endInsertRows()
        return True

    def removeRows(self, row: int, count: int, parent: QModelIndex = QModelIndex()):
        """Removes a number of rows from the model at the specified position."""
        self.beginRemoveRows(QModelIndex(), row, row + count - 1)
        for row in range(count):
            self._rects.pop(row)
        self.endRemoveRows()
        return True
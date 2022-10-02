from PyQt5.QtCore import QAbstractTableModel, Qt, QAbstractListModel, QModelIndex
from PyQt5.QtGui import QPainter, QBrush


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

class CustomModel(QAbstractListModel):
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

        # generate a log message when this method gets called

        if role == Qt.DisplayRole:
            return f"{self._rects[row].Area()}"
        elif role == Qt.BackgroundRole:
            if row % 4 == 0:  # change background only for cell(1,2)
                return QBrush(Qt.cyan)

    def setData(self, index, value, role=Qt.EditRole):
        """Changes an item in the string list, but only if the following conditions
           are met:

           # The index supplied is valid.
           # The index corresponds to an item to be shown in a view.
           # The role associated with editing text is specified.

           The dataChanged() signal is emitted if the item is changed."""

        if index.isValid() and role == Qt.EditRole:
            self._rects[index.row()] = value
            self.dataChanged.emit(index, index, {role})
            return True
        return False

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Returns the appropriate header string depending on the orientation of
           the header and the section. If anything other than the display role is
           requested, we return an invalid variant."""
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return f"Column {section}"
        return f"Row {section}"

    def insertRows(self, position, rows, parent):
        """Inserts a number of rows into the model at the specified position."""
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self._rects.insert(position, "")
        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent):
        """Removes a number of rows from the model at the specified position."""
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            del self._rects[position]
        self.endRemoveRows()
        return True
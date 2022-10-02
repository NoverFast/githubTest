from qtpy import QtWidgets, QtCore, QtGui
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from qtpy import QtWidgets, QtCore, QtGui

import numpy as np

class MainView(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        grid = QtWidgets.QVBoxLayout(self)
        self.plot_view = PlotView()
        self.options_view = View()

        grid.addWidget(self.plot_view)
        grid.addWidget(self.options_view)

        self.setLayout(grid)

    def getOptionView(self):
        return self.options_view

    def getPlotView(self):
        return self.plot_view

class PlotView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure = plt.figure()
        grid = QtWidgets.QVBoxLayout(self)
        self.draw()
        self.canvas = self.getWidget()
        grid.addWidget(self.canvas)
        self.setLayout(grid)

    def draw(self):
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.set_xlim([0.0, 10.5])
        ax.set_ylim([-1.05, 1.05])
        ax.set_xlabel("time ($s$)")
        ax.set_ylabel("$f(t)$")
        return ax

    def getWidget(self):
        return FigureCanvas(self.figure)

    def addData(self, xvalues, yvalues, grid_lines, colour, marker):
        ax = self.draw()
        ax.grid(grid_lines)
        ax.plot(xvalues, yvalues, color=colour, marker=marker, linestyle="--")
        self.canvas.draw()

class View(QtWidgets.QWidget):

    plotSignal = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        grid = QtWidgets.QVBoxLayout(self)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setRowCount(4)
        self.table.setColumnCount(2)

        grid.addWidget(self.table)

        self.colours = QtWidgets.QComboBox()
        options=["Blue", "Green", "Red"]
        self.colours.addItems(options)

        self.grid_lines= QtWidgets.QTableWidgetItem()
        self.grid_lines.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        self.grid_lines.setCheckState(QtCore.Qt.Unchecked)
        self.addItemToTable("Show grid lines", self.grid_lines, 1)

        self.freq = QtWidgets.QTableWidgetItem("1.0")
        self.phi = QtWidgets.QTableWidgetItem("0.0")

        self.addWidgetToTable("Colour", self.colours, 0)
        self.addItemToTable("Frequency", self.freq, 2)
        self.addItemToTable("Phase", self.phi, 3)

        self.plot = QtWidgets.QPushButton('Add', self)
        self.plot.setStyleSheet("background-color:lightgrey")

        grid.addWidget(self.plot)

        self.setLayout(grid)

        self.plot.clicked.connect(self.buttonPressed)

    def getColour(self):
        return self.colours.currentText()

    def getGridLines(self):
        return self.grid_lines.checkState() == QtCore.Qt.Checked

    def getFreq(self):
        return float(self.freq.text())

    def getPhase(self):
        return float(self.phi.text())

    def buttonPressed(self):
        self.plotSignal.emit()

    def setTableRow(self, name, row):
        text = QtWidgets.QTableWidgetItem(name)
        text.setFlags(QtCore.Qt.ItemIsEnabled)
        col = 0
        self.table.setItem(row, col, text)

    def addWidgetToTable(self, name, widget, row):
        self.setTableRow(name, row)
        col = 1
        self.table.setCellWidget(row, col, widget)

    def addItemToTable(self, name, widget, row):
        self.setTableRow(name, row)
        col = 1
        self.table.setItem(row, col, widget)

    def setColours(self, options):
        self.colours.clear()
        self.colours.addItems(options)
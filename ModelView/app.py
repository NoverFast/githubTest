import sys
import view as v
from model import  CustomModel
from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QVBoxLayout, QHBoxLayout, QLabel, QToolBar, QAction, QGridLayout, QComboBox, QPushButton, QTableView
from PyQt5.QtGui import QPalette, QColor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #tableView = QTableView()
    #model = CustomModel()
    #tableView.setModel(model)
    #tableView.show()
    start = v.MainWindow()
    start.show()
    app.exec()
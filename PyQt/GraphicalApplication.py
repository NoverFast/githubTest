from qtpy import QtWidgets

import sys

import Model as m
import View as v
import Presenter as p

class Demo(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        data_model = m.DataGenerator()
        colour_list = m.line_colours()

        self.window = QtWidgets.QMainWindow()

        my_view = v.MainView(parent=self)
        self.main_presenter = p.MainPresenter(my_view, data_model, colour_list)

        # set the view for the main window
        self.setCentralWidget(my_view)
        self.setWindowTitle("view tutorial")


def qapp():
    if QtWidgets.QApplication.instance():
        _app = QtWidgets.QApplication.instance()
    else:
        _app = QtWidgets.QApplication(sys.argv)
    return _app


app = qapp()
window = Demo()
window.show()
app.exec_()

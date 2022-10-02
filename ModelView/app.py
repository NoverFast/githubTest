import sys
import view as v

from PyQt5.QtWidgets import QApplication
if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = v.MainWindow()
    start.show()
    app.exec()
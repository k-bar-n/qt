# pyuic6 qt_p_1_d.ui -o py_qt_p_1_d.py

import sys
from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("qt_p_1_d.ui", self)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

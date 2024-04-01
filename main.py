# pyuic6 qt_p_1_d.ui -o py_qt_p_1_d.py

import sys
from PyQt6 import QtWidgets, uic


k = 0


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("qt_p_1_d.ui", self)

        self.Button_2.clicked.connect(self.first)

    def first(self):
        global k
        print("lol", k)
        k += 1
        if k % 2 == 0:
            self.Button_2.setStyleSheet("""
                QPushButton {
                    background-color: red;
                }
            """)
        else:
            self.Button_2.setStyleSheet("""
                QPushButton {
                    background-color: orange;
                }
            """)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

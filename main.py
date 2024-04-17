# pyuic6 qt_p_1_d.ui -o py_qt_p_1_d.py

import sys
from PyQt6 import QtWidgets, uic


k_red = 1
k_green = 1
k_yellow = 1


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("qt_p_1_d.ui", self)

        self.Button_red.clicked.connect(self.red)
        self.Button_green.clicked.connect(self.green)
        self.Button_yellow.clicked.connect(self.yellow)

        self.Button_on.clicked.connect(self.on)
        self.Button_off.clicked.connect(self.off)

    def red(self):
        global k_red
        # print("lol", k_red)
        k_red += 1
        if k_red % 2 == 0:
            self.Button_red.setStyleSheet("""
                QPushButton#Button_red {
                    background-color: red;
                }
            """)
        else:
            self.Button_red.setStyleSheet("""
                QPushButton#Button_red {
                    background-color: rgb(150, 150, 150);
                }
            """)

    def green(self):
        global k_green
        # print("lol", k_green)
        k_green += 1
        if k_green % 2 == 0:
            self.Button_green.setStyleSheet("""
                QPushButton#Button_green {
                    background-color: green;
                }
            """)
        else:
            self.Button_green.setStyleSheet("""
                QPushButton#Button_green {
                    background-color: rgb(150, 150, 150);
                }
            """)

    def yellow(self):
        global k_yellow
        # print("lol", k_yellow)
        k_yellow += 1
        if k_yellow % 2 == 0:
            self.Button_yellow.setStyleSheet("""
                QPushButton#Button_yellow {
                    background-color: yellow;
                }
            """)
        else:
            self.Button_yellow.setStyleSheet("""
                QPushButton#Button_yellow {
                    background-color: rgb(150, 150, 150);
                }
            """)

    def on(self):
        self.Button_red.setStyleSheet("""
            QPushButton#Button_red {
                background-color: red;
            }
        """)
        self.Button_green.setStyleSheet("""
            QPushButton#Button_green {
                background-color: green;
            }

        """)
        self.Button_yellow.setStyleSheet("""
            QPushButton#Button_yellow {
                background-color: yellow;
            }
        """)

    def off(self):
        self.Button_red.setStyleSheet("""
            QPushButton#Button_red {
                background-color: rgb(150, 150, 150);
            }
        """)
        self.Button_green.setStyleSheet("""
            QPushButton#Button_green {
                background-color: rgb(150, 150, 150);
            }

        """)
        self.Button_yellow.setStyleSheet("""
            QPushButton#Button_yellow {
                background-color: rgb(150, 150, 150);
            }
        """)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

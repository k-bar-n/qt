# pyuic6 qt_p_1_d.ui -o py_qt_p_1_d.py

import sys
from PyQt6 import QtWidgets, uic

# Задаем начальные значения для переменных k
k_red = 1
k_green = 1
k_yellow = 1

# Создаем словарь с RGB значениями для каждого цвета
color_rgb = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "grey": (150, 150, 150)
}


def set_button_color(button, color):
    button.setStyleSheet("""
        QPushButton {
            background-color: rgb(%d, %d, %d);
        }
    """ % color)


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
        k_red += 1
        if k_red % 2 == 0:
            set_button_color(self.Button_red, color_rgb["red"])
        else:
            set_button_color(self.Button_red, color_rgb["grey"])

    def green(self):
        global k_green
        k_green += 1
        if k_green % 2 == 0:
            set_button_color(self.Button_green, color_rgb["green"])
        else:
            set_button_color(self.Button_green, color_rgb["grey"])

    def yellow(self):
        global k_yellow
        k_yellow += 1
        if k_yellow % 2 == 0:
            set_button_color(self.Button_yellow, color_rgb["yellow"])
        else:
            set_button_color(self.Button_yellow, color_rgb["grey"])

    def on(self):
        set_button_color(self.Button_red, color_rgb["red"])
        set_button_color(self.Button_green, color_rgb["green"])
        set_button_color(self.Button_yellow, color_rgb["yellow"])

    def off(self):
        set_button_color(self.Button_red, color_rgb["grey"])
        set_button_color(self.Button_green, color_rgb["grey"])
        set_button_color(self.Button_yellow, color_rgb["grey"])


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

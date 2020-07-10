# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure


import numpy as np
import matplotlib.pyplot as plt

import gui
import sort
import db
import gen


def histoogramm(label, data1, data2):
    plt.rcdefaults()

    objects = ('TimeSort', 'MergeSort')
    y_pos = np.arange(len(objects))
    performance = [data1, data2]

    plt.bar(y_pos, performance, align='center', alpha=0.8, color="bg")
    plt.xticks(y_pos, objects)
    plt.title(label)

    plt.show()


class MplWidget(QWidget):

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)


if __name__ == '__main__':
    app = QApplication([])
    ex = MplWidget()
    sys.exit(app.exec_())

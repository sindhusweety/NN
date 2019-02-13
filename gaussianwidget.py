import sys
import random
import pandas as pd

import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import json
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure
import random

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker, cm
import json

import squarify

class gaussianWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.canvas)
        # lay.addWidget(button)
        self.update_graph()

    def update_graph(self):

        data = json.loads(open('list_gaussian_value.json').read())
        A = data[0]
        print(A)
        size = 100
        sigma_x = data[1]
        print(sigma_x)
        sigma_y = data[2]
        print(sigma_y)

        x = np.linspace(-20, 20, size)
        y = np.linspace(-20, 20, size)

        x, y = np.meshgrid(x, y)
        z = (A / (2 * np.pi * sigma_x * sigma_y) * np.exp(-(x ** 2 / (2 * sigma_x ** 2)
                                                           + y ** 2 / (2 * sigma_y ** 2))))
        fig, ax = plt.subplots()
        ax = self.canvas.figure.add_subplot(111)
        ax.contourf(x, y, z, cmap=cm.gist_gray)
        self.canvas.draw()

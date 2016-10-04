""" Katie Lunceford
"""

import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, list1, list2 = []):
        if list2 == []:
            self.y = list1
            self.x = [i + 1 for i in range(len(list1))]
        else:
            self.x = list1
            self.y = list2

    def scatterPlot(self):
        area = np.pi*15
        plt.scatter(self.x, self.y, s = area)
        plt.show()

    def barGraph(self):
        plt.bar(self.x, self.y, width = 0.5, align = 'center')
        plt.show()



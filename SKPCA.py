"""This file contains the starting block for PCA in scikit
    You will need to add functions/methods to convert data into needed format,
    See treedemo.py
"""

import pandas as pd
import numpy as np
from sklearn import decomposition
import math as math
import matplotlib.pyplot as plt

class SKPCA:

    def __init__(self):
        self.pca_h = None
        self.ncomp = 0
        self.labels = None
        self.X = None

    def train(self, data, labels, ncomp):
        """Data is a 2d data list.
           Each row in the 2dlist is sample (all samples probably of a word)
           The first column is the label idenity the sample ("A")
           labels are where the sample came frome, such as from JamesJoyce sisters
        """
        self.ncomp = ncomp
        self.labels = labels

        #Strip the first column
        x = [None]*len(data)
        y = [None]*len(data)
        
        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t


        self.pca_h = decomposition.PCA(ncomp)
        self.pca_h.fit(x)
        self.X = self.pca_h.transform(x)


    def eval(self, data):

        #Strip the first column
        x = [None]*len(data)
        y = [None]*len(data)
        
        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t


         #2 by number of test authors
        
        test = self.pca_h.transform(x)
        x = []
        y = []
        for i in range(len(self.X)):
            x.append(self.X[i,0])
            y.append(self.X[i,1])
        x.append(test[0,0])
        y.append(test[0,1])
        colors = [0]*len(self.X) + [0.7]
        plt.scatter(x,y, c = colors, s = 100)
        plt.show()
         
         #find distance btween all of test and self.X
         #Select one with smallest distance
        ind = 0
        x1 = float(test[0,0])
        x2 = float(test[0,1])
        y1 = float(self.X[0,0])
        y2 = float(self.X[0,1])
        m = math.sqrt((x1-y1)**2 + (x2-y2)**2)
        for i in range(1, len(self.X)):
            y1 = float(self.X[i,0])
            y2 = float(self.X[i,1])
            d = math.sqrt((x1-y1)**2 + (x2 - y2)**2)
            if d < m:
                m = d
                ind = i
        return i

        
        

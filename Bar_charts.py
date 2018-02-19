# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:37:15 2018

@author: Arafat
"""

import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x, y, label="Bar1", color='r')
plt.bar(x2, y2, label="Bar2", color='c')

plt.title('Bar chart')

plt.legend()

plt.show()
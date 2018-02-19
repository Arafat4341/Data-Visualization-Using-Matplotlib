# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:37:15 2018

@author: Arafat
"""

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label="First line")
plt.plot(x2, y2, label="Second line")

plt.title('Interesting graph')

plt.legend()

plt.show()
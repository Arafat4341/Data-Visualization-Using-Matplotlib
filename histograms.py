# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:37:15 2018

@author: Arafat
"""

import matplotlib.pyplot as plt

ageOfPeople = [11,12,21,22,24,52,55,56,63,65,67,68]
bins = [10,20,30,40,50,60,70,80,90,100]


plt.hist(ageOfPeople, bins, histtype='bar', rwidth=0.8)

plt.title('Histogram')

plt.legend()

plt.show()
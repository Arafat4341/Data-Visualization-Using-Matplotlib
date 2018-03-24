# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:25:47 2018

@author: Arafat
"""  
import sklearn.datasets as datasets
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

tree = DecisionTreeClassifier()
tree.fit(df, y)

dot_data = StringIO()
export_graphviz(tree, out_file=dot_data, filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
print(dot_data.getvalue())
Image(graph.create_png())

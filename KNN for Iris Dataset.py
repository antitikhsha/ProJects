#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
#import and split data
data=load_iris()
x=data.data
y=data.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
#training & preprocessing
from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=5)
clf.fit(x_train, y_train)
out=clf.predict(x_test)
print(out)
print(x_train)
print(x_test)
print(y_train)
print(y_test)
#evaluting the algorithm
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,out))
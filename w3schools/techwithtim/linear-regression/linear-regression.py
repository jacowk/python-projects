#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:46:10 2019

@author: jaco
"""

#https://techwithtim.net/tutorials/machine-learning-python/linear-regression/
#https://www.youtube.com/watch?v=45ryDIPHdGg&list=PLzMcBGfZo4-mP7qA9cagf68V06sko5otr&index=2

import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

X = np.array(data.drop([predict], 1))

y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train) # Train the AI
acc = linear.score(x_test, y_test)

print(acc)

print("Co: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(x, predictions[x], x_test[x], y_test[x])

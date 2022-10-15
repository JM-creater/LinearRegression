import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# load the data from csv
dataset = pd.read_csv("polydata_degree_2.csv")
# sort the data by area
dataset = dataset.sort_values(by=['area'])

# get input and output
x = dataset.iloc[:, 0:1].values  # starting point 0, and ends with 1
y = dataset.iloc[:, 1:2].values  # starting 1, and ends with 2. 2 is the output
print(x)
print(y)

# create the model


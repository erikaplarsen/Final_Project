import pandas as pd
from sklearn.datasets import make_regression
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

crash_data_csv = 'Resources/PrecrashData.csv'
data = pd.read_csv(crash_data_csv)
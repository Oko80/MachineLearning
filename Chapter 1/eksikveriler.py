# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#codes
#data setup

veriler = pd.read_csv("eksikveriler.csv")

#print(veriler)




#sci - kit learn
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values="NaN", strategy = "mean", axis=0)

Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])    
Yas[:,1:4] = imputer.transform(Yas[:,1:4])  
print(Yas)
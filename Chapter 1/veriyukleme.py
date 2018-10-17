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

veriler = pd.read_csv("veriler.csv")

print(veriler)


boy = veriler[["boy"]]

print(boy)
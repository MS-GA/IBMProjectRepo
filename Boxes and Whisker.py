# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:45:57 2021

@author: msivakumar
"""

import matplotlib as plt
from matplotlib import pyplot
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np


#import matplotlib.pyplot as plt

boxprops = dict(linestyle='-', linewidth=4, color='k')
medianprops = dict(linestyle='-', linewidth=4, color='k')

# path = "C:/Users/msivakumar/Documents/Py/Data/Shipped_2019_Rem10and10000.csv"
# header_list=['accountid', 'shippedmonth', 'shipments']
# df = pd.read_csv(path, names=header_list) 
# boxplot = df.boxplot(column=['shipments'])

# path = "C:/Users/msivakumar/Documents/Py/Data/DaystoCancel.csv"
# header_list=['2019', '2020', '2021']
# df = pd.read_csv(path, names=header_list) 
# boxplot = df.boxplot(column=['2019','2020','2021'])
# boxplot.set_ylabel("Days")
# boxplot.set_title("Days before cancellation")


# path = "C:/Users/msivakumar/Documents/Py/Data/shipmentslessthan10000_ 2019_2021.csv"
# header_list=['2019', '2020', '2021']
# df = pd.read_csv(path, names=header_list) 
# boxplot = df.boxplot(column=['2019','2020','2021'])
# boxplot.set_ylabel("Shipments")
# boxplot.set_title("Shipping variations - >10 and <10000")

# path = "C:/Users/msivakumar/Documents/Py/Data/shipmentslessthan2000_ 2019_2021.csv"
# header_list=['2019', '2020', '2021']
# df = pd.read_csv(path, names=header_list) 
# boxplot = df.boxplot(column=['2019','2020','2021'])
# boxplot.set_ylabel("Shipments")
# boxplot.set_title("Shipping variations - <2000")

path = "C:/Users/msivakumar/Documents/Py/Data/shipments 2021.csv"
header_list=['1000', '2000', '5000','10000', '50000']
df = pd.read_csv(path, names=header_list) 
hist = df.hist(bins=5, column='1000')
for ax in hist.flatten():
    ax.set_xlabel("Shipments")
    ax.set_ylabel("Accounts")
hist = df.hist(bins=5, column='2000')
for ax in hist.flatten():
    ax.set_xlabel("Shipments")
    ax.set_ylabel("Accounts")
hist = df.hist(bins=5, column='5000')
for ax in hist.flatten():
    ax.set_xlabel("Shipments")
    ax.set_ylabel("Accounts")
hist = df.hist(bins=5, column='10000')
for ax in hist.flatten():
    ax.set_xlabel("Shipments")
    ax.set_ylabel("Accounts")
hist = df.hist(bins=5, column='50000')
for ax in hist.flatten():
    ax.set_xlabel("Shipments")
    ax.set_ylabel("Accounts")

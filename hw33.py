# data cleaning

import csv
import pandas as pd

df = pd.read_csv("main.csv")

del df["luminosity"]
del df["NAN"]

df.to_csv('hw33.csv')
import os
import pandas as pd
import re

source = "data/csvs/2326.csv"
df = pd.read_csv(source)
df.columns = df.columns.str.strip()
df = df[(df["Q_RR"]==0) & (df["DATE"].astype(str).str.startswith("2014"))]
rr = df["RR"].mean()
print(rr)


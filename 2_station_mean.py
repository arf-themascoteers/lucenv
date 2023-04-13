import os
import pandas as pd
import re

source = "data/csvs"
rainfall = []
for file in os.listdir(source):
    f = os.path.join(source, file)
    df = pd.read_csv(f)
    df.columns = df.columns.str.strip()
    df = df[(df["Q_RR"]==0) & (df["DATE"].astype(str).str.startswith("2014"))]
    rr = df["RR"].mean()
    stid = int(re.findall("[0-9]+", file)[0])
    rainfall.append([stid, rr])

df = pd.DataFrame(data=rainfall, columns=["stid","rr"])
df.to_csv("data/meanrr.csv", index=False)



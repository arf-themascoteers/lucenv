import os
from io import StringIO
import pandas as pd
import re


def extract_id(filename):
    pattern = "[0-9]+"
    x = re.findall(pattern, filename)
    if len(x) == 0:
        return None
    return int(x[0])

data = []

for filename in os.listdir("ECA_blend_rr"):
    the_id = extract_id(filename)
    if the_id is None:
        continue
    path = os.path.join("ECA_blend_rr", filename)
    f = open(path,"r")
    content = f.read()
    search_text = "See files sources.txt and stations.txt for more info."
    index = content.find(search_text)
    start = index + len(search_text)
    csv_content = content[start:]
    csv_content = csv_content.strip()
    csv_content_io = StringIO(csv_content)
    df = pd.read_csv(csv_content_io, sep=",")
    f.close()

    df.columns = df.columns.str.strip()
    rainfall_points = []
    for index, row in df.iterrows():
        qrr = row["Q_RR"]
        if qrr != 0:
            continue
        date = str(row["DATE"])
        if not date.startswith("2014"):
            continue
        rr = row["RR"]
        rainfall_points.append(rr)
        if len(rainfall_points) == 0:
            print(f"No point for {the_id}")
            continue
        avg = sum(rainfall_points)/len(rainfall_points)
        data.append([the_id, avg])

df = pd.DataFrame(data=data, columns=["STAID","RF"])
df.to_csv("rf.csv", index=False)

import pandas as pd
from haversine import haversine, Unit
import numpy as np

NAN = -9999

rrs_file = "data/rrs_sorted.csv"
vis_file = "data/vis_sorted.csv"

rrs_df = pd.read_csv(rrs_file)
vis_df = pd.read_csv(vis_file)
vis_df["rr"] = NAN
vis_df["distance"] = NAN

for vis_index in range(len(vis_df)):
    vis_row = vis_df.iloc[vis_index]
    vis_c = (vis_row["lon"],vis_row["lat"])
    distances = np.zeros(len(rrs_df))
    for rrs_index in range(len(rrs_df)):
        rrs_row = rrs_df.iloc[rrs_index]
        rrs_c = (rrs_row["lon"], vis_row["lat"])
        distances[rrs_index] = haversine(vis_c, rrs_c)
    min_index = np.argmin(distances)
    vis_df.at[vis_index,"rr"] = rrs_df.iloc[min_index]["rr"]
    vis_df.at[vis_index,"distance"] = distances[min_index]
    if vis_index%100 == 0:
        print(vis_index)


vis_df = vis_df[["665","560","490","point_id","coarse","clay","sand","silt","phc","phh","ec","caco3","p","n","k"
    ,"elevation","lc1","lu1","stones","lon","lat","rr","distance","oc"]]
vis_df.to_csv("data/final.csv",index=False)




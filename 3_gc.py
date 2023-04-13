import os
import pandas as pd

rr_file = "data/meanrr.csv"
station_file = "data/stations.csv"

rr_df = pd.read_csv(rr_file)
station_df = pd.read_csv(station_file)

rr_df = rr_df.merge(station_df, how="inner", left_on="stid")


import os
import pandas as pd

def dms_to_decimal_lat(dms):
    degrees, minutes, seconds = [float(i) for i in dms.split(':')]
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    return decimal

def dms_to_decimal_lon(dms):
    degrees, minutes, seconds = [float(i) for i in dms.split(':')]
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if decimal > 180:
        decimal = decimal - 360
    return decimal


rr_file = "data/meanrr.csv"
station_file = "data/stations.csv"

rr_df = pd.read_csv(rr_file)
station_df = pd.read_csv(station_file)

rr_df = rr_df[(~(rr_df["rr"].isna()))]
rr_df = rr_df.merge(station_df, how="inner", left_on="stid", right_on="STAID")
rr_df = rr_df.drop(columns=["STAID"], axis=1)
rr_df.columns = rr_df.columns.str.strip()
for i in range(len(rr_df)):
    rr_df.at[i,'LAT'] = dms_to_decimal_lat(rr_df.iloc[i]['LAT'])
    rr_df.at[i,'LON'] = dms_to_decimal_lon(rr_df.iloc[i]['LON'])
rr_df = rr_df[["stid","rr","LON","LAT"]]
rr_df = rr_df.set_axis(["stid","rr","lon","lat"], axis=1)
rr_df.to_csv("data/rrs.csv",index=False)


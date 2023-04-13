import os
import pandas as pd

vis = pd.read_csv("data/vis_with_empty.csv")
vis = vis.sort_values(['lon', 'lat'],ascending = [False, True])
vis.to_csv("data/vis_sorted.csv", index=False)

vis = pd.read_csv("data/rrs.csv")
vis = vis.sort_values(['lon', 'lat'],ascending = [False, True])
vis.to_csv("data/rrs_sorted.csv", index=False)


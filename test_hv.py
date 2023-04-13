import haversine as hs

loc1=(28.426846,77.088834)
loc2=(28.394231,77.050308)
x = hs.haversine(loc1,loc2)

print(x)
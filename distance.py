from geopy.distance import geodesic


sds = geodesic((4.667982,-74.103693),(5.465616,-74.653929))

sds = str(sds)
sds = sds.split(' ')
distancia = float(sds[0])
dis = distancia * 1.60934

print(dis)

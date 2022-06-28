from unittest import result
from geopy.distance import geodesic


def calcular_distancia(cords_set_1, cords_set_2):
    distancia = (str(geodesic(cords_set_1, cords_set_2))).split(' ')
    result = (float(distancia[0]))*1000
    result = float("{:.3f}".format(result))
    return result

print(calcular_distancia((4.6764531,-74.0652501),(4.6764511,-74.0652501)))
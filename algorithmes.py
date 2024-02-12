import numpy as np
from numpy import append

import donnes
from math import radians, cos, sin, asin, sqrt


def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return round(c * r, 4)


def dist_from(coordennees):
    dist = []
    for i in range(len(coordennees)):
        for j in range(len(coordennees)):
            lat1 = float(coordennees[i]['lat'])
            lon1 = float(coordennees[i]['lon'])
            lat2 = float(coordennees[j]['lat'])
            lon2 = float(coordennees[j]['lon'])

            dist.append(haversine(lat1, lon1, lat2, lon2))

        coordennees[i]['dist'] = dist
        dist = []
    return coordennees


def nearest_neighbors(coordennees):
    pp = 1000
    ipp = 0

    for i in range(len(coordennees)):
        for j in range(len(coordennees)):
            if coordennees[i]['dist'][j] < pp and coordennees[i]['dist'][j] != 0.0:

                pp= coordennees[i]['dist'][j]
                ipp = j
                print(j)
    # print(ipp)


if __name__ == '__main__':
    coordennees = dist_from(donnes.coordennees)
    print(coordennees)

    nearest_neighbors(coordennees)

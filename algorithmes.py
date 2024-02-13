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


def dist_from(city1, city2):
    dist = haversine(float(city1[0]), float(city1[1]), float(city2[0]), float(city2[1]))
    return dist


# def nearest_neighbors(coordennees):
#     dist_max = 10000
#     nearest = [0*len(coordennees)]
#     for i in range(len(coordennees)):
#         temp = 0
#         for j in range(len(coordennees)):
#             if dist_from(donnes.coordennees[i], donnes.coordennees[j]) < dist_max and dist_from(donnes.coordennees[i], donnes.coordennees[j]) != 0.0:
#                 dist_max = dist_from(donnes.coordennees[i], donnes.coordennees[j])
#                 temp = j
#         nearest.append(coordennees[temp])
#         coordennees.pop()
#     print(nearest)

def path_distance(route, cities):
    list_dist = []
    temp = 1
    for j in route:
        if temp < len(route):
            dist = haversine(float(cities[j][0]), float(cities[j][1]), float(cities[route[temp]][0]),
                             float(cities[route[temp]][1]))
            list_dist.append(dist)
        temp = temp + 1
    sum_dist = sum(list_dist)
    # print(list_dist)
    # print(sum_dist)
    return sum_dist


def swap(listVille, i, j):
    listVille[i], listVille[j] = listVille[j], listVille[i]
    return listVille


def two_opt(cities):
    route = np.arange(cities.shape[0])
    best_distance = path_distance(route, cities)
    for swap_first in range(1, len(route)-2):
        for swap_last in range(swap_first + 1, len(route)):
            new_route = swap(route, 0, len(route) - 1)
            new_distance = path_distance(new_route, cities)
            if new_distance < best_distance:
                route = new_route
                best_distance = new_distance

    print(route)
    return route


if __name__ == '__main__':
    cities = np.array(donnes.coordennees)
    route = np.arange(cities.shape[0])
    route2=[23,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,0]
    route = two_opt(cities)

    # path_distance(route, cities)

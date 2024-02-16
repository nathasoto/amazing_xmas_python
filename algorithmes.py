# import numpy as np
# from numpy import append
# import pandas as pd
# import donnes
# from math import radians, cos, sin, asin, sqrt
# import folium
#
#
#
# def haversine(lat1, lon1, lat2, lon2):
#     """
#     Calculate the great circle distance in kilometers between two points
#     on the earth (specified in decimal degrees)
#     """
#     # convert decimal degrees to radians
#     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
#
#     # haversine formula
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#     a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
#     c = 2 * asin(sqrt(a))
#     r = 6371  # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
#     return round(c * r, 4)
#
# def matriz_dist(coordinates):
#     dist = []
#     matriz = []
#     for i in range(len(coordinates)):
#         for j in range(1, len(coordinates)):
#             dist.append(haversine((float(coordinates[i][0]), float(coordinates[i][1])),
#                                   (float(coordinates[j][0]), float(coordinates[j][1]))))
#         matriz.append(dist)
#         dist = []
#     print(np.asarray(matriz))
#
# def dist_from(city1, city2):
#     dist = haversine(float(city1[0]), float(city1[1]), float(city2[0]), float(city2[1]))
#     return dist
#
#
# # def nearest_neighbors(coordennees):
# #     dist_max = 10000
# #     nearest = [0*len(coordennees)]
# #     for i in range(len(coordennees)):
# #         temp = 0
# #         for j in range(len(coordennees)):
# #             if dist_from(donnes.coordennees[i], donnes.coordennees[j]) < dist_max and dist_from(donnes.coordennees[i], donnes.coordennees[j]) != 0.0:
# #                 dist_max = dist_from(donnes.coordennees[i], donnes.coordennees[j])
# #                 temp = j
# #         nearest.append(coordennees[temp])
# #         coordennees.pop()
# #     print(nearest)
#
# def path_distance(route, cities):
#     list_dist = []
#     temp = 1
#     for j in route:
#         if temp < len(route):
#             dist = haversine(float(cities[j][0]), float(cities[j][1]), float(cities[route[temp]][0]),
#                              float(cities[route[temp]][1]))
#             list_dist.append(dist)
#         temp = temp + 1
#     sum_dist = sum(list_dist)
#     # print(list_dist)
#     # print(sum_dist)
#     return sum_dist
#
#
# def swap(listVille, i, j):
#     listVille[i], listVille[j] = listVille[j], listVille[i]
#     return listVille
#
#
# def two_opt(cities):
#     route = np.arange(cities.shape[0])
#     best_distance = path_distance(route, cities)
#     for swap_first in range(1, len(route) - 2):
#         for swap_last in range(swap_first + 1, len(route)):
#             new_route = swap(route, swap_first, swap_last)
#             new_distance = path_distance(new_route, cities)
#             if new_distance < best_distance:
#                 route = new_route
#                 best_distance = new_distance
#
#     print(route)
#     print(best_distance)
#     return route
#
#
# def transfor_route_to_cities(route, list_donnes):
#     list_cities = []
#     for i in route:
#         list_cities.append(list_donnes[i])
#     return list_cities
#
#
# # def two_opt_better(cities, improvement_threshold):
# #     route = np.arange(cities.shape[0])
# #     improvement_factor = 1
# #     best_distance = path_distance(route, cities)
# #     while improvement_factor > improvement_threshold:
# #         distance_to_beat = best_distance
# #         for swap_first in range(1, len(route) - 2):
# #             for swap_last in range(swap_first + 1, len(route)):
# #                 new_route = swap(route, swap_first, swap_last)
# #                 new_distance = path_distance(new_route, cities)
# #                 if new_distance < best_distance:
# #                     route = new_route
# #                     best_distance = new_distance
# #         improvement_factor = 1 - best_distance / distance_to_beat
# #     print(route)
# #     print(best_distance)
# #     return route
#
#
# if __name__ == '__main__':
#     # read csv
#     df = pd.read_csv('70villes.csv', header=0, delimiter=',')
#     # convert df to list
#     list_donnes = df.values.tolist()
#
#     # print(list_donnes)
#
#     cities = np.array(donnes.coordennees)
#     route_normal = two_opt(cities)
#
#     donnes_organize = transfor_route_to_cities(route_normal, donnes.coordennees)
#
#     print(donnes_organize)
#
#     m = folium.Map((45.166672, 5.71667), zoom_start=12)
#     for i in range(len(donnes.coordennees)):
#         # # Adding markers
#         folium.Marker(
#             location=[donnes.coordennees[i][0], donnes.coordennees[i][1]],
#             tooltip="Click me!",
#             popup="Timberline Lodge",
#             icon=folium.Icon(color='red')
#         ).add_to(m)
#         m.save("index.html")
#
#
#     trail_coordinates = [
#     [45.171112, 5.695952],
#     [45.183152, 5.699386],
#     [45.174115, 5.711106],
#     [45.176123, 5.722083],
#     [45.184301, 5.719791],
#     [45.184252, 5.730698],
#     [45.170588, 5.716664],
#     [45.193702, 5.691028],
#     [45.165641, 5.739938],
#     [45.178718, 5.744940],
#     [45.176857, 5.762518],
#     [45.188512, 5.767172],
#     [45.174017, 5.706729],
#     [45.174458, 5.687902],
#     [45.185110, 5.733667],
#     [45.185702, 5.734507],
#     [45.184726, 5.734666],
#     [45.184438, 5.733735],
#     [45.184902, 5.735256],
#     [45.174812, 5.698095],
#     [45.169851, 5.695723],
#     [45.180943, 5.698965],
#     [45.176205, 5.692165],
#     [45.171244, 5.689872]
# ]
#
#     folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)
#     m.save("index.html")
#
#  # cost_actual =dist_from(coordinates[i], coordinates[i+1])+dist_from(coordinates[j], coordinates[j+1])
# # cost_nuevo = dist_from(coordinates[i], coordinates[j]) + dist_from(coordinates[i+1], coordinates[j + 1])



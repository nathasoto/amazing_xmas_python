import math

import numpy as np
from haversine import haversine


def get_distance_matrix(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = haversine((float(cities[i][0]), float(cities[i][1])), (float(cities[j][0]), float(cities[j][1])))
            distances[i][j] = int(dist)
            distances[j][i] = int(dist)
    return distances


def solve_tsp_nearest(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = []
    total_distance = 0

    # Start at the first city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True

    # Repeat until all cities have been visited
    while len(tour) < num_cities:
        nearest_city = None
        nearest_distance = math.inf

        # Find the nearest unvisited city
        for city in range(num_cities):
            if not visited[city]:
                distance = distances[current_city][city]
                if distance < nearest_distance:
                    nearest_city = city
                    nearest_distance = distance

        # Move to the nearest city
        current_city = nearest_city
        tour.append(current_city)
        visited[current_city] = True
        total_distance += nearest_distance

    # Complete the tour by returning to the starting city
    tour.append(0)
    total_distance += distances[current_city][0]

    return tour


def transfor_route_to_cities(route, list_donnes):
    list_cities = []
    for i in route:
        list_cities.append(list_donnes[i])
    return list_cities


def path_distance(coordinates):
    list_dist = []
    for i in range(len(coordinates)):
        if i + 1 < len(coordinates):
            dist = haversine((float(coordinates[i][0]), float(coordinates[i][1])),
                             (float(coordinates[i + 1][0]), float(coordinates[i + 1][1])))
            list_dist.append(dist)
    sum_dist = sum(list_dist)
    # print(list_dist)
    # print(sum_dist)
    return sum_dist


def two_opt2(coordinates):
    min_change = 0
    for i in range(len(coordinates) - 2):
        for j in range(i + 2, len(coordinates) - 1):

            cost_actual = haversine((float(coordinates[i][0]), float(coordinates[i][1])),
                                    (float(coordinates[i + 1][0]), float(coordinates[i + 1][1]))) + haversine(
                (float(coordinates[j][0]), float(coordinates[j][1])),
                (float(coordinates[j + 1][0]), float(coordinates[j + 1][1])))
            cost_nuevo = haversine((float(coordinates[i][0]), float(coordinates[i][1])),
                                   (float(coordinates[j][0]), float(coordinates[j][1]))) + haversine(
                (float(coordinates[i + 1][0]), float(coordinates[i + 1][1])),
                (float(coordinates[j + 1][0]), float(coordinates[j + 1][1])))
            change = cost_nuevo - cost_actual

            if change < min_change:
                min_change = change
                min_i = i
                min_j = j
    if min_change < 0:
        coordinates[min_i + 1:min_j + 1] = coordinates[min_i + 1:min_j + 1][::-1]

    return coordinates


def two_opt(solution):
    change = 1
    while change != 0:
        inicial = path_distance(solution)
        solution = two_opt2(solution).copy()
        final = path_distance(solution)
        change = np.abs(final - inicial)
    return solution

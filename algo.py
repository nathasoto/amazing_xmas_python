import numpy as np
from haversine import haversine, Unit


def path_distance(coordinates):
    list_dist = []
    for i in range(len(coordinates)):
        if i + 1 < len(coordinates):
            dist = haversine((float(coordinates[i][0]), float(coordinates[i][1])),
                             (float(coordinates[i + 1][0]), float(coordinates[i + 1][1])))
            list_dist.append(dist)
    sum_dist = sum(list_dist)
    # print(list_dist)
    print(sum_dist)
    return sum_dist


def swap(listVille, i, j):
    listVille[i], listVille[j] = listVille[j], listVille[i]
    return listVille


def two_opt(coordinates):
    best_distance = path_distance(coordinates)
    for swap_first in range(1, len(coordinates) - 2):
        for swap_last in range(swap_first + 1, len(coordinates)):
            new_route = swap(coordinates, swap_first, swap_last)
            new_distance = path_distance(new_route)
            if new_distance < best_distance:
                coordinates= new_route
                best_distance = new_distance

    print(coordinates)
    print(best_distance)
    return coordinates

def matriz_dist(coordinates):
    dist =[]
    matriz =[]
    for i in range(len(coordinates)):
        for j in range(1,len(coordinates)):
               dist.append(haversine((float(coordinates[i][0]), float(coordinates[i][1])),
                             (float(coordinates[j][0]), float(coordinates[j][1]))))
        matriz.append(dist)
        dist=[]
    print(np.asarray(matriz))


def two_opt2(NN):
    min_change = 0

    for i in range(len(NN)-2):
        for j in range(i+2, len(NN)-1):
            city1 = NN[i]
            city2=  NN[i+1]
            dist1 = haversine((float(city1[0]), float(city1[1])), (float(city2[0]),float(city2[1])))
            city3= NN[j]
            city4= NN[j+1]
            dist2= haversine((float(city3[0]), float(city3[1])), (float(city4[0]),float(city4[1])))
            cost_actual =  dist1 + dist2
            # cost_actual =dist_from(NN[i], NN[i+1])+dist_from(NN[j], NN[j+1])
            dist3= haversine((float(city1[0]), float(city1[1])), (float(city3[0]),float(city3[1])))
            dist4= haversine((float(city2[0]), float(city2[1])), (float(city4[0]),float(city4[1])))
            cost_nuevo = dist3 + dist4
            # cost_nuevo = dist_from(NN[i], NN[j]) + dist_from(NN[i+1], NN[j + 1])
            change = cost_nuevo - cost_actual

            if change  < min_change:
                min_change = change
                min_i = i
                min_j = j
    if min_change < 0:
        NN[min_i+1:min_j+1] =  NN[min_i+1:min_j+1][::-1]

    return NN

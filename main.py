from csv import reader
import folium
import numpy as np

import algo


def csv_to_list(file_csv):
    with open(file_csv) as csv_file:
        csv_reader = reader(csv_file)
        list_coordinates = list(csv_reader)
        del list_coordinates[0]
        return list_coordinates


def deploy_point(m, coord):
    for i in range(len(coord)):
        # # Adding markers
        folium.Marker(
            location=[coord[i][0], coord[i][1]],
            tooltip="Click me!",
            popup="Timberline Lodge",
            icon=folium.Icon(color='red')
        ).add_to(m)
    m.save("index.html")


def deploy_lines(m, coord):
    trail_coordinates = [coord]
    folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)
    m.save("index.html")


# '70villes.csv'
# 'coordinates.csv'

coordinates = csv_to_list('70villes.csv')
map = folium.Map((45.166672, 5.71667), zoom_start=12)

# deploy_point(map,coordinates)
# deploy_lines(map,coordinates)

# new_coordinates =algo.two_opt(coordinates)
# deploy_point(map,new_coordinates)
# deploy_lines(map,new_coordinates)


# new_coordinates = algo.two_opt2(coordinates)
# # print(coordinates)
# # deploy_point(map,new_coordinates)
# # deploy_lines(map,new_coordinates)

sol = coordinates.copy()
cambio=1
count =0
while cambio != 0:
    count = count +1
    inicial= algo.path_distance(sol)
    sol=algo.two_opt2(sol).copy()
    final = algo.path_distance(sol)
    cambio=np.abs(final-inicial)
print(sol)
deploy_point(map,sol)
deploy_lines(map,sol)
from csv import reader
import folium

import algo
from genetic_algorithm import genetic_algorithm


def csv_to_list(file_csv):
    with open(file_csv) as csv_file:
        csv_reader = reader(csv_file)
        list_coordinates = list(csv_reader)
        del list_coordinates[0]
        return list_coordinates


def deploy_point(m, coord, name):
    for i in range(len(coord)):
        # # Adding markers
        folium.Marker(
            location=[coord[i][0], coord[i][1]],
            tooltip="Click me!",
            popup="Timberline Lodge",
            icon=folium.Icon(color='red')
        ).add_to(m)
    m.save(f'{name}.html')


def deploy_lines(m, coord, name):
    trail_coordinates = [coord]
    folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)
    m.save(f'{name}.html')


# '70villes.csv'
# 'coordinates.csv'

coordinates = csv_to_list('70villes.csv')
# map_original = folium.Map((45.166672, 5.71667), zoom_start=12)
#
# deploy_point(map_original, coordinates, 'original')
# deploy_lines(map_original, coordinates, 'original')
#
# map_two_opt = folium.Map((45.166672, 5.71667), zoom_start=12)
#
# solution_two_opt = algo.two_opt(coordinates)
# print(solution_two_opt)
#
# deploy_point(map_two_opt, solution_two_opt, 'two_opt')
# deploy_lines(map_two_opt, solution_two_opt, 'two_opt')
#
# map_nearest = folium.Map((45.166672, 5.71667), zoom_start=12)
#
# solution = algo.get_distance_matrix(coordinates)
# tour = algo.solve_tsp_nearest(solution)
# solution_nearest_neighbor = algo.transfor_route_to_cities(tour, coordinates)
#
#
# deploy_point(map_nearest, solution_nearest_neighbor, 'tsp_nearest')
# deploy_lines(map_nearest, solution_nearest_neighbor, 'tsp_nearest')



map_genetic_algorithm = folium.Map((45.166672, 5.71667), zoom_start=12)
#
# Run the genetic algorithm
best_tour, best_distance = genetic_algorithm()
solution = algo.transfor_route_to_cities(best_tour,coordinates)

deploy_point(map_genetic_algorithm, solution, 'genetic algorithm')
deploy_lines(map_genetic_algorithm, solution, 'genetic algorithm')

# Print the results
print("Best tour:", solution)
print("Best distance:", best_distance)

import random
import numpy as np
import pandas as pd
from haversine import haversine, Unit

# Read latitude and longitude data from CSV file
data = pd.read_csv('70villes.csv')  # Replace 'your_data.csv' with your actual CSV file

# Extract latitude and longitude columns
latitude = data['latitude'].values
longitude = data['longitude'].values

# Create a distance matrix based on Haversine distance
def calculate_haversine_distance(lat1, lon1, lat2, lon2):
    return haversine((lat1, lon1), (lat2, lon2), unit=Unit.KILOMETERS)

# Genetic Algorithm parameters
population_size = 70
generations = 8000
crossover_probability = 0.8
mutation_probability = 0.2
elite_size = 30
crossover_size = population_size - elite_size
mutate_size = population_size - elite_size

# Function to calculate the total distance of a tour
def calculate_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Return to the starting city
    return total_distance

# Function to initialize a population of tours
def generate_initial_population(size):
    population = []
    for _ in range(size):
        route = list(range(num_cities))
        random.shuffle(route)
        population.append(route)
    return population
def evolve_population(population):
    ranked_population = sorted(population, key=lambda x: calculate_distance(x))
    elite = ranked_population[:elite_size]
    selection = random.sample(ranked_population[elite_size:], population_size - elite_size)

    new_population = elite

    for _ in range(crossover_size):
        parent1, parent2 = random.sample(selection, 2)
        crossover_point = random.randint(0, num_cities - 1)
        child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
        new_population.append(child)

    for _ in range(mutate_size):
        mutate_point = random.randint(0, population_size - 1)
        mutation = list(new_population[mutate_point])
        idx1, idx2 = random.sample(range(num_cities), 2)
        mutation[idx1], mutation[idx2] = mutation[idx2], mutation[idx1]
        new_population[mutate_point] = mutation

    return new_population
def initialize_population(size):
    population = generate_initial_population(size)
    for _ in range(generations):
        population = evolve_population(population)

    ranked_population = sorted(population, key=lambda x: calculate_distance(x))
    return ranked_population[:min(10, size)]

# Function for tournament selection
def tournament_selection(population, k=5):
    tournament = random.sample(population, k)
    return min(tournament, key=calculate_distance)

# Function for ordered crossover (OX) crossover
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [-1] * len(parent1)
    child[start:end] = parent1[start:end]
    remaining = [city for city in parent2 if city not in child]
    index = 0
    for i in range(len(child)):
        if child[i] == -1:
            child[i] = remaining[index]
            index += 1
    return child

# Function for mutation (swap mutation)
def mutate(tour):
    index1, index2 = sorted(random.sample(range(len(tour)), 2))
    tour[index1], tour[index2] = tour[index2], tour[index1]
    return tour

# Genetic Algorithm
def genetic_algorithm():
    population = initialize_population(population_size)

    for generation in range(generations):
        population = sorted(population, key=calculate_distance)
        new_population = [tournament_selection(population) for _ in range(population_size)]

        for i in range(0, population_size, 2):
            if random.random() < crossover_probability:
                child1 = crossover(new_population[i], new_population[i + 1])
                child2 = crossover(new_population[i + 1], new_population[i])
                new_population[i] = child1
                new_population[i + 1] = child2

        for i in range(population_size):
            if random.random() < mutation_probability:
                new_population[i] = mutate(new_population[i])

        population = new_population

    best_tour = min(population, key=calculate_distance)
    best_distance = calculate_distance(best_tour)
    return best_tour, best_distance

# Create a distance matrix using Haversine distance
num_cities = len(latitude)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calculate_haversine_distance(latitude[i], longitude[i], latitude[j], longitude[j])



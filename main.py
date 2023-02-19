import numpy as np
import random
import matplotlib.pyplot as plt


def calculate_delivery_costs(people, depots):

    total_cost = 0
    built_depots = [False] * len(depots)
    clusters = [[] for i in range(len(depots))]

    for person in people:

        distances = [np.linalg.norm(person - depot)
                     for depot in depots if np.linalg.norm(person - depot)]

        if (np.min(distances) > 150):
            continue

        cluster_index = np.argmin(distances)

        sorted_distances = sorted(distances)
        for i, distance in enumerate(sorted_distances[0:3]):
            if built_depots[cluster_index] == False and built_depots[distances.index(distance)] == True:
                cluster_index = distances.index(distance)

        built_depots[cluster_index] = True
        clusters[cluster_index].append(person)

        min_cost = distances[cluster_index]
        total_cost += min_cost

    for depot in built_depots:
        if depot == True:
            total_cost += 2500

    return total_cost


def main():
    depots = []
    people = []

    with open("depotP22.txt", "r") as f:
        n = int(f.readline())
        for i in range(n):
            depots.append([int(x) for x in f.readline().strip().split(" ")])
    with open("depotP317.txt", "r") as f:
        n = int(f.readline())
        for i in range(n):
            depots.append([int(x) for x in f.readline().strip().split(" ")])

    with open("p22.txt", "r") as f:
        n = int(f.readline())
        for i in range(n):
            people.append([int(x) for x in f.readline().strip().split(" ")])

    with open("p317.txt", "r") as f:
        n = int(f.readline())
        for i in range(n):
            people.append([int(x) for x in f.readline().strip().split(" ")])

    depots = np.array(depots)
    people = np.array(people)

    print(calculate_delivery_costs(people, depots))


main()

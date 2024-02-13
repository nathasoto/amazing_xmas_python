import numpy as np

import donnes


def cost_change(cost_mat, n1, n2, n3, n4):
    return cost_mat[n1][n3] + cost_mat[n2][n4] - cost_mat[n1][n2] - cost_mat[n3][n4]


def two_opt(route, cost_mat):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                if cost_change(cost_mat, best[i - 1], best[i], best[j - 1], best[j]) < 0:
                    best[i:j] = best[j - 1:i - 1:-1]
                    improved = True
        route = best
    return best


if __name__ == '__main__':
    # nodes = 4
    # init_route = list(range(nodes))
    # print(init_route)
    # cost_mat = np.random.randint(100, size=(nodes, nodes))
    # print(cost_mat)
    # cost_mat += cost_mat.T
    # print(cost_mat)
    # np.fill_diagonal(cost_mat, 0)
    # print(cost_mat)
    # cost_mat = list(cost_mat)
    # print(cost_mat)

    # best_route = two_opt(init_route, cost_mat)
    # print(best_route)

    cities = np.array(donnes.coordennees)
    route = np.arange(cities.shape[0])
    two_opt(cities, 0.001)
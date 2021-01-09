
def doTsp(dist_adj_matrix):
    import numpy as np
    from python_tsp.heuristics import solve_tsp_simulated_annealing

    dist_matrix = np.array(dist_adj_matrix)

    # Do TSP
    path_idx, distance = solve_tsp_simulated_annealing(dist_matrix)
    # path_idx = ind of nodes in adj-matrix,

    print("TSP Order of node indices to be traversed: ", path_idx)
    print("Total distance traversed: ", distance)

from data_manchester import dist_adj_matrix, dist_adj_matrix_after_weight

print("original graph")
doTsp(dist_adj_matrix)

print("edges reduced by 0.9 graph")
doTsp(dist_adj_matrix_after_weight)
    
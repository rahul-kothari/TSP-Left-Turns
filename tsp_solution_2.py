from reduce_graph_for_tsp import dijkstra_on_all_pair_of_nodes
import osmnx as ox
import numpy as np
from tsp_solver.greedy import solve_tsp
from dijkstra_shortest_path import dijkstra
from python_tsp.heuristics import solve_tsp_local_search
from python_tsp.heuristics import solve_tsp_simulated_annealing

def tsp_node_list(path_list, node_ids):
    loop_list = []
    for i in range(0,len(path_list)):
        if path_list[i] == 0:
            loop_list.append(node_ids[0])
        elif path_list[i] == 1:
            loop_list.append(node_ids[1])
        elif path_list[i] == 2:
            loop_list.append(node_ids[2])
        elif path_list[i] == 3:
            loop_list.append(node_ids[3])
        elif path_list[i] == 4:
            loop_list.append(node_ids[4])
    
    return(loop_list)

"""

[EMPTY...][PATH 1-0][PATH 2-0][PATH 3-0][PATH 4-0]
[PATH 0-1][EMPTY...][PATH 2-1][PATH 3-1][PATH 4-1]
[PATH 0-2][PATH 1-2][EMPTY...][PATH 3-2][PATH 4-2]
[PATH 0-3][PATH 1-3][PATH 2-3][EMPTY...][PATH 4-3]
[PATH 0-4][PATH 1-4][PATH 2-4][PATH 3-4][EMPTY...]

"""

def show_full_path(path, route_matrix, Graph):
    loop_list = []
    tsp_path_list = []
    for index, elem in enumerate(path[:-1]):
        print("GETTING PATH FROM " + str(elem) + " TO " + str(path[index+1]))
        loop_list.append(route_matrix[elem][path[index+1]])
    for i in loop_list:
        for j in i:
            tsp_path_list.append(j)
    tsp_path_list = list(dict.fromkeys(tsp_path_list))
    print(tsp_path_list)
    ox.plot.plot_graph_route(Graph, tsp_path_list)

if __name__ == "__main__":
    G = ox.graph.graph_from_xml("map-uni.osm", bidirectional=True)
    ox.bearing.add_edge_bearings(G)
    nodes =  list(G.nodes())    

    # Select n nodes with their ids:
    n1 = int(nodes[0])
    n2 = int(nodes[5])
    n3 = int(nodes[-5])
    n4 = int(nodes[-1])
    n5 = int(nodes[6])
    selected_nodes = [n1, n2, n3, n4, n5]

    result_matrix = dijkstra_on_all_pair_of_nodes(G, selected_nodes)
    adj_matrix = result_matrix[0]
    route_matrix = result_matrix[1]

    matrix = np.array(adj_matrix)

    solution = solve_tsp_simulated_annealing(matrix)

    path = solution[0]
    distance = solution[1]

    print(path)
    print(distance)
    node_list = tsp_node_list(path, selected_nodes)
    print(node_list)
    show_full_path(path, route_matrix, G)
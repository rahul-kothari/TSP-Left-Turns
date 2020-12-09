from reduce_graph_for_tsp import dijkstra_on_all_pair_of_nodes
import osmnx as ox
import numpy as np
from dijkstra_shortest_path import dijkstra
from python_tsp.heuristics import solve_tsp_local_search
from python_tsp.heuristics import solve_tsp_simulated_annealing

def tsp_node_list(path_list, node_ids):
    loop_list = []
    for i in range(0,len(path_list)):
        loop_list.append(node_ids[path_list[i]])
    
    return loop_list

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

    adj_matrix,route_matrix  = dijkstra_on_all_pair_of_nodes(G, selected_nodes)

    matrix = np.array(adj_matrix)

    path, distance = solve_tsp_simulated_annealing(matrix)

    print(path)
    print(distance)
    node_list = tsp_node_list(path, selected_nodes)
    print(node_list)
    # show_full_path(path, route_matrix, G)
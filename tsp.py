import numpy as np
from python_tsp.heuristics import solve_tsp_simulated_annealing

def tsp_node_list(path_of_nodes, node_ids):
    """
    Get OSM Node ids from the index of node in path_of_nodes.
    """
    loop_list = []
    for i in range(0,len(path_of_nodes)):
        loop_list.append(node_ids[path_of_nodes[i]])
    
    return loop_list


def get_full_tsp_path(start_node_id:int, dist_matrix:list, route_matrix:list, avoid_right_turns=False):
    """
    Given an adjacent_matrix showing distance and route to go from each pair of nodes, do TSP and get the total final path.
    """

    dist_matrix = np.array(dist_matrix)

    # Do TSP
    path_idx, distance = solve_tsp_simulated_annealing(dist_matrix)
    # path_idx = ind of nodes in adj-matrix,

    print("Node indexes to be covered: ", path_idx)
    print("Total distance traversed: ", distance)

    # final route:
    final_tsp_route = [start_node_id] 

    for i in range(len(path_idx)):
        # start with node 0 which is also the last elemet on parth_idx and go to path_idx[0]. Then path_idx[0] to path_idx[1] and so on...
        from_node_idx = path_idx[i-1]
        to_node_idx = path_idx[i]
        print("Get path from node", from_node_idx, "to node", to_node_idx)#, ": ", route_matrix[from_node_idx][to_node_idx])
        # remove the first element in route as it was the prev to_node
        final_tsp_route.extend(route_matrix[from_node_idx][to_node_idx][1:])

    return final_tsp_route, path_idx


if __name__ == "__main__":
    import osmnx as ox
    from reduce_graph_for_tsp import dijkstra_on_all_pair_of_nodes

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

    final_path, _ = get_full_tsp_path(n1, adj_matrix, route_matrix)
    print(final_path)

    ox.plot.plot_graph_route(G, final_path)
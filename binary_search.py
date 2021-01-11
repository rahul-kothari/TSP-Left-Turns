"""
Binary search for manipulating edge weights
"""
import osmnx as ox
from reduce_graph_for_tsp import dijkstra_on_all_pair_of_nodes
from manipulate_edges import manipulate_graph_edges_by_a_factor
from python_tsp.heuristics import solve_tsp_simulated_annealing
import math
import numpy as np

def binary_search():
    G = ox.graph_from_place('Liverpool, North West England, England, United Kingdom')
    ox.bearing.add_edge_bearings(G)
    
    n1 = G.nodes[416913103]
    n2 = G.nodes[338834142]
    n3 = G.nodes[423810866]
    n4 = G.nodes[27207873]
    n5 = G.nodes[60179781]
    node_ids = [n1['osmid'], n2['osmid'], n3['osmid'], n4['osmid'], n5['osmid']]
    
    dist_adj_matrix, route_matrix = dijkstra_on_all_pair_of_nodes(G, node_ids)
    path_idx, dist_traversed_no_constraints = solve_tsp_simulated_annealing(np.array(dist_adj_matrix))
    #print(dist_traversed_no_constraints)
    
    start = 0.1
    end = 0.9
    fraction = 0.5
    
    
    while(True):
        
        G_new = manipulate_graph_edges_by_a_factor(G, fraction)
        #Pretty sure this (two lines below) is wrong but I had trouble finding a better way to get the distance value
        dist_adj_matrix_new, route_matrix_new = dijkstra_on_all_pair_of_nodes(G_new, node_ids)
        path_idx, dist_traversed = solve_tsp_simulated_annealing(np.array(dist_adj_matrix_new))
        
        if (math.isclose(dist_traversed, dist_traversed_no_constraints) == True):
            break;
            
        elif  (dist_traversed > dist_traversed_no_constraints):
            #Reduce fraction
            fraction = start + (fraction / 2)
        
        else:
            #Increase fraction
            fraction = end + (fraction / 2)
    
    return fraction
    print("Fraction: ", fraction)
    

            
if __name__ == "__main__":
    binary_search()


"""
1. Import Map and select 5 nodes
2. Do Dijkstra across them all
3. Do TSP
4. Manipulate graph edges by a factor
5. Do Dijkstra on all by avoiding right turns
6. Do TSP on this
"""

import networkx as nx
import osmnx as ox
import numpy as np

from dijkstra_shortest_path import dijkstra
from reduce_graph_for_tsp import dijkstra_on_all_pair_of_nodes
from manipulate_edges import manipulate_graph_edges_by_a_factor
from tsp_solution_2 import tsp_node_list
from tsp_solution_2 import show_full_path
from python_tsp.heuristics import solve_tsp_simulated_annealing

def prettyPrintMatrix(matrix):
	print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

# STEP 1: IMport map and select nodes.
G = ox.graph_from_place('Liverpool, North West England, England, United Kingdom')
ox.bearing.add_edge_bearings(G)

n1 = G.nodes[416913103]
n2 = G.nodes[338834142]
n3 = G.nodes[423810866]
n4 = G.nodes[27207873]
n5 = G.nodes[60179781]

node_ids = [n1['osmid'], n2['osmid'], n3['osmid'], n4['osmid'], n5['osmid']]

# Step 2: Dijkstra
dijkstra_result = dijkstra_on_all_pair_of_nodes(G, node_ids)
adj_matrix = dijkstra_result[0]
route_matrix = dijkstra_result[1]
prettyPrintMatrix(adj_matrix)
#prettyPrintMatrix(route_matrix)
 
#Step 3: TSP
adj_matrix = np.array(adj_matrix)
solution = solve_tsp_simulated_annealing(adj_matrix)
path = solution[0]
distance = solution[1]

print(path)
print(distance)

node_path = tsp_node_list(path, node_ids)
print(node_path)
show_full_path(path, route_matrix, G)

# Step 4: Manipulate graph edges:
factor = 0.5
G_new = manipulate_graph_edges_by_a_factor(G, factor)
avoid_right_turns = True

# Step 5: Dijkstra when avoiding right turns
dijkstra_result_after_weight = dijkstra_on_all_pair_of_nodes(G, node_ids, avoid_right_turns=avoid_right_turns)
adj_matrix_after_weight = dijkstra_result_after_weight[0]
route_matrix_after_weight = dijkstra_result_after_weight[1]
print(adj_matrix)

# Step 6:
adj_matrix = np.array(adj_matrix)
solution_after_weight = solve_tsp_simulated_annealing(adj_matrix)
path_after_weight = solution_after_weight[0]
distance_after_weight = solution_after_weight[1]
node_path_after_weight = tsp_node_list(path_after_weight, node_ids)

print(path_after_weight)
print(distance_after_weight)
print(node_path_after_weight)

show_full_path(path_after_weight, route_matrix_after_weight, G)





 
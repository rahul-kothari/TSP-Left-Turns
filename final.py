"""
1. Import Map and select 5 nodes
2. Do Dijkstra across them all
3. Do TSP
4. Manipulate graph edges by a factor
5. Do Dijkstra on all by avoiding right turns
6. Do TSP on this
"""
import osmnx as ox
from manipulate_edges import manipulate_graph_edges_by_a_factor

from tsp import get_full_tsp_path
from reduce_graph_for_tsp import dijkstra_on_all_pair_of_nodes

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
dist_adj_matrix, route_matrix = dijkstra_on_all_pair_of_nodes(G, node_ids)
prettyPrintMatrix(dist_adj_matrix)
 
#Step 3: TSP
final_tsp_path, _ = get_full_tsp_path(node_ids[0], dist_adj_matrix, route_matrix)
ox.plot.plot_graph_route(G, final_tsp_path)

# Step 4: Manipulate graph edges:
factor = 0.5
G_new = manipulate_graph_edges_by_a_factor(G, factor)
avoid_right_turns = True

# Step 5: Dijkstra when avoiding right turns
dist_adj_matrix_after_weight, route_matrix_after_weight = dijkstra_on_all_pair_of_nodes(G_new, node_ids, avoid_right_turns)
prettyPrintMatrix(dist_adj_matrix_after_weight)

# Step 6: TSP on weighted graph when avoiding right turns
final_tsp_path_avoid_right_turns, _ = get_full_tsp_path(node_ids[0], dist_adj_matrix_after_weight, route_matrix_after_weight, avoid_right_turns)
ox.plot.plot_graph_route(G_new, final_tsp_path_avoid_right_turns)
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
ox.plot.plot_graph(G)

n1 = G.nodes[416913103]
n2 = G.nodes[338834142]
n3 = G.nodes[423810866]
n4 = G.nodes[27207873]
n5 = G.nodes[60179781]

node_ids = [n1['osmid'], n2['osmid'], n3['osmid'], n4['osmid'], n5['osmid']]
"""
# If choosing 10 nodes:
node_ids = [4970354696, 299318091, 1527511101, 7920174485, 24934369, 2025181550, 6547690048, 27089501, 5576447478, 1677663614]
"""
# Step 2: Dijkstra
dist_adj_matrix, route_matrix = dijkstra_on_all_pair_of_nodes(G, node_ids)
prettyPrintMatrix(dist_adj_matrix)
 
#Step 3: TSP
final_tsp_path = get_full_tsp_path(node_ids, dist_adj_matrix, route_matrix)
ox.plot.plot_graph_route(G, final_tsp_path)

# Step 4: Manipulate graph edges:
print("\nNow when trying to avoid right turns:\n")
factor = 0.9
G_new = manipulate_graph_edges_by_a_factor(G, factor)
avoid_right_turns = True

# Step 5: Dijkstra when avoiding right turns
# To preload data:
# uncomment next line and comment all subsequent lines in step 5.
from data import route_matrix_after_weight, dist_adj_matrix_after_weight

# dist_adj_matrix_after_weight, route_matrix_after_weight = dijkstra_on_all_pair_of_nodes(G_new, node_ids, avoid_right_turns)
# print("dist_adj_matrix_after_weight = ", dist_adj_matrix_after_weight)
# print("route_matrix_after_weight = ", route_matrix_after_weight)

# Step 6: TSP on weighted graph when avoiding right turns
final_tsp_path_avoid_right_turns = get_full_tsp_path(node_ids, dist_adj_matrix_after_weight, route_matrix_after_weight, avoid_right_turns)

ox.plot.plot_graph_route(G_new, final_tsp_path_avoid_right_turns)
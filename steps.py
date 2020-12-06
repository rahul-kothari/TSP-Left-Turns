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

from dijkstra_shortest_path import dijkstra
from reduce_graph_for_tsp import dijkstra_on_all_pair_of_nodes
from manipulate_edges import manipulate_graph_edges_by_a_factor

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
adj_matrix = dijkstra_on_all_pair_of_nodes(G, node_ids)
prettyPrintMatrix(adj_matrix)

"""
#Step 3: TSP
#TODO

# Step 4: Manipulate graph edges:
factor = 0.5
G_new = manipulate_graph_edges_by_a_factor(G, factor)
avoid_right_turns = True

# Step 5: Dijkstra when avoiding right turns
adj_matrix = dijkstra_on_all_pair_of_nodes(G, node_ids, avoid_right_turns=avoid_right_turns)
print(adj_matrix)

# Step 6:
# TODO!
"""
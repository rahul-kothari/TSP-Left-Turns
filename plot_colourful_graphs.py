"""
Given a TSP path (e.g. [4,3,1,0,2] on Liverpool graph, plot each sub-route with a diff colour (GitHub Issue #8 - https://github.com/rahul-kothari/TSP-Left-Turns/issues/8))
"""

import osmnx as ox
from data import route_matrix_after_weight, dist_adj_matrix_after_weight

G = ox.graph_from_place('Liverpool, North West England, England, United Kingdom')
ox.bearing.add_edge_bearings(G)

n1 = G.nodes[416913103]
n2 = G.nodes[338834142]
n3 = G.nodes[423810866]
n4 = G.nodes[27207873]
n5 = G.nodes[60179781]
node_ids = [n1['osmid'], n2['osmid'], n3['osmid'], n4['osmid'], n5['osmid']]

path_idx = [4,3,1,0,2]


routes = []
for i in range(len(path_idx)):
    routes.append(route_matrix_after_weight[i-1][i])

colours = ['r', 'g', 'b', 'y', 'c']
ox.plot.plot_graph_routes(G, routes, colours)
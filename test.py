import osmnx as ox
import numpy as np
# https://towardsdatascience.com/find-and-plot-your-optimal-path-using-plotly-and-networkx-in-python-17e75387b873
# https://osmnx.readthedocs.io/en/stable/osmnx.html?highlight=GET_NODE#module-osmnx.plot

G = ox.graph.graph_from_xml("map-uni.osm")
# OR: (uncomment below)
# G = ox.graph_from_place('Liverpool, North West England, England, United Kingdom')
ox.plot_graph(G)

# Get nodes and edges like so:
nodes =  list(G.nodes(data=True))
edges =  list(G.edges(data=True))

# Get the shortest route (dijkstra algorithm) from 1 node to another.
starting_node_id = nodes[0][0]
destination_node_id = nodes[-1][0]
route = ox.distance.shortest_path(G, starting_node_id, destination_node_id, weight = 'length')
ox.plot.plot_graph_route(G, route)
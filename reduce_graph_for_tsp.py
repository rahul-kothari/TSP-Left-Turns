import networkx as nx
from dijkstra_shortest_path import dijkstra

def reduce_graph(G: nx.MultiDiGraph, node_ids: list): 
	"""
	Given a list of nodes, carry out dijkstra for each pair of nodes and return a adjacent matrix. 
	adj_matrix represents the shortest distance to go from node_ids[i] to node_ids[j].

	Parameters:
	G: nx.MultiDiGraph
		(imported from osm file with bidirectional=True)
	node_ids: list
		list of node ids from osm.

	Returns:
	adj_matrix: 2D array n*n, n = len of nodes.
	"""
	n = len(node_ids)
	# create a n * n adjacent matrix.
	adj_matrix = [[-1 for x in range(n)] for x in range(n)]

	for i in range(n):
		for j in range(n):
			if (i == j):
				continue
			starting_node_id = node_ids[i]
			destination_node_id = node_ids[j]

			adj_matrix[i][j] = dijkstra(G, starting_node_id, destination_node_id)[1]

	return adj_matrix

if __name__ == "__main__":
	import osmnx as ox

	G = ox.graph.graph_from_xml("map-uni.osm", bidirectional=True)
	ox.bearing.add_edge_bearings(G)
	nodes =  list(G.nodes())
		
	# Select n nodes with their ids:
	n1 = int(nodes[0])
	n2 = int(nodes[5])
	n3 = int(nodes[-5])
	n4 = int(nodes[-1])
	selected_nodes = [n1, n2, n3, n4]
	
	adj_matrix = reduce_graph(G, selected_nodes)
	print(adj_matrix)

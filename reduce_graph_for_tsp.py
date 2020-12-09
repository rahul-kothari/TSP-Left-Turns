import networkx as nx
from dijkstra_shortest_path import dijkstra

def dijkstra_on_all_pair_of_nodes(G: nx.MultiDiGraph, node_ids: list, avoid_right_turns=False): 
	"""
	Given a list of nodes, carry out dijkstra for each pair of nodes and return a adjacent matrix. 
	adj_matrix represents the shortest distance to go from node_ids[i] to node_ids[j].

	Parameters:
	G: nx.MultiDiGraph
		(imported from osm file with bidirectional=True)
	node_ids: list
		list of node ids from osm.
	avoid_right_turns: boolean

	Returns:
	adj_matrix: 2D array n*n, n = len of nodes.
	route_matrix: path from point a to point b
	"""
	n = len(node_ids)
	# create a n * n adjacent matrix.
	adj_matrix = [[-1 for x in range(n)] for x in range(n)]
	route_matrix = [[-1 for x in range(n)] for x in range(n)]

	for i in range(n):
		for j in range(n):
			if (i == j):
				continue
			starting_node_id = node_ids[i]
			destination_node_id = node_ids[j]
			print("Calculating shortest path b/w indices ", i ," and ", j)

			if avoid_right_turns:
				# use custom dijkstra.
				route_matrix[i][j], adj_matrix[i][j] = dijkstra(G, starting_node_id, destination_node_id, avoid_right_turns)
			else:
				# Use networkX' dijkstra as it is more optimal.
				adj_matrix[i][j] = round(nx.shortest_path_length(G, starting_node_id, destination_node_id, weight = 'length'), 2)
				route_matrix[i][j] = nx.shortest_path(G, starting_node_id, destination_node_id, weight = 'length')

	return adj_matrix, route_matrix

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
	
	adj_matrix, route_matrix = dijkstra_on_all_pair_of_nodes(G, selected_nodes)
	print(adj_matrix)
	print(route_matrix)

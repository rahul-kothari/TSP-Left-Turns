from reduce_graph_for_tsp import dijkstra_on_all_pair_of_nodes
import tsp 
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
	
adj_matrix, _ = dijkstra_on_all_pair_of_nodes(G, selected_nodes)
print(adj_matrix)

r = range(len(adj_matrix))
dist = {(i,j): adj_matrix[i][j] for i in r for j in r}
print(tsp.tsp(r, dist))
import osmnx as ox
import copy

def manipulate_graph_edges_by_a_factor(G, factor: float):
	"""
	Given a graph, modifies all edge lengths by a factor

	Parameters
		G: nx.MultiDiGraph
		factor: flaot

	Returns
		new graph.
	"""
	# Make a deepcopy to not modify original graph.
	G_new = copy.deepcopy(G)	
	edges = list(G_new.edges(data=True))

	# modify edge lenght. In python, this changes the value in the list and also in the G_new.
	for edge in edges:
		edge[2]['length'] = edge[2]['length']*factor
		
	return G_new

if __name__ == "__main__":
    
	G = ox.graph.graph_from_xml("map-uni.osm", bidirectional=True)
	old_edges = list(G.edges(data=True))
	
	factor = 0.1
	G_altered = manipulate_graph(G, factor)
	altered_edges = list(G_altered.edges(data=True))

	for i in range(0,5):
		print(old_edges[i])
		print(altered_edges[i])
		print()
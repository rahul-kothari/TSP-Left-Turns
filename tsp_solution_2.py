from reduce_graph_for_tsp import reduce_graph
import osmnx as ox
from tsp_solver.greedy import solve_tsp
from dijkstra_shortest_path import dijkstra

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
#print(adj_matrix)

path = solve_tsp(adj_matrix)
#print(path)

loop_list = []


for i in range(0,len(path)):
    #print(path[i])
    if path[i] == 0:
        loop_list.append(selected_nodes[0])
    elif path[i] == 1:
        loop_list.append(selected_nodes[1])
    elif path[i] == 2:
        loop_list.append(selected_nodes[2])
    elif path[i] == 3:
        loop_list.append(selected_nodes[3])


#print(selected_nodes)
print(loop_list)

tsp_path_list = []

print("PATH: ")
for i in range(0, len(loop_list) - 1):
    route = dijkstra(G, loop_list[i], loop_list[i+1], False)
    for j in route[0]:
        tsp_path_list.append(j)
    #print(route)


tsp_path_list = list(dict.fromkeys(tsp_path_list))

#print(tsp_path_list)


ox.plot.plot_graph_route(G, tsp_path_list)

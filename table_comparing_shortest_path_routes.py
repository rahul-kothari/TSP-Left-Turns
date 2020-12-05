import networkx as nx
import osmnx as ox
from dijkstra_shortest_path import dijkstra

G = ox.graph_from_place('Liverpool, North West England, England, United Kingdom')
ox.bearing.add_edge_bearings(G)

n1 = G.nodes[416913103]
n2 = G.nodes[338834142]
n3 = G.nodes[423810866]
n4 = G.nodes[27207873]
n5 = G.nodes[60179781]


# OSMNX ROUTES:
r12_ox = ox.distance.shortest_path(G, n1['osmid'], n2['osmid'], weight = 'length') 
r13_ox = ox.distance.shortest_path(G, n1['osmid'], n3['osmid'], weight = 'length') 
r23_ox = ox.distance.shortest_path(G, n2['osmid'], n3['osmid'], weight = 'length') 
r24_ox = ox.distance.shortest_path(G, n2['osmid'], n4['osmid'], weight = 'length')  
r25_ox = ox.distance.shortest_path(G, n2['osmid'], n5['osmid'], weight = 'length') 
r34_ox = ox.distance.shortest_path(G, n3['osmid'], n4['osmid'], weight = 'length') 
r35_ox = ox.distance.shortest_path(G, n3['osmid'], n5['osmid'], weight = 'length') 
r45_ox = ox.distance.shortest_path(G, n4['osmid'], n5['osmid'], weight = 'length')



#OSMNX ROUTE DITANCE
r12_ox_dist = nx.shortest_path_length(G, n1['osmid'], n2['osmid'], weight = 'length')
r12_ox_dist = nx.shortest_path_length(G, n1['osmid'], n2['osmid'], weight = 'length')
r12_ox_dist = nx.shortest_path_length(G, n1['osmid'], n2['osmid'], weight = 'length')
r13_ox_dist = nx.shortest_path_length(G, n1['osmid'], n3['osmid'], weight = 'length')
r23_ox_dist = nx.shortest_path_length(G, n2['osmid'], n3['osmid'], weight = 'length')
r24_ox_dist = nx.shortest_path_length(G, n2['osmid'], n4['osmid'], weight = 'length')
r25_ox_dist = nx.shortest_path_length(G, n2['osmid'], n5['osmid'], weight = 'length')
r34_ox_dist = nx.shortest_path_length(G, n3['osmid'], n4['osmid'], weight = 'length')
r35_ox_dist = nx.shortest_path_length(G, n3['osmid'], n5['osmid'], weight = 'length')
r45_ox_dist = nx.shortest_path_length(G, n4['osmid'], n5['osmid'], weight = 'length')



# MY DIJKSTRA ROUTE
r12_me,r12_me_dist = dijkstra(G, n1['osmid'], n2['osmid']) 
r13_me,r13_me_dist = dijkstra(G, n1['osmid'], n3['osmid']) 
r23_me,r23_me_dist = dijkstra(G, n2['osmid'], n3['osmid']) 
r24_me,r24_me_dist = dijkstra(G, n2['osmid'], n4['osmid']) 
r25_me,r25_me_dist = dijkstra(G, n2['osmid'], n5['osmid']) 
r34_me,r34_me_dist = dijkstra(G, n3['osmid'], n4['osmid']) 
r35_me,r35_me_dist = dijkstra(G, n3['osmid'], n5['osmid']) 
r45_me,r45_me_dist = dijkstra(G, n4['osmid'], n5['osmid'])



#AVIOD RIGHT TURN ROUTE
r12_avoid,r12_avoid_dist = dijkstra(G, n1['osmid'], n2['osmid'], True) 
r13_avoid,r13_avoid_dist = dijkstra(G, n1['osmid'], n3['osmid'], True) 
r23_avoid,r23_avoid_dist = dijkstra(G, n2['osmid'], n3['osmid'], True) 
r24_avoid,r24_avoid_dist = dijkstra(G, n2['osmid'], n4['osmid'], True) 
r25_avoid,r25_avoid_dist = dijkstra(G, n2['osmid'], n5['osmid'], True) 
r34_avoid,r34_avoid_dist = dijkstra(G, n3['osmid'], n4['osmid'], True) 
r35_avoid,r35_avoid_dist = dijkstra(G, n3['osmid'], n5['osmid'], True) 
r45_avoid,r45_avoid_dist = dijkstra(G, n4['osmid'], n5['osmid'], True)



print("\nr12:")
print("routes equal ? ", r12_ox == r12_me, ", number of nodes in route: ", len(r12_ox))
print("distances equal? ", round(r12_ox_dist,2) == r12_me_dist, ", dist traversed: ", r12_me_dist)
print("avoid right turns: num of nodes in route - ", len(r12_avoid), " dist traversed: ", r12_avoid_dist)

print("\nr13:")
print("ox and my dijkstra routes equal ? ", r13_ox == r13_me, ", number of nodes in route: ", len(r13_ox))
print("ox and my dijkstra distances equal? ", round(r13_ox_dist,2) == r13_me_dist, ", dist traversed: ", r13_me_dist)
print("avoid right turns: num of nodes in route - ", len(r13_avoid), " dist traversed: ", r13_avoid_dist)

print("\nr23:")
print("ox and my dijkstra routes equal ? ", r23_ox == r23_me), ", number of nodes in route: ", len(r23_ox)
print("ox and my dijkstra distances equal? ", round(r23_ox_dist,2) == r23_me_dist, ", dist traversed: ", r23_me_dist)
print("avoid right turns: num of nodes in route - ", len(r23_avoid), " dist traversed: ", r23_avoid_dist)

print("\nr24:")
print("ox and my dijkstra routes equal ? ", r24_ox == r24_me, ", number of nodes in route: ", len(r24_ox))
print("ox and my dijkstra distances equal? ", round(r24_ox_dist,2) == r24_me_dist, ", dist traversed: ", r24_me_dist)
print("avoid right turns: num of nodes in route - ", len(r24_avoid), " dist traversed: ", r24_avoid_dist)

print("\nr25:")
print("ox and my dijkstra routes equal ? ", r25_ox == r25_me, ", number of nodes in route: ", len(r25_ox))
print("ox and my dijkstra distances equal? ", round(r25_ox_dist,2) == r25_me_dist, ", dist traversed: ", r25_me_dist)
print("avoid right turns: num of nodes in route - ", len(r25_avoid), " dist traversed: ", r25_avoid_dist)

print("\nr34:")
print("ox and my dijkstra routes equal ? ", r34_ox == r34_me, ", number of nodes in route: ", len(r34_ox))
print("ox and my dijkstra distances equal? ", round(r34_ox_dist,2) == r34_me_dist, ", dist traversed: ", r34_me_dist)
print("avoid right turns: num of nodes in route - ", len(r34_avoid), " dist traversed: ", r34_avoid_dist)

print("\nr35:")
print("ox and my dijkstra routes equal ? ", r35_ox == r35_me, ", number of nodes in route: ", len(r35_ox))
print("ox and my dijkstra distances equal? ", round(r35_ox_dist,2) == r35_me_dist, ", dist traversed: ", r35_me_dist)
print("avoid right turns: num of nodes in route - ", len(r35_avoid), " dist traversed: ", r35_avoid_dist)

print("\nr45:")
print("ox and my dijkstra routes equal ? ", r45_ox == r45_me, ", number of nodes in route: ", len(r45_ox))
print("ox and my dijkstra distances equal? ", round(r45_ox_dist,2) == r45_me_dist, ", dist traversed: ", r45_me_dist)
print("avoid right turns: num of nodes in route - ", len(r45_avoid), " dist traversed: ", r45_avoid_dist)


#### Plot graph:
rs = [r12_avoid, r13_avoid, r23_avoid, r24_avoid, r25_avoid, r34_avoid, r35_avoid, r45_avoid]
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'orange', 'fuchsia']
ox.plot.plot_graph_routes(G, rs, colors)

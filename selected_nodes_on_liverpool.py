from dijkstra_shortest_path import dijkstra
import osmnx as ox

G = ox.graph_from_place('Liverpool, North West England, England, United Kingdom')
ox.bearing.add_edge_bearings(G)

"""
nodes = list(G.nodes(data = False))
edges = list(G.edges(data = False))

n1s = list(filter(lambda node: node[1]['y'] > 53.46, nodes)) 
n2s = list(filter(lambda node: node[1]['x'] < -2.98 and node[1]['y'] > 53.42, nodes)) 
n3s = list(filter(lambda node: node[1]['x'] > -2.86 and node[1]['y'] > 53.387 and node[1]['y'] < 53.4, nodes))
n4s = list(filter(lambda node: node[1]['x'] < -2.90 and node[1]['x'] > -2.93  and node[1]['y'] > 53.35 and node[1]['y'] < 53.36, nodes))
n5s = list(filter(lambda node: node[1]['x'] > -2.84 and node[1]['y'] < 53.346, nodes))

n1 = n1s[100] # 416913103
n2 = n2s[100] # 338834142
n3 = n3s[100] # 423810866
n4 = n4s[100] # 27207873
n5 = n5s[100] # 60179781

r12 = ox.distance.shortest_path(G, n1[0], n2[0], weight = 'length') 
r13 = ox.distance.shortest_path(G, n1[0], n3[0], weight = 'length') 
r23 = ox.distance.shortest_path(G, n2[0], n3[0], weight = 'length') 
r24 = ox.distance.shortest_path(G, n2[0], n4[0], weight = 'length')  
r25 = ox.distance.shortest_path(G, n2[0], n5[0], weight = 'length') 
r34 = ox.distance.shortest_path(G, n3[0], n4[0], weight = 'length') 
r35 = ox.distance.shortest_path(G, n3[0], n5[0], weight = 'length') 
r45 = ox.distance.shortest_path(G, n4[0], n5[0], weight = 'length')
"""

n1 = G.nodes[416913103]
n2 = G.nodes[338834142]
n3 = G.nodes[423810866]
n4 = G.nodes[27207873]
n5 = G.nodes[60179781]

r12,dist = dijkstra(G, n1['osmid'], n2['osmid'], False) 
print("r12 done - dist = ", dist)
r13,dist = dijkstra(G, n1['osmid'], n3['osmid'], False) 
print("r13 done - dist = ", dist)
r23,dist = dijkstra(G, n2['osmid'], n3['osmid'], False) 
print("r23 done - dist = ", dist)
r24,dist = dijkstra(G, n2['osmid'], n4['osmid'], False)  
print("r24 done - dist = ", dist)
r25,dist = dijkstra(G, n2['osmid'], n5['osmid'], False) 
print("r25 done - dist = ", dist)
r34,dist = dijkstra(G, n3['osmid'], n4['osmid'], False) 
print("r34 done - dist = ", dist)
r35,dist = dijkstra(G, n3['osmid'], n5['osmid'], False) 
print("r35 done - dist = ", dist)
r45,dist = dijkstra(G, n4['osmid'], n5['osmid'], False)
print("r45 done - dist = ", dist)

rs = [r12, r13, r23, r24, r25, r34, r35, r45]
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'orange', 'fuchsia']
ox.plot.plot_graph_routes(G, rs, colors)